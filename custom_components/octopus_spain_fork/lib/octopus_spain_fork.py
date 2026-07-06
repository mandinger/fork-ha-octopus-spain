from datetime import datetime, timedelta, time, timezone
import logging
import os
from typing import Optional
from urllib.parse import parse_qs, urlparse

from python_graphql_client import GraphqlClient
from homeassistant.util import dt as dt_util

GRAPH_QL_ENDPOINT = "https://api.oees-kraken.energy/v1/graphql/"
SOLAR_WALLET_LEDGER = "SOLAR_WALLET_LEDGER"
ELECTRICITY_LEDGER = "SPAIN_ELECTRICITY_LEDGER"

_LOGGER = logging.getLogger(__name__)


def _empty_account_payload(
    solar_wallet: Optional[float] = None,
    octopus_credit: Optional[float] = None,
) -> dict:
    """Fallback account payload used when billing data cannot be fetched."""
    return {
        'solar_wallet': solar_wallet,
        'octopus_credit': octopus_credit,
        'has_solar_wallet': False,
        'billing': None,
        'payment_forecast': None,
        'last_invoice': {
            # Primary value and mirrors
            'amount': None,
            'invoiced_amount': None,
            # Totals
            'gross_total': None,
            'net_total': None,
            'tax_total': None,
            # Dates and identifiers
            'issued': None,
            'earliest_charge_at': None,
            'pdf': None,
            'pdf_expires_at': None,
            'id': None,
            # Legacy fields kept for compatibility
            'start': None,
            'end': None,
        }
    }


def _to_local_date_str(iso_str: Optional[str]) -> Optional[str]:
    """Parse an ISO8601 datetime string and return local date (YYYY-MM-DD).

    - Accepts timezone-aware or naive inputs; naive treated as UTC.
    - Returns a string for JSON-serializable HA attributes.
    """
    if not iso_str:
        return None
    try:
        dt: Optional[datetime] = dt_util.parse_datetime(iso_str)
        if dt is None:
            # Fallback for strict fromisoformat and trailing Z
            iso_norm = iso_str.replace("Z", "+00:00")
            dt = datetime.fromisoformat(iso_norm)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        dt_local = dt_util.as_local(dt)
        return dt_local.date().isoformat()
    except Exception:  # pragma: no cover - robust to any parse edge
        _LOGGER.debug("Failed to parse datetime '%s' for local date", iso_str, exc_info=True)
        try:
            # Last ditch: return the first 10 chars if it looks like a date
            return iso_str[:10]
        except Exception:
            return None


def _parse_presigned_url_expiry(url: Optional[str]) -> Optional[str]:
    """Return the UTC expiration timestamp for a presigned URL."""
    if not url:
        return None

    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        issued_raw = query.get("X-Amz-Date", [None])[0]
        expires_raw = query.get("X-Amz-Expires", [None])[0]
        if not issued_raw or not expires_raw:
            return None

        issued_at = datetime.strptime(issued_raw, "%Y%m%dT%H%M%SZ").replace(
            tzinfo=timezone.utc
        )
        expires_at = issued_at + timedelta(seconds=int(expires_raw))
        return expires_at.isoformat()
    except (TypeError, ValueError):
        _LOGGER.debug("Unable to parse presigned URL expiry from %s", url, exc_info=True)
        return None


