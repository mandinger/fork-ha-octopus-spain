import logging
from inspect import iscoroutinefunction
from datetime import datetime, date, time, timedelta
from decimal import Decimal, InvalidOperation
from typing import Any, Mapping, Callable

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
    SensorDeviceClass,
)
from homeassistant.const import (
    CURRENCY_EURO,
    UnitOfEnergy,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util
from homeassistant.util import slugify

from homeassistant.components.recorder import get_instance
from homeassistant.components.recorder.statistics import (
    async_add_external_statistics,
    get_last_statistics,
)
try:
    from homeassistant.components.recorder.statistics import STATISTIC_SUM
except ImportError:  # pragma: no cover - fallback if constant missing
    STATISTIC_SUM = "sum"
from .const import DOMAIN
from .coordinator import OctopusCoordinator
from .runtime import OctopusSpainConfigEntry

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: OctopusSpainConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = entry.runtime_data.coordinator
    await coordinator.async_config_entry_first_refresh()

    sensors = []
    accounts = list(coordinator.data)
    single_account = len(accounts) == 1
    for account in accounts:
        # Wallets
        sensors.append(
            OctopusWallet(account, "solar_wallet", "Solar Wallet", coordinator, single_account)
        )
        sensors.append(
            OctopusWallet(
                account, "octopus_credit", "Octopus Credit", coordinator, single_account
            )
        )
        # Aggregate invoice entity (back-compat)
        sensors.append(OctopusInvoice(account, coordinator, single_account))

        # Individual Last Invoice fields
        name_prefix = "Factura" if single_account else f"Factura ({account})"
        # Monetary fields (euros)
        sensors.extend(
            [
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="invoiced_amount",
                    name=f"{name_prefix}: Importe facturado",
                    icon="mdi:cash",
                    unit=CURRENCY_EURO,
                    is_numeric=True,
                ),
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="gross_total",
                    name=f"{name_prefix}: Total bruto",
                    icon="mdi:scale-balance",
                    unit=CURRENCY_EURO,
                    is_numeric=True,
                ),
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="net_total",
                    name=f"{name_prefix}: Total neto",
                    icon="mdi:scale-balance",
                    unit=CURRENCY_EURO,
                    is_numeric=True,
                ),
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="tax_total",
                    name=f"{name_prefix}: Impuestos",
                    icon="mdi:percent",
                    unit=CURRENCY_EURO,
                    is_numeric=True,
                ),
            ]
        )
        # Dates
        sensors.extend(
            [
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="issued",
                    name=f"{name_prefix}: Emitida",
                    icon="mdi:calendar-month",
                    device_class=SensorDeviceClass.DATE,
                ),
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="earliest_charge_at",
                    name=f"{name_prefix}: Inicio cargos",
                    icon="mdi:calendar-start",
                    device_class=SensorDeviceClass.DATE,
                ),
            ]
        )
        # PDF URL and ID
        sensors.extend(
            [
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="pdf",
                    name=f"{name_prefix}: PDF",
                    icon="mdi:file-pdf-box",
                ),
                OctopusInvoiceFieldSensor(
                    account,
                    coordinator,
                    field="id",
                    name=f"{name_prefix}: ID",
                    icon="mdi:identifier",
                ),
            ]
        )
    for account in accounts:
        importer = OctopusConsumptionStatisticsImporter(
            hass=hass,
            coordinator=coordinator,
            account=account,
            single=single_account,
        )
        await importer.async_setup()
        entry.async_on_unload(importer.close)

    async_add_entities(sensors)


class OctopusWallet(CoordinatorEntity[OctopusCoordinator], SensorEntity):

    def __init__(
        self,
        account: str,
        key: str,
        name: str,
        coordinator: OctopusCoordinator,
        single: bool,
    ) -> None:
        super().__init__(coordinator=coordinator)
        self._state = None
        self._key = key
        self._account = account
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = name if single else f"{name} ({account})"
        self._attr_unique_id = f"{key}_{account}"
        self.entity_description = SensorEntityDescription(
            key=f"{key}_{account}",
            icon="mdi:piggy-bank-outline",
            native_unit_of_measurement=CURRENCY_EURO,
            state_class=SensorStateClass.MEASUREMENT
        )

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._handle_coordinator_update()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._state = self.coordinator.data[self._account].get(self._key)
        self.async_write_ha_state()

    @property
    def native_value(self) -> StateType:
        return self._state


