import logging
from inspect import isawaitable
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
from homeassistant.core import HomeAssistant, callback, valid_entity_id
from homeassistant.helpers.event import async_track_point_in_utc_time
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util
from homeassistant.util import slugify

from homeassistant.components.recorder import DOMAIN as RECORDER_DOMAIN, get_instance
from homeassistant.components.recorder.statistics import (
    async_add_external_statistics,
    get_last_statistics,
)
try:
    from homeassistant.components.recorder.statistics import async_import_statistics
except ImportError:  # pragma: no cover - older Home Assistant versions
    async_import_statistics = None
try:
    from homeassistant.components.recorder.statistics import STATISTIC_SUM
except ImportError:  # pragma: no cover - fallback if constant missing
    STATISTIC_SUM = "sum"
try:
    from homeassistant.components.recorder.statistics import async_update_statistics_metadata
except ImportError:  # pragma: no cover - older Home Assistant versions
    async_update_statistics_metadata = None
from .const import CONSUMPTION_IMPORT_DELAY_DAYS, DOMAIN
from .coordinator import OctopusCoordinator
from .runtime import OctopusSpainConfigEntry

_LOGGER = logging.getLogger(__name__)

ENERGY_UNIT_CLASS = "energy"
PDF_URL_REFRESH_BUFFER = timedelta(minutes=5)


def _account_slug(account: str) -> str:
    """Return a stable slug for account-scoped entity IDs."""
    return slugify(account)


def _account_name(name: str, account: str) -> str:
    """Return a display name scoped to an Octopus account."""
    return f"{name} ({account})"


def _parse_invoice_pdf_expiry(invoice: Mapping[str, Any]) -> datetime | None:
    """Return the parsed PDF URL expiration timestamp in UTC."""
    raw_value = invoice.get("pdf_expires_at")
    if not raw_value:
        return None

    parsed = dt_util.parse_datetime(str(raw_value))
    if parsed is None:
        return None
    return dt_util.as_utc(parsed)


