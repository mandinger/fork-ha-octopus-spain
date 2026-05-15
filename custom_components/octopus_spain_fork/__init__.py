"""Balance Neto"""
from __future__ import annotations

import importlib

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import CONF_APIKEY, CONF_EMAIL, CONF_PASSWORD
from .coordinator import OctopusCoordinator
from .runtime import OctopusSpainRuntimeData, OctopusSpainConfigEntry

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: OctopusSpainConfigEntry) -> bool:
    entry_data = {**entry.data, **dict(entry.options)}
    coordinator = OctopusCoordinator(
        hass,
        email=entry_data.get(CONF_EMAIL),
        password=entry_data.get(CONF_PASSWORD),
        api_key=entry_data.get(CONF_APIKEY),
    )
    entry.runtime_data = OctopusSpainRuntimeData(coordinator=coordinator)

    await hass.async_add_executor_job(importlib.import_module, f"{__name__}.sensor")
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(_async_update_options))
    return True


async def async_unload_entry(
    hass: HomeAssistant, config_entry: OctopusSpainConfigEntry
) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)


async def _async_update_options(
    hass: HomeAssistant, config_entry: OctopusSpainConfigEntry
) -> None:
    """Handle options update."""
    # update entry replacing data with new options
    hass.config_entries.async_update_entry(
        config_entry, data={**config_entry.data, **config_entry.options}
    )
    await hass.config_entries.async_reload(config_entry.entry_id)
