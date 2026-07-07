from __future__ import annotations

import logging
from datetime import datetime, timedelta, time
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import dt as dt_util

from .const import CONSUMPTION_IMPORT_DELAY_DAYS, UPDATE_INTERVAL
from .invoice_pdf import InvoicePdfManager
from .lib.octopus_spain_fork import OctopusSpain

_LOGGER = logging.getLogger(__name__)
PDF_REFRESH_BUFFER = timedelta(minutes=5)


def _parse_invoice_expiry(value: Any) -> datetime | None:
    """Parse a stored invoice PDF expiry into UTC."""
    if not value:
        return None
    parsed = dt_util.parse_datetime(str(value))
    if parsed is None:
        return None
    return dt_util.as_utc(parsed)


def _invoice_pdf_needs_refresh(invoice: dict[str, Any] | None) -> bool:
    """Return whether the invoice PDF URL is missing or close to expiry."""
    if not invoice:
        return True
    if not invoice.get("pdf"):
        return True
    expires_at = _parse_invoice_expiry(invoice.get("pdf_expires_at"))
    if expires_at is None:
        return True
    return expires_at <= dt_util.utcnow() + PDF_REFRESH_BUFFER


class OctopusCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """DataUpdateCoordinator for Octopus Spain accounts."""

    def __init__(self, hass: HomeAssistant, email: str | None, password: str | None, api_key: str | None) -> None:
        super().__init__(
            hass=hass,
            logger=_LOGGER,
            name="Octopus Spain",
            update_interval=timedelta(hours=UPDATE_INTERVAL),
        )
        self._api = OctopusSpain(email, password, api_key)
        self._data: dict[str, Any] = {}
        self._invoice_refreshing_accounts: set[str] = set()
        self.pdf_manager = InvoicePdfManager(hass)

    async def _async_update_data(self) -> dict[str, Any]:
        if await self._api.login():
            self._data = {}
            accounts = await self._api.accounts()
            for account in accounts:
                acc = await self._api.account(account)
                # Download the PDF right away, while the presigned URL is fresh.
                await self._async_attach_local_pdf(account, acc)
                try:
                    acc["contract"] = await self._api.supply_points(account)
                except Exception:
                    _LOGGER.warning(
                        "Failed to fetch contract details for account %s",
                        account,
                        exc_info=True,
                    )
                    acc["contract"] = None
                if "hourly_consumption" not in acc:
                    acc["hourly_consumption"] = await self._async_seed_hourly(
                        account, self._api.hourly_consumption
                    )
                if acc.get("has_solar_wallet") and "hourly_generation" not in acc:
                    acc["hourly_generation"] = await self._async_seed_hourly(
                        account, self._api.hourly_generation
                    )
                self._data[account] = acc
        return self._data

    async def _async_seed_hourly(self, account: str, fetcher) -> list[dict[str, Any]]:
        """Fetch the initial small window of hourly measurements."""
        measurements: list[dict[str, Any]] = []
        today = dt_util.as_local(dt_util.utcnow()).date()
        end_day = today - timedelta(days=CONSUMPTION_IMPORT_DELAY_DAYS)
        start_day = end_day - timedelta(days=2)
        day_cursor = start_day
        while day_cursor < end_day:
            day_start = datetime.combine(day_cursor, time.min, dt_util.UTC)
            day_end = day_start + timedelta(days=1)
            fetched = await fetcher(account, start=day_start, end=day_end)
            if fetched:
                measurements.extend(fetched)
            day_cursor += timedelta(days=1)
        return measurements

    async def _async_attach_local_pdf(self, account: str, acc: dict[str, Any]) -> None:
        """Store the invoice PDF locally and expose its durable path/URL."""
        invoice = acc.get("last_invoice") if isinstance(acc, dict) else None
        if not isinstance(invoice, dict):
            return
        local = await self.pdf_manager.async_ensure_downloaded(account, invoice)
        invoice["local_path"] = local.get("local_path") if local else None
        invoice["local_url"] = local.get("local_url") if local else None

    async def async_fetch_hourly_consumption(
        self,
        account: str,
        start: datetime,
        end: datetime,
    ) -> list[dict[str, Any]]:
        """Fetch hourly consumption for a specific range."""
        return await self._api.hourly_consumption(account, start=start, end=end)

    async def async_fetch_daily_consumption(
        self,
        account: str,
        start: datetime,
        end: datetime,
    ) -> list[dict[str, Any]]:
        """Fetch daily consumption for a specific range."""
        return await self._api.daily_consumption(account, start=start, end=end)

    async def async_fetch_hourly_generation(
        self,
        account: str,
        start: datetime,
        end: datetime,
    ) -> list[dict[str, Any]]:
        """Fetch hourly solar generation (export) for a specific range."""
        return await self._api.hourly_generation(account, start=start, end=end)

    async def async_fetch_daily_generation(
        self,
        account: str,
        start: datetime,
        end: datetime,
    ) -> list[dict[str, Any]]:
        """Fetch daily solar generation (export) for a specific range."""
        return await self._api.daily_generation(account, start=start, end=end)

    async def async_refresh_account_invoice(self, account: str) -> bool:
        """Refresh billing data for a single account without reloading consumption."""
        if account in self._invoice_refreshing_accounts:
            return False

        self._invoice_refreshing_accounts.add(account)
        try:
            current = self._data.get(account, {})
            current_invoice = current.get("last_invoice", {}) if isinstance(current, dict) else {}
            current_pdf = current_invoice.get("pdf")

            try:
                refreshed = await self._api.account(account)
                if not refreshed:
                    return False

                refreshed_invoice = (
                    refreshed.get("last_invoice", {}) if isinstance(refreshed, dict) else {}
                )
                refreshed_pdf = refreshed_invoice.get("pdf")
                refreshed_needs_retry = _invoice_pdf_needs_refresh(refreshed_invoice)
                current_needs_refresh = _invoice_pdf_needs_refresh(current_invoice)

                if refreshed_needs_retry and (
                    refreshed_pdf == current_pdf or current_needs_refresh
                ):
                    _LOGGER.debug(
                        "Invoice refresh for %s returned a stale or expiring PDF URL; retrying with fresh login",
                        account,
                    )
                    relogged = await self._api.account(account, force_login=True)
                    if relogged:
                        refreshed = relogged
                        refreshed_invoice = (
                            refreshed.get("last_invoice", {})
                            if isinstance(refreshed, dict)
                            else {}
                        )
            except Exception:
                _LOGGER.warning(
                    "Invoice refresh for account %s failed", account, exc_info=True
                )
                return False

            if refreshed_invoice.get("id") is None:
                # The API returned the empty fallback payload; keep the data
                # we already have instead of clobbering it with None values.
                _LOGGER.debug(
                    "Invoice refresh for %s returned no invoice data; keeping current data",
                    account,
                )
                return False

            merged = {**current, **refreshed}
            for preserved_key in ("hourly_consumption", "hourly_generation", "contract"):
                if preserved_key in current and preserved_key not in merged:
                    merged[preserved_key] = current[preserved_key]

            await self._async_attach_local_pdf(account, merged)

            new_data = dict(self._data)
            new_data[account] = merged
            self._data = new_data
            self.async_set_updated_data(new_data)
            return True
        finally:
            self._invoice_refreshing_accounts.discard(account)

    async def async_download_invoice(self, account: str) -> bool:
        """Force a (re-)download of the account's latest invoice PDF."""
        current = self._data.get(account)
        if not isinstance(current, dict):
            _LOGGER.warning("Cannot download invoice: unknown account %s", account)
            return False

        invoice = current.get("last_invoice") or {}
        if _invoice_pdf_needs_refresh(invoice):
            # The stored presigned URL is stale; fetch a fresh one first.
            await self.async_refresh_account_invoice(account)
            current = self._data.get(account) or {}
            invoice = current.get("last_invoice") or {}

        local = await self.pdf_manager.async_ensure_downloaded(
            account, invoice, force=True
        )
        if local is None:
            return False

        invoice["local_path"] = local["local_path"]
        invoice["local_url"] = local["local_url"]
        new_data = dict(self._data)
        new_data[account] = {**current, "last_invoice": invoice}
        self._data = new_data
        self.async_set_updated_data(new_data)
        return True