class OctopusInvoice(CoordinatorEntity[OctopusCoordinator], SensorEntity):

    def __init__(self, account: str, coordinator: OctopusCoordinator, single: bool) -> None:
        super().__init__(coordinator=coordinator)
        self._state = None
        self._account = account
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = "Última Factura Octopus" if single else f"Última Factura Octopus ({account})"
        self._attr_unique_id = f"last_invoice_{account}"
        self.entity_description = SensorEntityDescription(
            key=f"last_invoice_{account}",
            icon="mdi:currency-eur",
            native_unit_of_measurement=CURRENCY_EURO,
            state_class=SensorStateClass.MEASUREMENT
        )

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._handle_coordinator_update()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        prefix = f"OctopusInvoice[{self._account}]"
        try:
            account_data = self.coordinator.data.get(self._account)
            if not account_data:
                _LOGGER.debug("%s: no account data available yet", prefix)
                self._state = None
                self._attrs = {}
                self.async_write_ha_state()
                return

            inv = account_data.get('last_invoice')
            if not inv:
                _LOGGER.debug("%s: 'last_invoice' not present in coordinator data", prefix)
                self._state = None
                self._attrs = {}
                self.async_write_ha_state()
                return

            # Determine the best amount field to use for state
            amount = (
                inv.get('amount')
                if inv.get('amount') is not None
                else inv.get('invoiced_amount')
                if inv.get('invoiced_amount') is not None
                else inv.get('gross_total')
            )
            # Coerce to float when possible; leave as None if missing
            try:
                self._state = float(amount) if amount is not None else None
            except (TypeError, ValueError):
                _LOGGER.debug("%s: invalid amount value on invoice: %s", prefix, amount)
                self._state = None

            # Attributes: ensure they are JSON-serializable (strings)
            def _to_str(v: Any) -> Any:
                if v is None:
                    return None
                return v.isoformat() if hasattr(v, 'isoformat') else str(v)

            self._attrs = {
                # Legacy fields if still present
                'Inicio': _to_str(inv.get('start')),
                'Fin': _to_str(inv.get('end')),
                # New API fields
                'Emitida': _to_str(inv.get('issued')),
                'Inicio cargos': _to_str(inv.get('earliest_charge_at')),
                'Total bruto': inv.get('gross_total'),
                'Total neto': inv.get('net_total'),
                'Impuestos': inv.get('tax_total'),
                'Importe facturado': inv.get('invoiced_amount'),
                'ID': inv.get('id'),
                'PDF': inv.get('pdf'),
            }

            _LOGGER.debug(
                "%s: updated invoice state amount=%s attrs=%s",
                prefix,
                self._state,
                self._attrs,
            )
            self.async_write_ha_state()
        except Exception as err:  # pragma: no cover - defensive guard
            _LOGGER.exception("%s: error processing invoice update: %s", prefix, err)

    @property
    def native_value(self) -> StateType:
        return self._state

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        return self._attrs


