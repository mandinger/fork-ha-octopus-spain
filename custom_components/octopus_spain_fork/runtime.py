from __future__ import annotations

from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry

from .coordinator import OctopusCoordinator


@dataclass(slots=True)
class OctopusSpainRuntimeData:
    """Runtime data stored on the config entry."""

    coordinator: OctopusCoordinator


OctopusSpainConfigEntry = ConfigEntry[OctopusSpainRuntimeData]