def _invoice_pdf_status(invoice: Mapping[str, Any]) -> tuple[datetime | None, bool]:
    """Return the PDF expiry and whether the current URL is expired."""
    expires_at = _parse_invoice_pdf_expiry(invoice)
    if expires_at is None:
        return None, False
    return expires_at, expires_at <= dt_util.utcnow()


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
        consumption_sensor = OctopusConsumptionStatisticsSensor(
            account, coordinator, single_account
        )
        sensors.append(consumption_sensor)

        # Individual Last Invoice fields
        name_prefix = _account_name("Factura", account)
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
        safe_account = _account_slug(account)
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = _account_name(name, account)
        self._attr_entity_id = f"sensor.octopus_{key}_{safe_account}"
        self._attr_unique_id = f"{key}_{safe_account}"
        self.entity_description = SensorEntityDescription(
            key=f"{key}_{safe_account}",
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


class _InvoiceRefreshMixin(CoordinatorEntity[OctopusCoordinator]):
    """Shared helpers for invoice entities with expiring PDF URLs."""

    _account: str
    _pdf_refresh_requested: bool
    _pdf_expiry_listener: Callable[[], None] | None

    def _cancel_pdf_expiry_listener(self) -> None:
        if self._pdf_expiry_listener is None:
            return
        self._pdf_expiry_listener()
        self._pdf_expiry_listener = None

    def _schedule_pdf_expiry_checkpoint(
        self, invoice: Mapping[str, Any], prefix: str
    ) -> None:
        pdf_url = invoice.get("pdf")
        expires_at = _parse_invoice_pdf_expiry(invoice)
        if not pdf_url or expires_at is None:
            self._cancel_pdf_expiry_listener()
            return

        now = dt_util.utcnow()
        refresh_at = expires_at - PDF_URL_REFRESH_BUFFER
        checkpoint_at: datetime | None = None
        if now < refresh_at:
            checkpoint_at = refresh_at
        elif now < expires_at:
            checkpoint_at = expires_at

        self._cancel_pdf_expiry_listener()
        if checkpoint_at is None:
            return

        @callback
        def _async_pdf_expiry_checkpoint(_: datetime) -> None:
            self._pdf_expiry_listener = None
            _LOGGER.debug(
                "%s: PDF URL checkpoint reached at %s",
                prefix,
                checkpoint_at.isoformat(),
            )
            self._handle_coordinator_update()

        self._pdf_expiry_listener = async_track_point_in_utc_time(
            self.hass,
            _async_pdf_expiry_checkpoint,
            checkpoint_at,
        )

    def _maybe_refresh_invoice_pdf(self, invoice: Mapping[str, Any], prefix: str) -> None:
        pdf_url = invoice.get("pdf")
        expires_at = _parse_invoice_pdf_expiry(invoice)
        if not pdf_url or expires_at is None:
            return
        if expires_at > dt_util.utcnow() + PDF_URL_REFRESH_BUFFER:
            self._pdf_refresh_requested = False
            return
        if self._pdf_refresh_requested:
            return

        self._pdf_refresh_requested = True
        _LOGGER.debug(
            "%s: PDF URL expires at %s, requesting an invoice refresh",
            prefix,
            expires_at.isoformat(),
        )
        self.hass.async_create_task(self._async_refresh_invoice_pdf())

    async def _async_refresh_invoice_pdf(self) -> None:
        try:
            await self.coordinator.async_refresh_account_invoice(self._account)
        finally:
            self._pdf_refresh_requested = False

    async def async_update(self) -> None:
        """Allow manual entity refresh to fetch a fresh signed PDF URL."""
        await self.coordinator.async_refresh_account_invoice(self._account)

    async def async_will_remove_from_hass(self) -> None:
        self._cancel_pdf_expiry_listener()
        await super().async_will_remove_from_hass()


class OctopusInvoice(_InvoiceRefreshMixin, SensorEntity):

    def __init__(self, account: str, coordinator: OctopusCoordinator, single: bool) -> None:
        super().__init__(coordinator=coordinator)
        self._state = None
        self._account = account
        self._pdf_refresh_requested = False
        self._pdf_expiry_listener = None
        safe_account = _account_slug(account)
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = _account_name("Última Factura Octopus", account)
        self._attr_entity_id = f"sensor.octopus_last_invoice_{safe_account}"
        self._attr_unique_id = f"last_invoice_{safe_account}"
        self.entity_description = SensorEntityDescription(
            key=f"last_invoice_{safe_account}",
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
                self._cancel_pdf_expiry_listener()
                self.async_write_ha_state()
                return

            inv = account_data.get('last_invoice')
            if not inv:
                _LOGGER.debug("%s: 'last_invoice' not present in coordinator data", prefix)
                self._state = None
                self._attrs = {}
                self._cancel_pdf_expiry_listener()
                self.async_write_ha_state()
                return

            self._schedule_pdf_expiry_checkpoint(inv, prefix)
            self._maybe_refresh_invoice_pdf(inv, prefix)
            pdf_expires_at, pdf_is_expired = _invoice_pdf_status(inv)

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
                'PDF caduca': pdf_expires_at.isoformat() if pdf_expires_at else None,
                'PDF expirada': pdf_is_expired,
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


class OctopusInvoiceFieldSensor(_InvoiceRefreshMixin, SensorEntity):
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
        self._pdf_refresh_requested = False
        self._pdf_expiry_listener = None
        self._field = field
        safe_account = _account_slug(account)
        safe_field = slugify(field)
        self._attrs: Mapping[str, Any] = {}
        self._attr_name = name
        self._attr_entity_id = f"sensor.octopus_last_invoice_{safe_field}_{safe_account}"
        self._attr_unique_id = f"last_invoice_{safe_field}_{safe_account}"
        desc_kwargs: dict[str, Any] = {
            "key": f"last_invoice_{safe_field}_{safe_account}",
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
                self._cancel_pdf_expiry_listener()
                self.async_write_ha_state()
                return

            inv = account_data.get("last_invoice") or {}
            if self._field == "pdf":
                self._schedule_pdf_expiry_checkpoint(inv, prefix)
                self._maybe_refresh_invoice_pdf(inv, prefix)
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
                    expires_at, is_expired = _invoice_pdf_status(inv)
                    self._attrs = {
                        "url": url,
                        "expires_at": expires_at.isoformat() if expires_at else None,
                        "is_expired": is_expired,
                    } if url else {}
                    # keep state short and indicative
                    self._state = "expired" if is_expired else "available" if url else None
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


class OctopusConsumptionStatisticsSensor(
    CoordinatorEntity[OctopusCoordinator], SensorEntity
):
    """Expose the imported cumulative consumption statistic as an energy sensor."""

    def __init__(
        self,
        account: str,
        coordinator: OctopusCoordinator,
        single: bool,
    ) -> None:
        super().__init__(coordinator=coordinator)
        self._state: StateType = None
        self._account = account
        self._single = single
        self._attrs: Mapping[str, Any] = {}
        self._importer: OctopusConsumptionStatisticsImporter | None = None
        safe_account = _account_slug(account)
        self._attr_name = _account_name("Consumo Electrico", account)
        self._attr_entity_id = f"sensor.consumo_electrico_{safe_account}"
        self._attr_unique_id = f"energy_consumption_{safe_account}"
        self._statistic_id = self._attr_entity_id
        # This entity mirrors a delayed, recorder-backed cumulative total.
        # Do not opt into automatic recorder statistics here, or Home Assistant
        # will synthesize additional "live" statistics from the mirrored state
        # and pollute the imported history with current-day rows.
        self.entity_description = SensorEntityDescription(
            key=f"energy_consumption_{safe_account}",
            icon="mdi:transmission-tower-import",
            device_class=SensorDeviceClass.ENERGY,
            native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        )

    async def async_added_to_hass(self) -> None:
        """Start importing statistics once Home Assistant has assigned entity_id."""
        await super().async_added_to_hass()
        self._statistic_id = self.entity_id
        self._importer = OctopusConsumptionStatisticsImporter(
            hass=self.hass,
            coordinator=self.coordinator,
            account=self._account,
            single=self._single,
            statistic_id=self._statistic_id,
            state_callback=self.async_set_native_value,
        )
        self.async_on_remove(self._importer.close)
        await self._importer.async_setup()

    @callback
    def async_set_native_value(
        self,
        value: float | None,
        attrs: Mapping[str, Any] | None = None,
    ) -> None:
        """Update the sensor from the imported recorder statistic total."""
        self._state = value
        if attrs is not None:
            self._attrs = attrs
        if getattr(self, "_hass", None) is not None:
            self.async_write_ha_state()

    @property
    def native_value(self) -> StateType:
        return self._state

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        return self._attrs

    @property
    def statistic_id(self) -> str:
        """Return the statistic id used by the Energy Dashboard for this sensor."""
        return self._statistic_id


class OctopusConsumptionStatisticsImporter:
    """Process coordinator data to feed historical consumption into statistics."""

    def __init__(
        self,
        hass: HomeAssistant,
        coordinator: OctopusCoordinator,
        account: str,
        single: bool,
        statistic_id: str,
        state_callback: Callable[[float | None, Mapping[str, Any] | None], None],
    ) -> None:
        self._hass = hass
        self._coordinator = coordinator
        self._account = account
        self._single = single
        self._state_callback = state_callback
        self._statistic_id = statistic_id
        self._name = _account_name("Consumo Electrico", account)
        self._remove_listener: Callable[[], None] | None = None
        self._metadata_updated = False
        self._reconcile_warning_fingerprint_by_day: dict[date, tuple[int, float, float]] = {}
        self._current_month_mismatch_fingerprint: tuple[int, float] | None = None
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

    async def _async_update_statistics_metadata(self) -> None:
        """Ensure the active recorder metadata is classified as energy."""
        if self._metadata_updated:
            return
        if async_update_statistics_metadata is None:
            self._metadata_updated = True
            return
        try:
            async_update_statistics_metadata(
                self._hass,
                self._statistic_id,
                new_unit_class=ENERGY_UNIT_CLASS,
                new_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
            )
        except TypeError:
            try:
                async_update_statistics_metadata(
                    self._hass,
                    self._statistic_id,
                    new_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                )
            except Exception as err:  # pragma: no cover - best-effort metadata repair
                _LOGGER.debug(
                    "%s: unable to update statistic metadata: %s",
                    self._statistic_id,
                    err,
                )
        except Exception as err:  # pragma: no cover - best-effort metadata repair
            _LOGGER.debug(
                "%s: unable to update statistic metadata: %s",
                self._statistic_id,
                err,
            )
        self._metadata_updated = True

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

    @staticmethod
    def _local_day_start_utc(day: date) -> datetime:
        timezone = dt_util.DEFAULT_TIME_ZONE or dt_util.UTC
        return dt_util.as_utc(datetime.combine(day, time.min, tzinfo=timezone))

    @staticmethod
    def _local_date(value: datetime) -> date:
        return dt_util.as_local(value).date()

    @staticmethod
    def _local_hour(value: datetime) -> int:
        return dt_util.as_local(value).hour

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
        add_statistics = (
            async_import_statistics
            if valid_entity_id(metadata["statistic_id"])
            else async_add_external_statistics
        )
        if add_statistics is None:
            _LOGGER.warning(
                "%s: this Home Assistant version cannot import entity statistics",
                self._statistic_id,
            )
            return
        result = add_statistics(self._hass, metadata, statistics)
        if isawaitable(result):
            await result

    async def _async_reconcile_current_month(
        self,
        *,
        prefix: str,
        metadata: dict[str, Any],
        today_local: date,
    ) -> None:
        month_start_day = today_local.replace(day=1)
        complete_until = today_local - timedelta(days=1)
        if complete_until < month_start_day:
            return

        range_start = self._local_day_start_utc(month_start_day)
        range_end = self._local_day_start_utc(complete_until + timedelta(days=1))
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
            day = self._local_date(dt_util.as_utc(parsed_start))
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
            day_start = self._local_day_start_utc(day)
            day_end = self._local_day_start_utc(day + timedelta(days=1))

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
        day_start = self._local_day_start_utc(day)
        day_end = self._local_day_start_utc(day + timedelta(days=1))
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

        present_hours = {self._local_hour(dt) for dt in hourly_values}
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
        import_end_utc: datetime,
    ) -> None:
        """Compare hourly-summed totals with API daily totals for diagnostics."""
        if not measurements_by_start:
            return

        # We diagnose a recent complete window to avoid noisy partial-day mismatches.
        complete_until = self._local_date(import_end_utc - timedelta(hours=1))
        compare_days = 7
        compare_start_day = complete_until - timedelta(days=compare_days - 1)
        if compare_start_day > complete_until:
            return

        hourly_by_day: dict[date, float] = {}
        hours_seen_by_day: dict[date, set[int]] = {}
        for start_utc, item in measurements_by_start.items():
            day = self._local_date(start_utc)
            if day < compare_start_day or day > complete_until:
                continue
            raw_value = item.get("value") if isinstance(item, Mapping) else item
            val = self._parse_non_negative_kwh(
                raw_value,
                prefix=prefix,
                label=f"seed-hourly:{start_utc.isoformat()}",
            )
            if val is None:
                continue
            hourly_by_day[day] = hourly_by_day.get(day, 0.0) + val
            hours_seen_by_day.setdefault(day, set()).add(self._local_hour(start_utc))

        if not hourly_by_day:
            return

        range_start = self._local_day_start_utc(compare_start_day)
        range_end = self._local_day_start_utc(complete_until + timedelta(days=1))
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
            day = self._local_date(start_at)
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

    @staticmethod
    def _parse_api_start(value: Any) -> datetime | None:
        if not isinstance(value, str):
            return None
        parsed = dt_util.parse_datetime(value)
        if parsed is None:
            return None
        return dt_util.as_utc(parsed)

    @staticmethod
    def _month_import_window(now_utc: datetime) -> tuple[datetime, datetime]:
        """Return the delayed Home Assistant-local current month window in UTC."""
        now_local = dt_util.as_local(now_utc)
        month_start_local = now_local.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0
        )
        delayed_end_local = (now_local - timedelta(days=CONSUMPTION_IMPORT_DELAY_DAYS)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        if delayed_end_local < month_start_local:
            delayed_end_local = month_start_local
        return dt_util.as_utc(month_start_local), dt_util.as_utc(delayed_end_local)

    def _local_day_hour_starts(self, day: date) -> list[datetime]:
        """Return expected hourly interval starts for a local day in UTC."""
        day_start = self._local_day_start_utc(day)
        day_end = self._local_day_start_utc(day + timedelta(days=1))
        expected_hours = int((day_end - day_start).total_seconds() // 3600)
        return [day_start + timedelta(hours=hour) for hour in range(expected_hours)]

    def _truncate_incomplete_days(
        self,
        *,
        prefix: str,
        measurements_by_start: dict[datetime, float],
    ) -> tuple[dict[datetime, float], date | None]:
        """Skip the first incomplete local day and every day after it."""
        if not measurements_by_start:
            return measurements_by_start, None

        days = sorted({self._local_date(start_utc) for start_utc in measurements_by_start})
        for day in days:
            expected_starts = self._local_day_hour_starts(day)
            missing_starts = [
                start_utc for start_utc in expected_starts if start_utc not in measurements_by_start
            ]
            if not missing_starts:
                continue

            day_start = self._local_day_start_utc(day)
            kept_measurements = {
                start_utc: value
                for start_utc, value in measurements_by_start.items()
                if start_utc < day_start
            }
            missing_hours = [dt_util.as_local(start_utc).hour for start_utc in missing_starts]
            _LOGGER.warning(
                "%s: incomplete hourly data detected on %s (hours_seen=%s/%s, missing_hours=%s); skipping that day and all following days",
                prefix,
                day.isoformat(),
                len(expected_starts) - len(missing_starts),
                len(expected_starts),
                missing_hours,
            )
            return kept_measurements, day

        return measurements_by_start, None

    @staticmethod
    def _parse_stat_sum(point: Mapping[str, Any]) -> float | None:
        raw_sum = point.get("sum")
        if raw_sum is None:
            raw_sum = point.get("state")
        try:
            return float(raw_sum)
        except (TypeError, ValueError):
            return None

    async def _async_get_stat_points(
        self,
        *,
        hours_to_fetch: int,
    ) -> list[tuple[datetime, float]]:
        existing = await get_instance(self._hass).async_add_executor_job(
            get_last_statistics,
            self._hass,
            hours_to_fetch,
            self._statistic_id,
            True,
            {STATISTIC_SUM},
        )
        points: list[tuple[datetime, float]] = []
        for point in existing.get(self._statistic_id, []):
            parsed_start = self._parse_stat_start(point.get("start"))
            parsed_sum = self._parse_stat_sum(point)
            if parsed_start is None or parsed_sum is None:
                continue
            points.append((parsed_start, parsed_sum))
        points.sort(key=lambda item: item[0])
        return points

    async def _async_add_month_baseline_statistic(
        self,
        *,
        metadata: dict[str, Any],
        import_start_utc: datetime,
        baseline_sum: float,
    ) -> None:
        """Create statistics metadata even before delayed consumption is available."""
        await self._async_add_statistics(
            metadata,
            [{
                "start": import_start_utc,
                "state": baseline_sum,
                "sum": baseline_sum,
            }],
        )

    async def _async_fill_confirmed_zero_hours(
        self,
        *,
        prefix: str,
        measurements_by_start: dict[datetime, float],
        import_start_utc: datetime,
        today_local: date,
    ) -> int:
        """Fill omitted zero-consumption hours only when daily totals confirm it."""
        if not measurements_by_start:
            return 0

        complete_until = today_local - timedelta(days=1)
        range_start_day = self._local_date(import_start_utc)
        if complete_until < range_start_day:
            return 0

        range_start = self._local_day_start_utc(range_start_day)
        range_end = self._local_day_start_utc(complete_until + timedelta(days=1))
        daily_rows = await self._coordinator.async_fetch_daily_consumption(
            self._account,
            range_start,
            range_end,
        )

        daily_by_day: dict[date, float] = {}
        for row in daily_rows:
            start_utc = self._parse_api_start(row.get("startAt"))
            if start_utc is None:
                continue
            day = self._local_date(start_utc)
            if day < range_start_day or day > complete_until:
                continue
            daily_value = self._parse_non_negative_kwh(
                row.get("value"),
                prefix=prefix,
                label=f"zero-fill-daily:{day.isoformat()}",
            )
            if daily_value is None:
                continue
            daily_by_day[day] = daily_value

        if not daily_by_day:
            return 0

        tolerance_kwh = 0.05
        filled = 0
        for day, daily_total in sorted(daily_by_day.items()):
            day_start = self._local_day_start_utc(day)
            slots = [day_start + timedelta(hours=hour) for hour in range(24)]
            eligible_slots = [
                slot for slot in slots if slot >= import_start_utc and slot in measurements_by_start
            ]
            if eligible_slots:
                hourly_total = sum(measurements_by_start[slot] for slot in eligible_slots)
                present_hours = {self._local_hour(slot) for slot in eligible_slots}
                missing_hours = sorted(set(range(24)) - present_hours)
            elif abs(daily_total) <= tolerance_kwh:
                hourly_total = 0.0
                missing_hours = list(range(24))
            else:
                continue

            if not missing_hours or abs(hourly_total - daily_total) > tolerance_kwh:
                continue

            filled_for_day = 0
            for hour in missing_hours:
                slot = day_start + timedelta(hours=hour)
                if slot < import_start_utc:
                    continue
                measurements_by_start[slot] = 0.0
                filled_for_day += 1

            if filled_for_day:
                filled += filled_for_day
                _LOGGER.debug(
                    "%s: filled %s zero-consumption hour(s) for %s because daily total matches hourly rows",
                    prefix,
                    filled_for_day,
                    day.isoformat(),
                )

        return filled

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

            await self._async_update_statistics_metadata()

            now_utc = dt_util.utcnow()
            import_start_utc, import_end_utc = self._month_import_window(now_utc)
            stats_window_hours = max(
                1,
                int((import_end_utc - import_start_utc).total_seconds() // 3600) + 96,
            )

            existing_points = await self._async_get_stat_points(
                hours_to_fetch=stats_window_hours,
            )
            baseline_sum = 0.0
            baseline_start: datetime | None = None
            last_start: datetime | None = None
            last_sum = 0.0
            existing_month_points = 0
            existing_month_values_by_start: dict[datetime, float] = {}
            existing_month_sums_by_start: dict[datetime, float] = {}
            previous_sum = 0.0
            for point_start, point_sum in existing_points:
                last_start = point_start
                last_sum = point_sum
                if point_start < import_start_utc:
                    baseline_start = point_start
                    baseline_sum = point_sum
                    previous_sum = point_sum
                else:
                    existing_month_points += 1
                    if point_start < import_end_utc:
                        existing_month_sums_by_start[point_start] = point_sum
                        existing_value = point_sum - previous_sum
                        if existing_value >= 0:
                            existing_month_values_by_start[point_start] = existing_value
                    previous_sum = point_sum

            if last_start is not None:
                _LOGGER.debug(
                    "%s: last statistics point start=%s last_sum=%s baseline_start=%s baseline_sum=%s existing_month_points=%s",
                    prefix,
                    last_start,
                    last_sum,
                    baseline_start,
                    baseline_sum,
                    existing_month_points,
                )
            else:
                _LOGGER.debug("%s: no existing statistics found, starting fresh", prefix)

            base_attrs: dict[str, Any] = {
                "statistic_id": self._statistic_id,
                "current_month_start": dt_util.as_local(import_start_utc).isoformat(),
                "current_month_start_utc": import_start_utc.isoformat(),
                "import_window_end_utc": import_end_utc.isoformat(),
                "import_delay_days": CONSUMPTION_IMPORT_DELAY_DAYS,
                "baseline_hour": baseline_start.isoformat() if baseline_start else None,
                "baseline_sum_kwh": round(baseline_sum, 6),
                "previous_last_imported_hour": last_start.isoformat() if last_start else None,
                "previous_last_sum_kwh": round(last_sum, 6) if last_start else None,
            }
            self._state_callback(last_sum if last_start is not None else None, base_attrs)

            metadata = {
                "has_mean": False,
                "mean_type": 0,
                "has_sum": True,
                "name": self._name,
                "source": RECORDER_DOMAIN if valid_entity_id(self._statistic_id) else DOMAIN,
                "statistic_id": self._statistic_id,
                "unit_of_measurement": UnitOfEnergy.KILO_WATT_HOUR,
                "unit_class": ENERGY_UNIT_CLASS,
            }
            _LOGGER.debug("%s: filled metadata statistics metadata=%s", prefix, metadata)

            fetched = await self._coordinator.async_fetch_hourly_consumption(
                self._account,
                import_start_utc,
                import_end_utc,
            )
            fetched_count = len(fetched) if isinstance(fetched, list) else 0
            if not fetched:
                baseline_imported = not existing_month_values_by_start
                if baseline_imported:
                    await self._async_add_month_baseline_statistic(
                        metadata=metadata,
                        import_start_utc=import_start_utc,
                        baseline_sum=baseline_sum,
                    )
                attrs = {
                    **base_attrs,
                    "last_update_success": True,
                    "last_update_message": "No current-month hourly rows returned by API yet",
                    "current_month_hourly_rows": 0,
                    "current_month_api_hourly_rows": 0,
                    "current_month_preserved_existing_hours": len(existing_month_values_by_start),
                    "current_month_baseline_imported": baseline_imported,
                    "current_month_zero_filled_hours": 0,
                    "current_month_imported_total_kwh": 0.0,
                    "api_data_through": None,
                    "hours_not_yet_available": max(
                        0,
                        int((import_end_utc - import_start_utc).total_seconds() // 3600),
                    ),
                }
                self._state_callback(baseline_sum, attrs)
                _LOGGER.debug(
                    "%s: current-month hourly pull returned 0 rows for %s..%s",
                    prefix,
                    import_start_utc,
                    import_end_utc,
                )
                return

            api_measurements_by_start: dict[datetime, float] = {}
            api_measurement_starts: set[datetime] = set()
            skipped_seed_unparsed = 0
            skipped_seed_before_window = 0
            if isinstance(measurements_raw, list):
                for item in measurements_raw:
                    start_at = item.get("startAt")
                    if not start_at:
                        continue
                    start_utc = self._parse_api_start(start_at)
                    if start_utc is None:
                        skipped_seed_unparsed += 1
                        continue
                    if start_utc < import_start_utc or start_utc >= import_end_utc:
                        skipped_seed_before_window += 1
                        continue
                    value = self._parse_non_negative_kwh(
                        item.get("value"),
                        prefix=prefix,
                        label=f"seed-hourly:{start_utc.isoformat()}",
                    )
                    if value is None:
                        continue
                    api_measurements_by_start[start_utc] = value
                    api_measurement_starts.add(start_utc)

            skipped_additional_unparsed = 0
            skipped_additional_missing = 0
            skipped_additional_invalid = 0
            for item in fetched:
                start_at = item.get("startAt")
                if not start_at:
                    skipped_additional_missing += 1
                    continue
                start_utc = self._parse_api_start(start_at)
                if start_utc is None:
                    skipped_additional_unparsed += 1
                    continue
                if start_utc < import_start_utc or start_utc >= import_end_utc:
                    continue
                value = self._parse_non_negative_kwh(
                    item.get("value"),
                    prefix=prefix,
                    label=f"import-hourly:{start_utc.isoformat()}",
                )
                if value is None:
                    skipped_additional_invalid += 1
                    continue
                api_measurements_by_start[start_utc] = value
                api_measurement_starts.add(start_utc)

            api_data_through = max(api_measurement_starts) if api_measurement_starts else None
            preserved_existing_values_by_start: dict[datetime, float] = {}
            if api_data_through is not None:
                for start_utc, value in existing_month_values_by_start.items():
                    if start_utc > api_data_through:
                        continue
                    if start_utc in api_measurements_by_start:
                        continue
                    preserved_existing_values_by_start[start_utc] = value

            api_measurements_by_start, truncated_from_day = self._truncate_incomplete_days(
                prefix=prefix,
                measurements_by_start=api_measurements_by_start,
            )
            if truncated_from_day is not None:
                preserved_existing_values_by_start = {
                    start_utc: value
                    for start_utc, value in preserved_existing_values_by_start.items()
                    if self._local_date(start_utc) < truncated_from_day
                }
                api_measurement_starts = {
                    start_utc
                    for start_utc in api_measurement_starts
                    if self._local_date(start_utc) < truncated_from_day
                }
                api_measurements_by_start = {
                    start_utc: value
                    for start_utc, value in api_measurements_by_start.items()
                    if self._local_date(start_utc) < truncated_from_day
                }

            measurements_by_start: dict[datetime, float] = {}
            measurements_by_start.update(preserved_existing_values_by_start)
            measurements_by_start.update(api_measurements_by_start)

            total_measurements = len(measurements_by_start)
            api_data_through = max(api_measurement_starts) if api_measurement_starts else None
            _LOGGER.debug(
                "%s: consolidated current-month measurements total=%s fetched=%s preserved_existing=%s api_data_through=%s seed_skipped_outside_window=%s seed_skipped_unparsed=%s fetched_skipped_unparsed=%s fetched_skipped_missing=%s fetched_skipped_invalid=%s window=%s..%s",
                prefix,
                total_measurements,
                fetched_count,
                len(preserved_existing_values_by_start),
                api_data_through.isoformat() if api_data_through else None,
                skipped_seed_before_window,
                skipped_seed_unparsed,
                skipped_additional_unparsed,
                skipped_additional_missing,
                skipped_additional_invalid,
                import_start_utc,
                import_end_utc,
            )
            if not measurements_by_start:
                baseline_imported = not preserved_existing_values_by_start
                if baseline_imported:
                    await self._async_add_month_baseline_statistic(
                        metadata=metadata,
                        import_start_utc=import_start_utc,
                        baseline_sum=baseline_sum,
                    )
                attrs = {
                    **base_attrs,
                    "last_update_success": True,
                    "last_update_message": (
                        f"Incomplete hourly data detected from {truncated_from_day.isoformat()}; "
                        "skipped that day and later"
                        if truncated_from_day is not None
                        else "Current-month API rows were returned but none were parseable"
                    ),
                    "current_month_hourly_rows": 0,
                    "current_month_api_hourly_rows": 0,
                    "current_month_preserved_existing_hours": len(preserved_existing_values_by_start),
                    "current_month_baseline_imported": baseline_imported,
                    "current_month_zero_filled_hours": 0,
                    "current_month_imported_total_kwh": 0.0,
                    "api_data_through": None,
                    "truncated_from_day": truncated_from_day.isoformat() if truncated_from_day else None,
                    "hours_not_yet_available": max(
                        0,
                        int((import_end_utc - import_start_utc).total_seconds() // 3600),
                    ),
                }
                self._state_callback(baseline_sum, attrs)
                _LOGGER.debug(
                    "%s: no hourly consumption data available after consolidation",
                    prefix,
                )
                return

            zero_filled_hours = 0

            # Diagnostic-only comparison to help identify discrepancies with official app totals.
            await self._async_compare_hourly_vs_daily(
                prefix=prefix,
                measurements_by_start=measurements_by_start,
                import_end_utc=import_end_utc,
            )

            sorted_meas = sorted(measurements_by_start.items(), key=lambda item: item[0])
            _LOGGER.debug("%s: sorted measurements count=%s", prefix, len(sorted_meas))

            statistics = []
            running_sum = baseline_sum
            imported_month_total = 0.0
            reused_existing_points = 0
            mismatched_existing_points = 0
            max_existing_delta = 0.0
            sum_tolerance_kwh = 0.001

            for start_utc, val in sorted_meas:
                running_sum += val
                imported_month_total += val
                _LOGGER.debug(
                    "%s: prepared statistic start=%s value=%s running_sum=%s",
                    prefix,
                    start_utc,
                    val,
                    running_sum,
                )

                existing_sum = existing_month_sums_by_start.get(start_utc)
                if existing_sum is not None:
                    reused_existing_points += 1
                    point_delta = abs(existing_sum - running_sum)
                    if point_delta > sum_tolerance_kwh:
                        mismatched_existing_points += 1
                        if point_delta > max_existing_delta:
                            max_existing_delta = point_delta
                    continue

                statistics.append({
                    "start": start_utc,
                    "state": running_sum,
                    "sum": running_sum,
                })

            _LOGGER.debug(
                "%s: prepared current-month statistics count=%s imported_month_total=%.6f baseline_sum=%.6f final_sum=%.6f",
                prefix,
                len(statistics),
                imported_month_total,
                baseline_sum,
                running_sum,
            )
            if reused_existing_points:
                _LOGGER.debug(
                    "%s: skipped %s recorder statistic point(s) that already exist for the current month",
                    prefix,
                    reused_existing_points,
                )
            if mismatched_existing_points:
                fingerprint = (
                    mismatched_existing_points,
                    round(max_existing_delta, 3),
                )
                if self._current_month_mismatch_fingerprint != fingerprint:
                    self._current_month_mismatch_fingerprint = fingerprint
                    _LOGGER.warning(
                        "%s: reconstructed current-month totals differ from %s existing recorder point(s) (max_delta=%.3f kWh). Existing points are left untouched to avoid duplicate accumulation.",
                        prefix,
                        mismatched_existing_points,
                        max_existing_delta,
                    )
                else:
                    _LOGGER.debug(
                        "%s: current-month mismatch fingerprint unchanged (%s point(s), max_delta=%.3f kWh)",
                        prefix,
                        mismatched_existing_points,
                        max_existing_delta,
                    )

            last_imported_hour = sorted_meas[-1][0] if sorted_meas else None
            if api_data_through is None:
                hours_not_yet_available = max(
                    0,
                    int((import_end_utc - import_start_utc).total_seconds() // 3600),
                )
            else:
                hours_not_yet_available = max(
                    0,
                    int(
                        (
                            import_end_utc
                            - (api_data_through + timedelta(hours=1))
                        ).total_seconds()
                        // 3600
                    ),
                )

            attrs = {
                **base_attrs,
                "last_update_success": True,
                "last_update_message": (
                    f"Current month statistics synchronized; truncated from {truncated_from_day.isoformat()}"
                    if truncated_from_day is not None
                    else "Current month statistics synchronized"
                ),
                "current_month_hourly_rows": len(sorted_meas),
                "current_month_api_hourly_rows": len(api_measurement_starts),
                "current_month_new_statistics_rows": len(statistics),
                "current_month_existing_statistics_rows": reused_existing_points,
                "current_month_preserved_existing_hours": len(preserved_existing_values_by_start),
                "current_month_baseline_imported": False,
                "current_month_zero_filled_hours": zero_filled_hours,
                "current_month_imported_total_kwh": round(imported_month_total, 6),
                "api_data_through": api_data_through.isoformat() if api_data_through else None,
                "truncated_from_day": truncated_from_day.isoformat() if truncated_from_day else None,
                "hours_not_yet_available": hours_not_yet_available,
                "last_imported_hour": last_imported_hour.isoformat() if last_imported_hour else None,
                "last_imported_sum_kwh": round(running_sum, 6),
            }

            if statistics:
                _LOGGER.debug(
                    "%s: importing current-month statistics metadata=%s statistics=%s",
                    prefix,
                    metadata,
                    statistics,
                )
                await self._async_add_statistics(metadata, statistics)
                self._state_callback(running_sum, attrs)
                _LOGGER.debug(
                    "%s: imported %d current-month statistics entries",
                    prefix,
                    len(statistics),
                )
            else:
                self._state_callback(running_sum, attrs)
                _LOGGER.debug("%s: no new statistics to add (running_sum=%s)", prefix, running_sum)

        except Exception as err:  # pylint: disable=broad-except
            _LOGGER.exception("%s: error importing consumption statistics: %s", prefix, err)