class OctopusInvoiceFieldSensor(CoordinatorEntity[OctopusCoordinator], SensorEntity):
    """Expose individual fields from last_invoice as separate sensors."""

    def __init__(
        self,
        account: str,
        coordinator: OctopusCoordinator,
        field: str,
        name: str,
        icon: str | None = None,
        unit: str | None = None,
        device_class: SensorDeviceClass | None = None,
        is_numeric: bool = False,
    ) -> None:
        super().__init__(coordinator=coordinator)
        self._state: StateType = None
        self._account = account
        self._field = field
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = name
        self._attr_unique_id = f"last_invoice_{field}_{account}"
        desc_kwargs: dict[str, Any] = {
            "key": f"last_invoice_{field}_{account}",
        }
        if icon:
            desc_kwargs["icon"] = icon
        if unit:
            desc_kwargs["native_unit_of_measurement"] = unit
        if device_class is not None:
            desc_kwargs["device_class"] = device_class
        # Only set MEASUREMENT for numeric monetary values
        if is_numeric:
            desc_kwargs["state_class"] = SensorStateClass.MEASUREMENT
        self.entity_description = SensorEntityDescription(**desc_kwargs)
        self._is_numeric = is_numeric

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        self._handle_coordinator_update()

    @callback
    def _handle_coordinator_update(self) -> None:
        prefix = f"OctopusInvoiceField[{self._account}:{self._field}]"
        try:
            account_data = self.coordinator.data.get(self._account)
            if not account_data:
                _LOGGER.debug("%s: no account data available yet", prefix)
                self._state = None
                self._attrs = {}
                self.async_write_ha_state()
                return

            inv = account_data.get("last_invoice") or {}
            raw = inv.get(self._field)
            # Handle date device class: needs date/datetime, not string
            if (
                getattr(self.entity_description, "device_class", None)
                == SensorDeviceClass.DATE
            ):
                val: date | None = None
                if isinstance(raw, date):
                    val = raw
                elif isinstance(raw, datetime):
                    val = raw.date()
                elif isinstance(raw, str):
                    # Expect YYYY-MM-DD; fall back to parse_datetime
                    try:
                        val = date.fromisoformat(raw)
                    except Exception:
                        dtp = dt_util.parse_datetime(raw)
                        if dtp is not None:
                            val = dt_util.as_local(dtp).date()
                self._state = val
            elif self._is_numeric and raw is not None:
                try:
                    self._state = float(raw)
                except (TypeError, ValueError):
                    _LOGGER.debug("%s: invalid numeric value: %s", prefix, raw)
                    self._state = None
            else:
                # Non-numeric/text fields. Special-case long PDF URLs (state limit 255)
                if self._field == "pdf":
                    url = str(raw) if raw is not None else None
                    self._attrs = {"url": url} if url else {}
                    # keep state short and indicative
                    self._state = "available" if url else None
                else:
                    self._state = raw if raw is not None else None

            _LOGGER.debug("%s: state=%s", prefix, self._state)
            self.async_write_ha_state()
        except Exception as err:  # pragma: no cover - defensive guard
            _LOGGER.exception("%s: error updating field sensor: %s", prefix, err)

    @property
    def native_value(self) -> StateType:
        return self._state

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        return self._attrs

