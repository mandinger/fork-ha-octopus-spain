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

                try:
                    val = float(Decimal(m["value"]))
                except (InvalidOperation, ValueError, TypeError):
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
                if iscoroutinefunction(async_add_external_statistics):
                    await async_add_external_statistics(self._hass, metadata, statistics)
                else:
                    await self._hass.async_add_executor_job(
                        async_add_external_statistics, self._hass, metadata, statistics
                    )
                _LOGGER.debug(
                    "%s: added %d statistics entries",
                    prefix,
                    len(statistics),
                )
            else:
                _LOGGER.debug("%s: no new statistics to add (running_sum=%s)", prefix, running_sum)

        except Exception as err:  # pylint: disable=broad-except
            _LOGGER.exception("%s: error importing consumption statistics: %s", prefix, err)