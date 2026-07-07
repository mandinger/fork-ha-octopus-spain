"""Balance Neto"""
from __future__ import annotations

import importlib
import logging

import voluptuous as vol

from homeassistant.const import Platform
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import config_validation as cv

from .const import (
    ATTR_ACCOUNT,
    CONF_APIKEY,
    CONF_EMAIL,
    CONF_PASSWORD,
    DOMAIN,
    SERVICE_DOWNLOAD_INVOICE,
)
from .coordinator import OctopusCoordinator
from .runtime import OctopusSpainRuntimeData, OctopusSpainConfigEntry

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

SERVICE_DOWNLOAD_INVOICE_SCHEMA = vol.Schema(
    {vol.Optional(ATTR_ACCOUNT): cv.string}
)


def _async_register_services(hass: HomeAssistant) -> None:
    if hass.services.has_service(DOMAIN, SERVICE_DOWNLOAD_INVOICE):
        return

    async def _handle_download_invoice(call: ServiceCall) -> None:
        requested = call.data.get(ATTR_ACCOUNT)
        matched = False
        for config_entry in hass.config_entries.async_loaded_entries(DOMAIN):
            coordinator = config_entry.runtime_data.coordinator
            for account in list(coordinator.data or {}):
                if requested and account != requested:
                    continue
                matched = True
                await coordinator.async_download_invoice(account)
        if not matched:
            _LOGGER.warning(
                "download_invoice: no account matched %s",
                requested or "<any>",
            )

    hass.services.async_register(
        DOMAIN,
        SERVICE_DOWNLOAD_INVOICE,
        _handle_download_invoice,
        schema=SERVICE_DOWNLOAD_INVOICE_SCHEMA,
    )


async def async_setup_entry(hass: HomeAssistant, entry: OctopusSpainConfigEntry) -> bool:
    entry_data = {**entry.data, **dict(entry.options)}
    coordinator = OctopusCoordinator(
        hass,
        email=entry_data.get(CONF_EMAIL),
        password=entry_data.get(CONF_PASSWORD),
        api_key=entry_data.get(CONF_APIKEY),
    )
    entry.runtime_data = OctopusSpainRuntimeData(coordinator=coordinator)

    # Ensure config/www/octopus_spain_fork exists: HA only serves /local/ when
    # config/www existed at startup, so create it as early as possible.
    await hass.async_add_executor_job(coordinator.pdf_manager.ensure_base_dir)

    await hass.async_add_executor_job(importlib.import_module, f"{__name__}.sensor")
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    _async_register_services(hass)

    entry.async_on_unload(entry.add_update_listener(_async_update_options))
    return True


async def async_unload_entry(
    hass: HomeAssistant, config_entry: OctopusSpainConfigEntry
) -> bool:
    """Unload a config entry."""
    unloaded = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unloaded:
        remaining = [
            entry
            for entry in hass.config_entries.async_loaded_entries(DOMAIN)
            if entry.entry_id != config_entry.entry_id
        ]
        if not remaining:
            hass.services.async_remove(DOMAIN, SERVICE_DOWNLOAD_INVOICE)
    return unloaded


async def _async_update_options(
    hass: HomeAssistant, config_entry: OctopusSpainConfigEntry
) -> None:
    """Handle options update."""
    # update entry replacing data with new options
    hass.config_entries.async_update_entry(
        config_entry, data={**config_entry.data, **config_entry.options}
    )
    await hass.config_entries.async_reload(config_entry.entry_id)
