"""Config flow for Tuya Decoder Manager."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .const import (
    CONF_CURRENT_CORRECTION,
    CONF_POWER_CORRECTION,
    CONF_SOURCE_SENSOR,
    CONF_VOLTAGE_CORRECTION,
    DEFAULT_CURRENT_CORRECTION,
    DEFAULT_NAME,
    DEFAULT_POWER_CORRECTION,
    DEFAULT_VOLTAGE_CORRECTION,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

class TuyaDecoderManagerFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Tuya Decoder Manager."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        _LOGGER.debug("Starting config flow for Tuya Decoder Manager")
        
        errors = {}
        
        if user_input is not None:
            # Validation
            source_sensor = user_input[CONF_SOURCE_SENSOR]
            
            # Check if source sensor exists
            if source_sensor not in self.hass.states.async_entity_ids("sensor"):
                errors[CONF_SOURCE_SENSOR] = "entity_not_found"
            else:
                # All validations passed, create entry
                title = user_input.get(CONF_NAME, DEFAULT_NAME)
                return self.async_create_entry(title=title, data=user_input)
        
        # Show configuration form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=DEFAULT_NAME): str,
                    vol.Required(CONF_SOURCE_SENSOR): EntitySelector(
                        EntitySelectorConfig(domain="sensor")
                    ),
                    vol.Optional(
                        CONF_VOLTAGE_CORRECTION, default=DEFAULT_VOLTAGE_CORRECTION
                    ): vol.Coerce(float),
                    vol.Optional(
                        CONF_CURRENT_CORRECTION, default=DEFAULT_CURRENT_CORRECTION
                    ): vol.Coerce(float),
                    vol.Optional(
                        CONF_POWER_CORRECTION, default=DEFAULT_POWER_CORRECTION
                    ): vol.Coerce(float),
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Create the options flow."""
        return TuyaDecoderManagerOptionsFlowHandler(config_entry)

class TuyaDecoderManagerOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Tuya Decoder Manager."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        super().__init__()
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Manage the options."""
        if user_input is not None:
            # Aggiorna il titolo dell'entry con il nuovo nome
            updated_data = self.config_entry.data.copy()
            updated_data.update(user_input)
            
            # Rimuovi il nome dai dati poiché viene gestito separatamente
            data_without_name = updated_data.copy()
            if CONF_NAME in data_without_name:
                data_without_name.pop(CONF_NAME)
            
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                title=user_input.get(CONF_NAME, self.config_entry.title),
                data=data_without_name,
            )
            return self.async_create_entry(title="", data={})
            
        # Get current values
        name = self.config_entry.title
        source_sensor = self.config_entry.data.get(CONF_SOURCE_SENSOR)
        voltage_correction = self.config_entry.data.get(
            CONF_VOLTAGE_CORRECTION, DEFAULT_VOLTAGE_CORRECTION
        )
        power_correction = self.config_entry.data.get(
            CONF_POWER_CORRECTION, DEFAULT_POWER_CORRECTION
        )
        current_correction = self.config_entry.data.get(
            CONF_CURRENT_CORRECTION, DEFAULT_CURRENT_CORRECTION
        )
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=name): str,
                    vol.Required(CONF_SOURCE_SENSOR, default=source_sensor): EntitySelector(
                        EntitySelectorConfig(domain="sensor")
                    ),
                    vol.Optional(
                        CONF_VOLTAGE_CORRECTION, default=voltage_correction
                    ): vol.Coerce(float),
                    vol.Optional(
                        CONF_CURRENT_CORRECTION, default=current_correction
                    ): vol.Coerce(float),
                    vol.Optional(
                        CONF_POWER_CORRECTION, default=power_correction
                    ): vol.Coerce(float),
                }
            ),
        )
