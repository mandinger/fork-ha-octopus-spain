from datetime import datetime, timedelta, time, timezone
import logging
import os
from typing import Optional

from python_graphql_client import GraphqlClient
from homeassistant.util import dt as dt_util

GRAPH_QL_ENDPOINT = "https://api.oees-kraken.energy/v1/graphql/"
SOLAR_WALLET_LEDGER = "SOLAR_WALLET_LEDGER"
ELECTRICITY_LEDGER = "SPAIN_ELECTRICITY_LEDGER"

_LOGGER = logging.getLogger(__name__)


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

        query = """
            query getMeasurements(
                $account: String!,
                $startAt: DateTime!,
                $endAt: DateTime!,
                $utilityFilters: [UtilityFiltersInput!]
                ) {
                account(accountNumber: $account) {
                    properties {
                    id
                    measurements(
                        first: 1500,
                        utilityFilters: $utilityFilters,
                        startAt: $startAt,
                        endAt: $endAt,
                        timezone: "Etc/GMT"
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
                    "Unable to fetch hourly consumption for account %s due to login failure",
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
                "Skipping hourly consumption request for account %s because start %s >= end %s",
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
            "utilityFilters":[{"electricityFilters": {"readingDirection": "CONSUMPTION","readingFrequencyType": "HOUR_INTERVAL"}}]
        }
        headers = {"authorization": self._token}
        client = GraphqlClient(endpoint=GRAPH_QL_ENDPOINT, headers=headers)
        response = await client.execute_async(query, variables)
        if "errors" in response:
            _LOGGER.error(
                "GraphQL errors while fetching hourly consumption for account %s: %s",
                account,
                response["errors"],
            )
            return []

        _LOGGER.debug(
            "Hourly consumption query for account %s executed. Start=%s End=%s",
            account,
            variables["startAt"],
            variables["endAt"],
        )

        props = response.get("data", {}).get("account", {}).get("properties", [])
        if not props:
            _LOGGER.warning(
                "No properties returned in hourly consumption response for account %s",
                account,
            )
            return []
        try:
            edges = props[0]["measurements"]["edges"]
        except (KeyError, IndexError, TypeError) as err:
            _LOGGER.error(
                "Unexpected hourly consumption response format for account %s: %s",
                account,
                err,
            )
            _LOGGER.debug(
                "Hourly consumption raw response for account %s: %s", account, response
            )
            return []

        if not edges:
            _LOGGER.debug(
                "Hourly consumption response returned 0 measurements for account %s",
                account,
            )
            return []

        measurements = [
            {
                "value": edge["node"]["value"],
                "unit": edge["node"]["unit"],
                "startAt": edge["node"]["startAt"],
                "endAt": edge["node"]["endAt"],
            }
            for edge in edges
        ]
        return measurements

    async def account(self, account: str):
        # Ensure we're authenticated (mirror logic from hourly_consumption)
        if self._token is None:
            if not await self.login():
                _LOGGER.error(
                    "Unable to fetch billing info for account %s due to login failure",
                    account,
                )
                return {
                    'solar_wallet': None,
                    'octopus_credit': None,
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
                        'id': None,
                        # Legacy fields kept for compatibility
                        'start': None,
                        'end': None,
                    }
                }

        # --- Helpers: proper timezone-aware conversion ---
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

        query = """
            query ($account: String!) {
              account(accountNumber: $account) {
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
        ledgers = response.get("data", {}).get("account", {}).get("ledgers", [])
        if not isinstance(ledgers, list):
            _LOGGER.error(
                "Billing info ledgers payload unexpected for account %s: %s",
                account,
                type(ledgers).__name__,
            )
            ledgers = []
        electricity = next(filter(lambda x: x['ledgerType'] == ELECTRICITY_LEDGER, ledgers), None)
        solar_wallet = next(filter(lambda x: x['ledgerType'] == SOLAR_WALLET_LEDGER, ledgers), {'balance': 0})

        if not electricity:
            raise Exception("Electricity ledger not found")

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
            return {
                'solar_wallet': None,
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
                    'id': None,
                    # Legacy fields kept for compatibility
                    'start': None,
                    'end': None,
                }
            }

        invoice = invoices[0].get("node", {}) if isinstance(invoices[0], dict) else {}

        # Los timedelta son bastante chapuzas, habrá que arreglarlo
        # Parse monetary values (API returns cents) and dates
        invoiced_amount_cents = invoice.get("invoicedAmount")
        charges = invoice.get("totalCharges") or {}
        gross_cents = charges.get("grossTotal")
        net_cents = charges.get("netTotal")
        tax_cents = charges.get("taxTotal")

        def cents_to_eur(value):
            try:
                return float(value) / 100 if value is not None else None
            except (TypeError, ValueError):
                return None

        def parse_iso_date(value: Optional[str]) -> Optional[str]:
            # Keep name for compatibility but use timezone-aware local conversion
            return _to_local_date_str(value)

        return {
            "solar_wallet": (float(solar_wallet.get("balance", 0)) / 100),
            "octopus_credit": (float(electricity.get("balance", 0)) / 100),
            "last_invoice": {
                # State (euros): prefer invoicedAmount as the main amount
                "amount": cents_to_eur(invoiced_amount_cents),
                # New fields from invoices API (euros)
                "invoiced_amount": cents_to_eur(invoiced_amount_cents),
                "gross_total": cents_to_eur(gross_cents),
                "net_total": cents_to_eur(net_cents),
                "tax_total": cents_to_eur(tax_cents),
                # Dates (parsed to date)
                "issued": parse_iso_date(invoice.get("firstIssued")),
                "earliest_charge_at": parse_iso_date(invoice.get("earliestChargeAt")),
                "pdf": invoice.get("pdfUrl"),
                "id": invoice.get("id"),
            },
        }