class OctopusConsumptionStatisticsImporter:
    """Process coordinator data to feed historical consumption into statistics."""

    def __init__(
        self,
        hass: HomeAssistant,
        coordinator: OctopusCoordinator,
        account: str,
        single: bool,
    ) -> None:
        self._hass = hass
        self._coordinator = coordinator
        self._account = account
        safe_account = slugify(account)
        self._statistic_id = f"{DOMAIN}:energy_consumption_{safe_account}"
        self._name = "Consumo Electrico" if single else f"Consumo Electrico ({account})"
        self._remove_listener: Callable[[], None] | None = None
        self._reconcile_warning_fingerprint_by_day: dict[date, tuple[int, float, float]] = {}
        self._negative_consumption_fingerprints: set[str] = set()

    async def async_setup(self) -> None:
        """Run an initial sync and subscribe to coordinator updates."""
        await self._async_process_update()
        self._remove_listener = self._coordinator.async_add_listener(self._schedule_update)

    def close(self) -> None:
        """Unsubscribe from coordinator updates."""
        if self._remove_listener:
            self._remove_listener()
            self._remove_listener = None

    def _schedule_update(self) -> None:
        """Schedule processing for the latest coordinator data."""
        self._hass.async_create_task(self._async_process_update())

    @staticmethod
    def _parse_stat_start(value: Any) -> datetime | None:
        if isinstance(value, (int, float)):
            return dt_util.utc_from_timestamp(value)
        if isinstance(value, str):
            parsed = dt_util.parse_datetime(value)
            if parsed is not None:
                return dt_util.as_utc(parsed)
            return None
        if isinstance(value, datetime):
            if value.tzinfo is None:
                return value.replace(tzinfo=dt_util.UTC)
            return dt_util.as_utc(value)
        return None

    def _parse_non_negative_kwh(self, raw_value: Any, *, prefix: str, label: str) -> float | None:
        try:
            value = float(Decimal(raw_value))
        except (InvalidOperation, ValueError, TypeError):
            return None

        if value < 0:
            fingerprint = f"{label}:{value:.6f}"
            if fingerprint not in self._negative_consumption_fingerprints:
                self._negative_consumption_fingerprints.add(fingerprint)
                _LOGGER.warning(
                    "%s: negative consumption ignored at %s (value=%.6f kWh)",
                    prefix,
                    label,
                    value,
                )
            return None
        return value

    async def _async_add_statistics(self, metadata: dict[str, Any], statistics: list[dict[str, Any]]) -> None:
        if not statistics:
            return
        if iscoroutinefunction(async_add_external_statistics):
            await async_add_external_statistics(self._hass, metadata, statistics)
        else:
            await self._hass.async_add_executor_job(
                async_add_external_statistics, self._hass, metadata, statistics
            )

    async def _async_reconcile_current_month(
        self,
        *,
        prefix: str,
        metadata: dict[str, Any],
        today_utc: date,
    ) -> None:
        month_start_day = today_utc.replace(day=1)
        complete_until = today_utc - timedelta(days=1)
        if complete_until < month_start_day:
            return

        range_start = datetime.combine(month_start_day, time.min, dt_util.UTC)
        range_end = datetime.combine(complete_until + timedelta(days=1), time.min, dt_util.UTC)
        daily_rows = await self._coordinator.async_fetch_daily_consumption(
            self._account,
            range_start,
            range_end,
        )
        if not daily_rows:
            _LOGGER.debug("%s: monthly reconcile daily pull returned no rows", prefix)
            return

        daily_by_day: dict[date, float] = {}
        for row in daily_rows:
            start_at = row.get("startAt")
            if not isinstance(start_at, str):
                continue
            parsed_start = dt_util.parse_datetime(start_at)
            if parsed_start is None:
                continue
            day = dt_util.as_utc(parsed_start).date()
            if day < month_start_day or day > complete_until:
                continue
            parsed_daily = self._parse_non_negative_kwh(
                row.get("value"),
                prefix=prefix,
                label=f"daily:{day.isoformat()}",
            )
            if parsed_daily is None:
                continue
            daily_by_day[day] = parsed_daily

        if not daily_by_day:
            _LOGGER.debug("%s: monthly reconcile has no comparable daily totals", prefix)
            return

        stats_window = ((complete_until.day + 2) * 24) + 48
        existing = await get_instance(self._hass).async_add_executor_job(
            get_last_statistics,
            self._hass,
            stats_window,
            self._statistic_id,
            True,
            {STATISTIC_SUM},
        )
        existing_points_raw = existing.get(self._statistic_id, [])
        existing_points: list[tuple[datetime, float]] = []
        existing_by_start: dict[datetime, float] = {}
        for point in existing_points_raw:
            parsed_start = self._parse_stat_start(point.get("start"))
            if parsed_start is None:
                continue
            raw_sum = point.get("sum")
            if raw_sum is None:
                raw_sum = point.get("state")
            try:
                parsed_sum = float(raw_sum)
            except (TypeError, ValueError):
                continue
            existing_points.append((parsed_start, parsed_sum))
            existing_by_start[parsed_start] = parsed_sum
        existing_points.sort(key=lambda item: item[0])

        tolerance_kwh = 0.05
        reconciled_days = 0

        for day in sorted(daily_by_day):
            day_start = datetime.combine(day, time.min, dt_util.UTC)
            day_end = day_start + timedelta(days=1)

            prev_sum = 0.0
            day_last_sum: float | None = None
            day_hours_seen = 0
            for point_start, point_sum in existing_points:
                if point_start < day_start:
                    prev_sum = point_sum
                    continue
                if point_start >= day_end:
                    break
                day_last_sum = point_sum
                day_hours_seen += 1

            stored_day_total = None if day_last_sum is None else (day_last_sum - prev_sum)
            api_day_total = daily_by_day[day]
            delta = None if stored_day_total is None else (stored_day_total - api_day_total)

            needs_reconcile = (
                stored_day_total is None
                or day_hours_seen < 24
                or (delta is not None and abs(delta) > tolerance_kwh)
            )
            if not needs_reconcile:
                continue

            updated = await self._async_reconcile_day_from_hourly(
                prefix=prefix,
                metadata=metadata,
                day=day,
                api_day_total=api_day_total,
                existing_by_start=existing_by_start,
                existing_points=existing_points,
                tolerance_kwh=tolerance_kwh,
            )
            if updated:
                reconciled_days += 1

        if reconciled_days:
            _LOGGER.info(
                "%s: monthly reconcile updated statistics for %s day(s)",
                prefix,
                reconciled_days,
            )
        else:
            _LOGGER.debug("%s: monthly reconcile found no updatable mismatches", prefix)

    async def _async_reconcile_day_from_hourly(
        self,
        *,
        prefix: str,
        metadata: dict[str, Any],
        day: date,
        api_day_total: float,
        existing_by_start: dict[datetime, float],
        existing_points: list[tuple[datetime, float]],
        tolerance_kwh: float,
    ) -> bool:
        day_start = datetime.combine(day, time.min, dt_util.UTC)
        day_end = day_start + timedelta(days=1)
        hourly_rows = await self._coordinator.async_fetch_hourly_consumption(
            self._account,
            day_start,
            day_end,
        )
        if not hourly_rows:
            _LOGGER.warning(
                "%s: reconcile day %s skipped, hourly pull returned 0 rows",
                prefix,
                day.isoformat(),
            )
            return False

        hourly_values: dict[datetime, float] = {}
        for row in hourly_rows:
            start_at = row.get("startAt")
            if not isinstance(start_at, str):
                continue
            parsed = dt_util.parse_datetime(start_at)
            if parsed is None:
                continue
            start_utc = dt_util.as_utc(parsed)
            parsed_hourly = self._parse_non_negative_kwh(
                row.get("value"),
                prefix=prefix,
                label=f"hourly:{start_utc.isoformat()}",
            )
            if parsed_hourly is None:
                continue
            hourly_values[start_utc] = parsed_hourly

        if not hourly_values:
            _LOGGER.warning(
                "%s: reconcile day %s skipped, no parseable hourly rows",
                prefix,
                day.isoformat(),
            )
            return False

        present_hours = {dt.hour for dt in hourly_values}
        missing_hours = sorted(set(range(24)) - present_hours)
        hourly_total = sum(hourly_values.values())
        if missing_hours and abs(api_day_total - hourly_total) <= tolerance_kwh:
            for hour in missing_hours:
                hourly_values[day_start + timedelta(hours=hour)] = 0.0
            _LOGGER.debug(
                "%s: reconcile day %s filled %s missing hourly interval(s) with 0.0 kWh because daily total matches",
                prefix,
                day.isoformat(),
                len(missing_hours),
            )

        baseline_sum = 0.0
        for point_start, point_sum in existing_points:
            if point_start < day_start:
                baseline_sum = point_sum
            else:
                break

        running = baseline_sum
        day_statistics: list[dict[str, Any]] = []
        mismatch_count = 0
        max_abs_delta = 0.0
        first_mismatch_start: datetime | None = None
        for hour in range(24):
            slot_start = day_start + timedelta(hours=hour)
            if slot_start not in hourly_values:
                continue
            running += hourly_values[slot_start]
            existing_sum = existing_by_start.get(slot_start)
            if existing_sum is None:
                day_statistics.append(
                    {
                        "start": slot_start,
                        "state": running,
                        "sum": running,
                    }
                )
            elif abs(existing_sum - running) > tolerance_kwh:
                mismatch_count += 1
                point_abs_delta = abs(existing_sum - running)
                if point_abs_delta > max_abs_delta:
                    max_abs_delta = point_abs_delta
                if first_mismatch_start is None:
                    first_mismatch_start = slot_start

        if mismatch_count:
            # Avoid repeating exactly the same warning fingerprint on every refresh.
            fingerprint = (mismatch_count, round(max_abs_delta, 3), round(api_day_total, 3))
            last_fingerprint = self._reconcile_warning_fingerprint_by_day.get(day)
            if last_fingerprint != fingerprint:
                self._reconcile_warning_fingerprint_by_day[day] = fingerprint
                _LOGGER.warning(
                    "%s: reconcile day %s found %s existing statistic mismatch(es), first=%s, max_delta=%.3f kWh. Existing points are not overwritten.",
                    prefix,
                    day.isoformat(),
                    mismatch_count,
                    first_mismatch_start.isoformat() if first_mismatch_start else "n/a",
                    max_abs_delta,
                )
            else:
                _LOGGER.debug(
                    "%s: reconcile day %s mismatch fingerprint unchanged (%s mismatch(es), max_delta=%.3f kWh), suppressing repeated warning",
                    prefix,
                    day.isoformat(),
                    mismatch_count,
                    max_abs_delta,
                )

        if not day_statistics:
            return False

        await self._async_add_statistics(metadata, day_statistics)
        for point in day_statistics:
            start = point["start"]
            sum_value = point["sum"]
            existing_by_start[start] = sum_value
            existing_points.append((start, sum_value))
        existing_points.sort(key=lambda item: item[0])
        _LOGGER.info(
            "%s: reconcile day %s added %s missing statistics point(s)",
            prefix,
            day.isoformat(),
            len(day_statistics),
        )
        return True

    async def _async_compare_hourly_vs_daily(
        self,
        *,
        prefix: str,
        measurements_by_start: dict[datetime, Any],
        today_utc: date,
    ) -> None:
        """Compare hourly-summed totals with API daily totals for diagnostics."""
        if not measurements_by_start:
            return

        # We diagnose a recent complete window to avoid noisy partial-day mismatches.
        complete_until = today_utc - timedelta(days=1)
        compare_days = 7
        compare_start_day = complete_until - timedelta(days=compare_days - 1)
        if compare_start_day > complete_until:
            return

        hourly_by_day: dict[date, float] = {}
        hours_seen_by_day: dict[date, set[int]] = {}
        for start_utc, item in measurements_by_start.items():
            day = start_utc.date()
            if day < compare_start_day or day > complete_until:
                continue
            val = self._parse_non_negative_kwh(
                item.get("value"),
                prefix=prefix,
                label=f"seed-hourly:{start_utc.isoformat()}",
            )
            if val is None:
                continue
            hourly_by_day[day] = hourly_by_day.get(day, 0.0) + val
            hours_seen_by_day.setdefault(day, set()).add(start_utc.hour)

        if not hourly_by_day:
            return

        range_start = datetime.combine(compare_start_day, time.min, dt_util.UTC)
        range_end = datetime.combine(complete_until + timedelta(days=1), time.min, dt_util.UTC)
        daily_rows = await self._coordinator.async_fetch_daily_consumption(
            self._account,
            range_start,
            range_end,
        )

        def _parse_start_at(value: Any) -> datetime | None:
            if not isinstance(value, str):
                return None
            parsed = dt_util.parse_datetime(value)
            if parsed is None:
                return None
            return dt_util.as_utc(parsed)

        daily_by_day: dict[date, float] = {}
        for row in daily_rows:
            start_at = _parse_start_at(row.get("startAt"))
            if start_at is None:
                continue
            day = start_at.date()
            if day < compare_start_day or day > complete_until:
                continue
            parsed_daily = self._parse_non_negative_kwh(
                row.get("value"),
                prefix=prefix,
                label=f"diag-daily:{day.isoformat()}",
            )
            if parsed_daily is None:
                continue
            daily_by_day[day] = parsed_daily

        if not daily_by_day:
            _LOGGER.debug("%s: daily diagnostic returned 0 comparable rows", prefix)
            return

        tolerance_kwh = 0.05
        for day in sorted(hourly_by_day):
            hourly_total = hourly_by_day[day]
            daily_total = daily_by_day.get(day)
            seen_hours = hours_seen_by_day.get(day, set())
            hours_seen = len(seen_hours)
            missing_hours = sorted(set(range(24)) - seen_hours)
            has_missing_hours = hours_seen < 24

            if daily_total is None:
                if has_missing_hours:
                    _LOGGER.warning(
                        "%s: missing hourly intervals for %s (hours_seen=%s/24, missing_hours=%s, hourly_total=%.3f kWh)",
                        prefix,
                        day.isoformat(),
                        hours_seen,
                        missing_hours,
                        hourly_total,
                    )
                _LOGGER.warning(
                    "%s: no daily value returned for %s while hourly data exists (hourly_total=%.3f kWh)",
                    prefix,
                    day.isoformat(),
                    hourly_total,
                )
                continue

            delta = hourly_total - daily_total
            if abs(delta) > tolerance_kwh:
                _LOGGER.warning(
                    "%s: hourly/daily mismatch on %s (hourly=%.3f kWh, daily=%.3f kWh, delta=%.3f kWh, hours_seen=%s/24, missing_hours=%s)",
                    prefix,
                    day.isoformat(),
                    hourly_total,
                    daily_total,
                    delta,
                    hours_seen,
                    missing_hours,
                )
            else:
                if has_missing_hours:
                    _LOGGER.debug(
                        "%s: hourly/daily aligned on %s despite missing intervals (hours_seen=%s/24, missing_hours=%s, hourly=%.3f kWh, daily=%.3f kWh, delta=%.3f kWh)",
                        prefix,
                        day.isoformat(),
                        hours_seen,
                        missing_hours,
                        hourly_total,
                        daily_total,
                        delta,
                    )
                else:
                    _LOGGER.debug(
                        "%s: hourly/daily aligned on %s (hourly=%.3f kWh, daily=%.3f kWh, delta=%.3f kWh)",
                        prefix,
                        day.isoformat(),
                        hourly_total,
                        daily_total,
                        delta,
                    )

    async def _async_process_update(self) -> None:
        prefix = f"OctopusConsumptionStats[{self._account}]"
        try:
            measurements_raw = self._coordinator.data[self._account].get("hourly_consumption", [])
            meas_count = len(measurements_raw) if isinstance(measurements_raw, list) else "unknown"
            _LOGGER.debug(
                "%s: fetched hourly measurements count=%s type=%s",
                prefix,
                meas_count,
                type(measurements_raw).__name__,
            )

            _LOGGER.debug(
                "%s: requesting last statistics statistic_id=%s",
                prefix,
                self._statistic_id,
            )
            last = await get_instance(self._hass).async_add_executor_job(
                get_last_statistics,
                self._hass,
                1,
                self._statistic_id,
                True,
                {STATISTIC_SUM},
            )
            _LOGGER.debug("%s: last statistics response=%s", prefix, last)

            last_points = last.get(self._statistic_id)
            last_start = None
            last_sum = 0.0
            if last_points:
                last_point = last_points[-1]

                last_start_raw = last_point.get("start")
                if isinstance(last_start_raw, (int, float)):
                    last_start = dt_util.utc_from_timestamp(last_start_raw)
                elif isinstance(last_start_raw, str):
                    parsed_start = dt_util.parse_datetime(last_start_raw)
                    if parsed_start is not None:
                        last_start = dt_util.as_utc(parsed_start)
                elif isinstance(last_start_raw, datetime):
                    if last_start_raw.tzinfo is None:
                        last_start = last_start_raw.replace(tzinfo=dt_util.UTC)
                    else:
                        last_start = dt_util.as_utc(last_start_raw)

                last_sum_raw = last_point.get("sum")
                if last_sum_raw is None:
                    last_sum_raw = last_point.get("state")
                try:
                    last_sum = float(last_sum_raw or 0.0)
                except (TypeError, ValueError):
                    last_sum = 0.0

                if last_point.get("sum") is None and last_point.get("state") is None:
                    _LOGGER.debug(
                        "%s: last statistics point lacks sum/state, re-importing from start",
                        prefix,
                    )
                    last_start = None
                    last_sum = 0.0

                _LOGGER.debug(
                    "%s: last statistics point start=%s last_sum=%s",
                    prefix,
                    last_start,
                    last_sum,
                )
            else:
                _LOGGER.debug("%s: no existing statistics found, starting fresh", prefix)

            now_utc = dt_util.utcnow()
            today_utc = now_utc.date()

            if last_start is None:
                fetch_start_day = now_utc.replace(
                    day=1, hour=0, minute=0, second=0, microsecond=0
                ).date()
            else:
                fetch_start_day = (last_start + timedelta(hours=1)).date()

            keep_from_utc = datetime.combine(fetch_start_day, time.min, dt_util.UTC)

            def _parse_dt(dt_str: str):
                dt = dt_util.parse_datetime(dt_str)
                if dt is None:
                    return None
                return dt_util.as_utc(dt)

            measurements_by_start: dict[datetime, Any] = {}
            skipped_seed_unparsed = 0
            skipped_seed_before_window = 0
            if isinstance(measurements_raw, list):
                for item in measurements_raw:
                    start_at = item.get("startAt")
                    if not start_at:
                        continue
                    start_utc = _parse_dt(start_at)
                    if start_utc is None:
                        skipped_seed_unparsed += 1
                        continue
                    if start_utc < keep_from_utc:
                        skipped_seed_before_window += 1
                        continue
                    measurements_by_start[start_utc] = item

            additional_count = 0
            fetched_days: list[date] = []
            skipped_additional_unparsed = 0
            skipped_additional_missing = 0

            if fetch_start_day <= today_utc:
                # Batch fetch in a single request to reduce API calls and avoid rate limits
                range_start = datetime.combine(fetch_start_day, time.min, dt_util.UTC)
                range_end = datetime.combine(today_utc + timedelta(days=1), time.min, dt_util.UTC)
                fetched_days.append(fetch_start_day)
                fetched = await self._coordinator.async_fetch_hourly_consumption(
                    self._account,
                    range_start,
                    range_end,
                )
                if not fetched:
                    _LOGGER.debug(
                        "%s: fetched 0 measurements for range %s..%s",
                        prefix,
                        fetch_start_day,
                        today_utc,
                    )
                else:
                    additional_count += len(fetched)
                    for item in fetched:
                        start_at = item.get("startAt")
                        if not start_at:
                            skipped_additional_missing += 1
                            continue
                        start_utc = _parse_dt(start_at)
                        if start_utc is None:
                            skipped_additional_unparsed += 1
                            continue
                        if start_utc < keep_from_utc:
                            continue
                        measurements_by_start[start_utc] = item
            else:
                _LOGGER.debug(
                    "%s: no additional range to fetch (fetch_start_day=%s today=%s)",
                    prefix,
                    fetch_start_day,
                    today_utc,
                )

            total_measurements = len(measurements_by_start)
            _LOGGER.debug(
                "%s: consolidated measurements total=%s additional=%s fetched_days=%s seed_skipped_before=%s seed_skipped_unparsed=%s fetched_skipped_unparsed=%s fetched_skipped_missing=%s",
                prefix,
                total_measurements,
                additional_count,
                fetched_days,
                skipped_seed_before_window,
                skipped_seed_unparsed,
                skipped_additional_unparsed,
                skipped_additional_missing,
            )
            if not measurements_by_start:
                _LOGGER.debug(
                    "%s: no hourly consumption data available after consolidation",
                    prefix,
                )
                return

            # Diagnostic-only comparison to help identify discrepancies with official app totals.
            await self._async_compare_hourly_vs_daily(
                prefix=prefix,
                measurements_by_start=measurements_by_start,
                today_utc=today_utc,
            )

            metadata = {
                "mean_type": 0,
                "has_sum": True,
                "name": self._name,
                "source": DOMAIN,
                "statistic_id": self._statistic_id,
                "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                "unit_class": None,
            }
            _LOGGER.debug("%s: filled metadata statistics metadata=%s", prefix, metadata)

            await self._async_reconcile_current_month(
                prefix=prefix,
                metadata=metadata,
                today_utc=today_utc,
            )

            # Re-read tail statistics in case monthly reconcile inserted points.
            last_after_reconcile = await get_instance(self._hass).async_add_executor_job(
                get_last_statistics,
                self._hass,
                1,
                self._statistic_id,
                True,
                {STATISTIC_SUM},
            )
            last_points_after = last_after_reconcile.get(self._statistic_id) or []
            if last_points_after:
                last_point = last_points_after[-1]
                parsed_start = self._parse_stat_start(last_point.get("start"))
                if parsed_start is not None:
                    last_start = parsed_start
                raw_sum = last_point.get("sum")
                if raw_sum is None:
                    raw_sum = last_point.get("state")
                try:
                    last_sum = float(raw_sum or 0.0)
                except (TypeError, ValueError):
                    pass
                _LOGGER.debug(
                    "%s: tail statistics refreshed after reconcile start=%s sum=%s",
                    prefix,
                    last_start,
                    last_sum,
                )

            sorted_meas = sorted(measurements_by_start.items(), key=lambda item: item[0])
            _LOGGER.debug("%s: sorted measurements count=%s", prefix, len(sorted_meas))

            statistics = []
            running_sum = last_sum
            skipped_already_imported = 0
            skipped_invalid_value = 0

            for start_utc, m in sorted_meas:
                if last_start is not None and start_utc <= last_start:
                    skipped_already_imported += 1
                    continue

                val = self._parse_non_negative_kwh(
                    m.get("value"),
                    prefix=prefix,
                    label=f"import-hourly:{start_utc.isoformat()}",
                )
                if val is None:
                    skipped_invalid_value += 1
                    continue

                running_sum += val
                _LOGGER.debug(
                    "%s: prepared statistic start=%s value=%s running_sum=%s",
                    prefix,
                    start_utc,
                    val,
                    running_sum,
                )

                statistics.append({
                    "start": start_utc,
                    "state": running_sum,
                    "sum": running_sum,
                })

            _LOGGER.debug(
                "%s: post-filter counts prepared=%s skipped_already_imported=%s skipped_invalid_value=%s",
                prefix,
                len(statistics),
                skipped_already_imported,
                skipped_invalid_value,
            )

            if statistics:
                _LOGGER.debug(
                    "%s: adding external statistics metadata=%s statistics=%s",
                    prefix,
                    metadata,
                    statistics,
                )
                await self._async_add_statistics(metadata, statistics)
                _LOGGER.debug(
                    "%s: added %d statistics entries",
                    prefix,
                    len(statistics),
                )
            else:
                _LOGGER.debug("%s: no new statistics to add (running_sum=%s)", prefix, running_sum)

        except Exception as err:  # pylint: disable=broad-except
            _LOGGER.exception("%s: error importing consumption statistics: %s", prefix, err)