class OctopusSpain:
    def __init__(self, email, password, apikey):
        self._email = email
        self._password = password
        self._apikey = apikey
        self._token = None

    async def login(self):
        mutation = """
           mutation obtainKrakenToken($input: ObtainJSONWebTokenInput!) {
              obtainKrakenToken(input: $input) {
                token
              }
            }
        """
        if self._apikey is None:
            variables = {"input": {"email": self._email, "password": self._password}}
        else:
            variables = {"input": {"APIKey": self._apikey}}

        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT)
        response = await client.execute_async(mutation, variables)

        if "errors" in response:
            return False

        self._token = response["data"]["obtainKrakenToken"]["token"]
        return True

    async def regenerate_api_key(self) -> str | None:
        """Generate a new API key for the authenticated user.

        Returns the generated key when successful, otherwise None.
        """
        if self._token is None:
            if not await self.login():
                return None

        mutation = """
            mutation regenerateSecretKey {
              regenerateSecretKey {
                key
              }
            }
        """
        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(mutation)
        if "errors" in response:
            _LOGGER.error("GraphQL errors while regenerating API key: %s", response["errors"])
            return None

        return (
            response.get("data", {})
            .get("regenerateSecretKey", {})
            .get("key")
        )

    async def accounts(self):
        query = """
             query getAccountNames{
                viewer {
                    accounts {
                        ... on Account {
                            number
                        }
                    }
                }
            }
            """

        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(query)

        return list(map(lambda a: a["number"], response["data"]["viewer"]["accounts"]))

    async def hourly_consumption(
        self,
        account: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
    ):
        return await self._consumption(
            account=account,
            reading_frequency_type="HOUR_INTERVAL",
            start=start,
            end=end,
        )

    async def daily_consumption(
        self,
        account: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
    ):
        return await self._consumption(
            account=account,
            reading_frequency_type="DAY_INTERVAL",
            start=start,
            end=end,
        )

    async def hourly_generation(
        self,
        account: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
    ):
        return await self._consumption(
            account=account,
            reading_frequency_type="HOUR_INTERVAL",
            start=start,
            end=end,
            reading_direction="GENERATION",
        )

    async def daily_generation(
        self,
        account: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
    ):
        return await self._consumption(
            account=account,
            reading_frequency_type="DAY_INTERVAL",
            start=start,
            end=end,
            reading_direction="GENERATION",
        )

    async def _consumption(
        self,
        account: str,
        reading_frequency_type: str,
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
        reading_direction: str = "CONSUMPTION",
    ):
        api_timezone = self._api_timezone_name()
        query = """
            query getMeasurements(
                $account: String!,
                $startAt: DateTime!,
                $endAt: DateTime!,
                $utilityFilters: [UtilityFiltersInput!],
                $timezone: String
                ) {
                account(accountNumber: $account) {
                    properties {
                    id
                    measurements(
                        first: 1500,
                        utilityFilters: $utilityFilters,
                        startAt: $startAt,
                        endAt: $endAt,
                        timezone: $timezone
                    ) {
                        edges {
                        node {
                            value
                            unit
                            ... on IntervalMeasurementType {
                            startAt
                            endAt
                            }
                        }
                        }
                    }
                    }
                }
            }
        """

        if self._token is None:
            if not await self.login():
                _LOGGER.error(
                    "Unable to fetch %s consumption for account %s due to login failure",
                    reading_frequency_type.lower(),
                    account,
                )
                return []

        tz = timezone.utc
        now_utc = datetime.now(tz)

        if end is None:
            end_local = datetime.combine(now_utc.date() + timedelta(days=1), time.min, tzinfo=tz)
        else:
            end_local = end if end.tzinfo else end.replace(tzinfo=tz)
            end_local = end_local.astimezone(tz)

        if start is None:
            default_start = now_utc.date() - timedelta(days=1)
            start_local = datetime.combine(default_start, time.min, tzinfo=tz)
        else:
            start_local = start if start.tzinfo else start.replace(tzinfo=tz)
            start_local = start_local.astimezone(tz)

        if start_local >= end_local:
            _LOGGER.debug(
                "Skipping %s consumption request for account %s because start %s >= end %s",
                reading_frequency_type.lower(),
                account,
                start_local,
                end_local,
            )
            return []

        start_utc = start_local.astimezone(timezone.utc)
        end_utc = end_local.astimezone(timezone.utc)

        def to_utc_iso_z(dt: datetime) -> str:
            return dt.isoformat(timespec="milliseconds").replace("+00:00", "Z")

        variables = {
            "account": account,
            "startAt": to_utc_iso_z(start_utc),
            "endAt": to_utc_iso_z(end_utc),
            "timezone": api_timezone,
            "utilityFilters": [
                {
                    "electricityFilters": {
                        "readingDirection": reading_direction,
                        "readingFrequencyType": reading_frequency_type,
                    }
                }
            ],
        }
        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(query, variables)
        if "errors" in response:
            _LOGGER.error(
                "GraphQL errors while fetching %s %s for account %s: %s",
                reading_frequency_type.lower(),
                reading_direction.lower(),
                account,
                response["errors"],
            )
            return []

        _LOGGER.debug(
            "%s %s query for account %s executed. Start=%s End=%s Timezone=%s",
            reading_frequency_type,
            reading_direction,
            account,
            variables["startAt"],
            variables["endAt"],
            api_timezone,
        )

        props = response.get("data", {}).get("account", {}).get("properties", [])
        if not props:
            _LOGGER.warning(
                "No properties returned in %s consumption response for account %s",
                reading_frequency_type.lower(),
                account,
            )
            return []
        try:
            edges = props[0]["measurements"]["edges"]
        except (KeyError, IndexError, TypeError) as err:
            _LOGGER.error(
                "Unexpected %s consumption response format for account %s: %s",
                reading_frequency_type.lower(),
                account,
                err,
            )
            _LOGGER.debug(
                "%s consumption raw response for account %s: %s",
                reading_frequency_type,
                account,
                response,
            )
            return []

        if not edges:
            _LOGGER.debug(
                "%s consumption response returned 0 measurements for account %s",
                reading_frequency_type,
                account,
            )
            return []

        return [
            {
                "value": edge["node"]["value"],
                "unit": edge["node"]["unit"],
                "startAt": edge["node"].get("startAt"),
                "endAt": edge["node"].get("endAt"),
            }
            for edge in edges
        ]

    @staticmethod
    def _api_timezone_name() -> str:
        """Return the IANA timezone name to request measurements in."""
        default_tz = getattr(dt_util, "DEFAULT_TIME_ZONE", None)
        timezone_name = getattr(default_tz, "key", None)
        if not timezone_name and default_tz is not None:
            timezone_name = str(default_tz)
        if not timezone_name:
            return "Etc/GMT"
        return timezone_name.replace('"', "")

    async def account(self, account: str, *, force_login: bool = False):
        # Ensure we're authenticated (mirror logic from hourly_consumption)
        if force_login:
            self._token = None
        if self._token is None:
            if not await self.login():
                _LOGGER.error(
                    "Unable to fetch billing info for account %s due to login failure",
                    account,
                )
                return _empty_account_payload()

        query = """
            query ($account: String!) {
              account(accountNumber: $account) {
                billingOptions {
                  currentBillingPeriodStartDate
                  currentBillingPeriodEndDate
                  nextBillingDate
                  isFixed
                  periodStartDay
                }
                paginatedPaymentForecast(first: 1) {
                  edges {
                    node {
                      amount
                      date
                    }
                  }
                }
                ledgers {
                  ledgerType
                  balance
                  invoices(last: 1) {
                    edges {
                      node {
                        id
                        invoicedAmount
                        earliestChargeAt
                        firstIssued
                        pdfUrl
                        totalCharges {
                          grossTotal
                          netTotal
                          taxTotal
                        }
                      }
                    }
                  }
                }
              }
            }
        """
        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(query, {"account": account})
        if not isinstance(response, dict) or "errors" in response:
            _LOGGER.error(
                "Failed to fetch billing info for account %s: %s",
                account,
                response.get("errors") if isinstance(response, dict) else "no response from API",
            )
            return _empty_account_payload()

        # The API can return {"data": null} or {"data": {"account": null}}
        # without an "errors" key; chained .get(..., {}) does not protect
        # against explicit nulls (see issue #29).
        data = response.get("data")
        account_data = (data or {}).get("account") or {}
        if not account_data:
            _LOGGER.error(
                "Billing info response contained no account data for account %s: %s",
                account,
                response.get("errors") or "null data",
            )
            return _empty_account_payload()

        def cents_to_eur(value):
            try:
                return float(value) / 100 if value is not None else None
            except (TypeError, ValueError):
                return None

        billing_options = account_data.get("billingOptions") or {}
        billing = {
            "period_start": billing_options.get("currentBillingPeriodStartDate"),
            "period_end": billing_options.get("currentBillingPeriodEndDate"),
            "next_billing_date": billing_options.get("nextBillingDate"),
            "is_fixed": billing_options.get("isFixed"),
            "period_start_day": billing_options.get("periodStartDay"),
        } if billing_options else None

        forecast_edges = (account_data.get("paginatedPaymentForecast") or {}).get("edges") or []
        forecast_node = (forecast_edges[0] or {}).get("node") if forecast_edges else None
        payment_forecast = {
            "amount": cents_to_eur(forecast_node.get("amount")),
            "date": forecast_node.get("date"),
        } if isinstance(forecast_node, dict) else None

        ledgers = account_data.get("ledgers") or []
        if not isinstance(ledgers, list):
            _LOGGER.error(
                "Billing info ledgers payload unexpected for account %s: %s",
                account,
                type(ledgers).__name__,
            )
            ledgers = []
        ledgers = [ledger for ledger in ledgers if isinstance(ledger, dict)]
        electricity = next(filter(lambda x: x.get('ledgerType') == ELECTRICITY_LEDGER, ledgers), None)
        solar_wallet = next(filter(lambda x: x.get('ledgerType') == SOLAR_WALLET_LEDGER, ledgers), None)
        has_solar_wallet = solar_wallet is not None
        if solar_wallet is None:
            solar_wallet = {'balance': 0}

        if not electricity:
            _LOGGER.warning(
                "Electricity ledger not found in billing info for account %s (ledgers: %s)",
                account,
                [ledger.get('ledgerType') for ledger in ledgers],
            )
            return _empty_account_payload()

        invs = electricity.get("invoices") or {}
        invoices = invs.get("edges") or []

        try:
            bal_preview = float(electricity.get("balance")) / 100.0
        except Exception:
            bal_preview = None
        _LOGGER.debug(
            "Billing ledger for %s: ledgerType=%s balance_eur=%s invoices_edges=%s keys=%s",
            account,
            electricity.get('ledgerType'),
            bal_preview,
            len(invoices) if isinstance(invoices, list) else 'n/a',
            list(electricity.keys()),
        )

        if len(invoices) == 0:
            # Ledgers are valid even without invoices: keep the balances.
            payload = _empty_account_payload(
                solar_wallet=(float(solar_wallet.get("balance", 0)) / 100),
                octopus_credit=(float(electricity.get("balance", 0)) / 100),
            )
            payload["has_solar_wallet"] = has_solar_wallet
            payload["billing"] = billing
            payload["payment_forecast"] = payment_forecast
            return payload

        invoice = invoices[0].get("node", {}) if isinstance(invoices[0], dict) else {}

        # Los timedelta son bastante chapuzas, habrá que arreglarlo
        # Parse monetary values (API returns cents) and dates
        invoiced_amount_cents = invoice.get("invoicedAmount")
        charges = invoice.get("totalCharges") or {}
        gross_cents = charges.get("grossTotal")
        net_cents = charges.get("netTotal")
        tax_cents = charges.get("taxTotal")

        def parse_iso_date(value: Optional[str]) -> Optional[str]:
            # Keep name for compatibility but use timezone-aware local conversion
            return _to_local_date_str(value)

        return {
            "solar_wallet": (float(solar_wallet.get("balance", 0)) / 100),
            "octopus_credit": (float(electricity.get("balance", 0)) / 100),
            "has_solar_wallet": has_solar_wallet,
            "billing": billing,
            "payment_forecast": payment_forecast,
            "last_invoice": {
                # State (euros): prefer invoicedAmount as the main amount
                "amount": cents_to_eur(gross_cents),
                # New fields from invoices API (euros)
                "invoiced_amount": cents_to_eur(invoiced_amount_cents),
                "gross_total": cents_to_eur(gross_cents),
                "net_total": cents_to_eur(net_cents),
                "tax_total": cents_to_eur(tax_cents),
                # Dates (parsed to date)
                "issued": parse_iso_date(invoice.get("firstIssued")),
                "earliest_charge_at": parse_iso_date(invoice.get("earliestChargeAt")),
                "pdf": invoice.get("pdfUrl"),
                "pdf_expires_at": _parse_presigned_url_expiry(invoice.get("pdfUrl")),
                "id": invoice.get("id"),
            },
        }

    async def supply_points(self, account: str) -> Optional[dict]:
        """Fetch contract/tariff details for the account's electricity supply point.

        Returns a normalized dict for the first supply point of the first
        property (multi-CUPS accounts are not yet supported), or None when the
        data cannot be fetched.
        """
        if self._token is None:
            if not await self.login():
                _LOGGER.error(
                    "Unable to fetch supply points for account %s due to login failure",
                    account,
                )
                return None

        query = """
            query getSupplyPoints($account: String!) {
              account(accountNumber: $account) {
                properties {
                  electricitySupplyPoints {
                    cups
                    status
                    selfConsumption
                    supplierChangeInProgress
                    activeAgreement {
                      validFrom
                      validTo
                      product {
                        code
                        displayName
                        fullName
                        prices {
                          variableTerm
                          variableTermWithTaxes
                          variableTermUnits
                          fixedTerm
                          fixedTermWithTaxes
                          fixedTermUnits
                          dailyFee
                          dailyFeeWithTaxes
                          surplusRate
                          surplusRateUnits
                          marginTerm
                        }
                      }
                      details {
                        contractualMaxPower
                      }
                    }
                  }
                }
              }
            }
        """
        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(query, {"account": account})
        if not isinstance(response, dict) or "errors" in response:
            _LOGGER.warning(
                "Failed to fetch supply points for account %s: %s",
                account,
                response.get("errors") if isinstance(response, dict) else "no response from API",
            )
            return None

        account_data = (response.get("data") or {}).get("account") or {}
        properties = account_data.get("properties") or []
        supply_point = None
        for prop in properties:
            points = (prop or {}).get("electricitySupplyPoints") or []
            points = [point for point in points if isinstance(point, dict)]
            if points:
                supply_point = points[0]
                if len(points) > 1 or len(properties) > 1:
                    _LOGGER.debug(
                        "Account %s has multiple properties/supply points; using the first one",
                        account,
                    )
                break
        if supply_point is None:
            _LOGGER.debug("No electricity supply points returned for account %s", account)
            return None

        agreement = supply_point.get("activeAgreement") or {}
        product = agreement.get("product") or {}
        prices = product.get("prices") or {}
        details = agreement.get("details") or {}

        def to_float_list(values) -> list[float]:
            result = []
            for value in values or []:
                try:
                    result.append(float(value))
                except (TypeError, ValueError):
                    continue
            return result

        def to_float(value) -> Optional[float]:
            try:
                return float(value) if value is not None else None
            except (TypeError, ValueError):
                return None

        return {
            "cups": supply_point.get("cups"),
            "status": supply_point.get("status"),
            "self_consumption": supply_point.get("selfConsumption"),
            "supplier_change_in_progress": supply_point.get("supplierChangeInProgress"),
            "valid_from": _to_local_date_str(agreement.get("validFrom")),
            "valid_to": _to_local_date_str(agreement.get("validTo")),
            "product_code": product.get("code"),
            "product_display_name": product.get("displayName"),
            "product_full_name": product.get("fullName"),
            "prices": {
                "variable_term": to_float_list(prices.get("variableTerm")),
                "variable_term_with_taxes": to_float_list(prices.get("variableTermWithTaxes")),
                "variable_term_units": prices.get("variableTermUnits"),
                "fixed_term": to_float_list(prices.get("fixedTerm")),
                "fixed_term_with_taxes": to_float_list(prices.get("fixedTermWithTaxes")),
                "fixed_term_units": prices.get("fixedTermUnits"),
                "daily_fee": to_float(prices.get("dailyFee")),
                "daily_fee_with_taxes": to_float(prices.get("dailyFeeWithTaxes")),
                "surplus_rate": to_float(prices.get("surplusRate")),
                "surplus_rate_units": prices.get("surplusRateUnits"),
                "margin_term": to_float(prices.get("marginTerm")),
            },
            "contracted_power": to_float_list(details.get("contractualMaxPower")),
        }
