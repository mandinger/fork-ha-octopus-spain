from __future__ import annotations

import logging
from datetime import datetime, timedelta, time
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import dt as dt_util

from .const import CONSUMPTION_IMPORT_DELAY_DAYS, UPDATE_INTERVAL
from .lib.octopus_spain_fork import OctopusSpain

_LOGGER = logging.getLogger(__name__)


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

    async def _async_update_data(self) -> dict[str, Any]:
        if await self._api.login():
            self._data = {}
            accounts = await self._api.accounts()
            for account in accounts:
                acc = await self._api.account(account)
                if "hourly_consumption" not in acc:
                    hourly_consumption: list[dict[str, Any]] = []
                    today = dt_util.as_local(dt_util.utcnow()).date()
                    end_day = today - timedelta(days=CONSUMPTION_IMPORT_DELAY_DAYS)
                    start_day = end_day - timedelta(days=2)
                    day_cursor = start_day
                    while day_cursor < end_day:
                        day_start = datetime.combine(day_cursor, time.min, dt_util.UTC)
                        day_end = day_start + timedelta(days=1)
                        fetched = await self._api.hourly_consumption(
                            account, start=day_start, end=day_end
                        )
                        if fetched:
                            hourly_consumption.extend(fetched)
                        day_cursor += timedelta(days=1)
                    acc["hourly_consumption"] = hourly_consumption
                self._data[account] = acc
        return self._data

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

    async def async_refresh_account_invoice(self, account: str) -> bool:
        """Refresh billing data for a single account without reloading consumption."""
        if account in self._invoice_refreshing_accounts:
            return False

        self._invoice_refreshing_accounts.add(account)
        try:
            refreshed = await self._api.account(account)
            if not refreshed:
                return False

            current = self._data.get(account, {})
            merged = {**current, **refreshed}
            if "hourly_consumption" in current and "hourly_consumption" not in merged:
                merged["hourly_consumption"] = current["hourly_consumption"]

            new_data = dict(self._data)
            new_data[account] = merged
            self._data = new_data
            self.async_set_updated_data(new_data)
            return True
        finally:
            self._invoice_refreshing_accounts.discard(account)
