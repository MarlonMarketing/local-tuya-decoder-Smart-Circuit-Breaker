"""Sensor platform for Tuya Decoder Manager."""
from __future__ import annotations

import base64
import logging
from typing import Any
from datetime import timedelta

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    UnitOfPower,
)
from homeassistant.const import UnitOfElectricCurrent, UnitOfElectricPotential
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from .const import (
    ATTR_SOURCE_SENSOR,
    CONF_CURRENT_CORRECTION,
    CONF_POWER_CORRECTION,
    CONF_SOURCE_SENSOR,
    CONF_VOLTAGE_CORRECTION,
    DEFAULT_CURRENT_CORRECTION,
    DEFAULT_POWER_CORRECTION,
    DEFAULT_VOLTAGE_CORRECTION,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    source_sensor = config_entry.data[CONF_SOURCE_SENSOR]
    
    entities = []
    entities.append(TuyaVoltageSensor(source_sensor, config_entry))
    entities.append(TuyaCurrentSensor(source_sensor, config_entry))
    entities.append(TuyaPowerSensor(source_sensor, config_entry))
    
    async_add_entities(entities)

class TuyaBaseSensor(RestoreEntity, SensorEntity):
    """Base class for Tuya sensors."""
    
    def __init__(
        self,
        source_entity: str,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the base sensor."""
        self._source_entity = source_entity
        self._config_entry = config_entry
        self._state = None
        self._available = True
        self._attributes: dict[str, Any] = {
            ATTR_SOURCE_SENSOR: source_entity,
        }
        self._remove_listener = None
        
    async def async_added_to_hass(self) -> None:
        """Register callbacks when entity is added to hass."""
        await super().async_added_to_hass()
        
        # Restore previous state if available
        last_state = await self.async_get_last_state()
        if last_state is not None:
            self._state = last_state.state
            self._available = last_state.state != "unavailable"
            self._attributes.update(last_state.attributes)
        
        # Register listener for source entity state changes
        self._remove_listener = self.hass.bus.async_listen(
            "state_changed", self._handle_source_state_change
        )
        
    async def async_will_remove_from_hass(self) -> None:
        """Clean up when entity is removed from hass."""
        if self._remove_listener:
            self._remove_listener()
            self._remove_listener = None
            
    async def _handle_source_state_change(self, event) -> None:
        """Handle state changes of the source entity."""
        if event.data.get("entity_id") == self._source_entity:
            _LOGGER.debug("Source entity %s changed, updating sensor", self._source_entity)
            await self.async_update()
            self.async_write_ha_state()
        
    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self._config_entry.entry_id}_{self.name.lower().replace(' ', '_')}"
        
    @property
    def device_info(self) -> dict[str, Any]:
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, self._config_entry.entry_id)},
            "name": self._config_entry.title,
            "manufacturer": "Tuya",
            "model": "Breaker Decoder",
        }
        
    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return the state attributes."""
        return self._attributes

class TuyaVoltageSensor(TuyaBaseSensor):
    """Representation of a Tuya Voltage sensor."""
    
    def __init__(
        self,
        source_entity: str,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the voltage sensor."""
        super().__init__(source_entity, config_entry)
        self._attr_translation_key = "voltage"
        self._attr_native_unit_of_measurement = UnitOfElectricPotential.VOLT
        self._attr_icon = "mdi:flash"
        
    @property
    def name(self) -> str | None:
        """Return the name of the sensor."""
        return f"{self._config_entry.title} {self._attr_translation_key}"
        
    @property
    def _voltage_correction(self) -> float:
        """Return the voltage correction from config."""
        return self._config_entry.data.get(CONF_VOLTAGE_CORRECTION, DEFAULT_VOLTAGE_CORRECTION)
    
    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        try:
            _LOGGER.debug("Updating voltage sensor for source entity: %s", self._source_entity)
            source_state = self.hass.states.get(self._source_entity)
            if source_state is None:
                _LOGGER.warning("Source entity %s not found", self._source_entity)
                self._available = False
                return
                
            _LOGGER.debug("Source entity state: %s", source_state)
            _LOGGER.debug("Source entity attributes: %s", source_state.attributes)
                
            if source_state.state == "unavailable":
                self._available = False
                return
                
            # Decode base64 data
            base64_data = source_state.state
            _LOGGER.debug("Base64 data: %s", base64_data)
            if not base64_data:
                self._available = False
                return
                
            try:
                # Decode base64 string to bytes
                decoded_bytes = base64.b64decode(base64_data)
                _LOGGER.debug("Decoded bytes: %s", decoded_bytes)
                
                # Extract voltage from first two bytes (big-endian) and divide by 10
                voltage_raw = int.from_bytes(decoded_bytes[0:2], byteorder='big')
                voltage = voltage_raw / 10.0
                _LOGGER.debug("Extracted voltage: %s", voltage)
                
                # Apply correction
                corrected_voltage = voltage + self._voltage_correction
                self._state = corrected_voltage
                self._available = True
                _LOGGER.debug("Voltage sensor updated successfully. Value: %s", corrected_voltage)
            except Exception as e:
                _LOGGER.warning("Error decoding voltage data: %s", e)
                self._available = False
                
        except Exception as e:
            _LOGGER.error("Error updating voltage sensor: %s", e, exc_info=True)
            self._available = False
            
    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        if self._state is not None:
            # Return voltage as integer
            return int(round(self._state))
        return self._state
        
    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

class TuyaCurrentSensor(TuyaBaseSensor):
    """Representation of a Tuya Current sensor."""
    
    def __init__(
        self,
        source_entity: str,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the current sensor."""
        super().__init__(source_entity, config_entry)
        self._attr_translation_key = "current"
        self._attr_native_unit_of_measurement = UnitOfElectricCurrent.AMPERE
        self._attr_icon = "mdi:current-ac"
        
    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"{self._config_entry.title} {self._attr_translation_key}"
        
    @property
    def _current_correction(self) -> float:
        """Return the current correction from config."""
        return self._config_entry.data.get(CONF_CURRENT_CORRECTION, DEFAULT_CURRENT_CORRECTION)
        
    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        try:
            _LOGGER.debug("Updating current sensor for source entity: %s", self._source_entity)
            source_state = self.hass.states.get(self._source_entity)
            if source_state is None:
                _LOGGER.warning("Source entity %s not found", self._source_entity)
                self._available = False
                return
                
            _LOGGER.debug("Source entity state: %s", source_state)
            _LOGGER.debug("Source entity attributes: %s", source_state.attributes)
                
            if source_state.state == "unavailable":
                self._available = False
                return
                
            # Decode base64 data
            base64_data = source_state.state
            _LOGGER.debug("Base64 data: %s", base64_data)
            if not base64_data:
                self._available = False
                return
                
            try:
                # Decode base64 string to bytes
                decoded_bytes = base64.b64decode(base64_data)
                _LOGGER.debug("Decoded bytes: %s", decoded_bytes)
                
                # Extract current from byte 4
                current_raw = decoded_bytes[4]
                current = current_raw * 0.00593
                _LOGGER.debug("Extracted current: %s", current)
                
                # Apply correction
                corrected_current = current + self._current_correction
                # Ensure current doesn't go negative (when no load is present)
                self._state = max(0, corrected_current)
                self._available = True
                _LOGGER.debug("Current sensor updated successfully. Value: %s", corrected_current)
            except Exception as e:
                _LOGGER.warning("Error decoding current data: %s", e)
                self._available = False
                
        except Exception as e:
            _LOGGER.error("Error updating current sensor: %s", e, exc_info=True)
            self._available = False
            
    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        if self._state is not None:
            # Return current with 2 decimal places as requested
            return round(self._state, 2)
        return self._state
        
    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

class TuyaPowerSensor(TuyaBaseSensor):
    """Representation of a Tuya Power sensor."""
    
    def __init__(
        self,
        source_entity: str,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize the power sensor."""
        super().__init__(source_entity, config_entry)
        self._attr_translation_key = "power"
        self._attr_native_unit_of_measurement = UnitOfPower.KILO_WATT
        self._attr_icon = "mdi:lightning-bolt"
        
    @property
    def name(self) -> str:
        """Return the name of the sensor."""
        return f"{self._config_entry.title} {self._attr_translation_key}"
        
    @property
    def _power_correction(self) -> float:
        """Return the power correction from config."""
        return self._config_entry.data.get(CONF_POWER_CORRECTION, DEFAULT_POWER_CORRECTION)
        
    async def async_update(self) -> None:
        """Fetch new state data for the sensor."""
        try:
            _LOGGER.debug("Updating power sensor for source entity: %s", self._source_entity)
            source_state = self.hass.states.get(self._source_entity)
            if source_state is None:
                _LOGGER.warning("Source entity %s not found", self._source_entity)
                self._available = False
                return
                
            _LOGGER.debug("Source entity state: %s", source_state)
            _LOGGER.debug("Source entity attributes: %s", source_state.attributes)
                
            if source_state.state == "unavailable":
                self._available = False
                return
                
            # Decode base64 data
            base64_data = source_state.state
            _LOGGER.debug("Base64 data: %s", base64_data)
            if not base64_data:
                self._available = False
                return
                
            try:
                # Decode base64 string to bytes
                decoded_bytes = base64.b64decode(base64_data)
                _LOGGER.debug("Decoded bytes: %s", decoded_bytes)
                
                # Extract voltage from first two bytes (big-endian) and divide by 10
                voltage_raw = int.from_bytes(decoded_bytes[0:2], byteorder='big')
                voltage = voltage_raw / 10.0
                _LOGGER.debug("Extracted voltage: %s", voltage)
                
                # Extract current from byte 4
                current_raw = decoded_bytes[4]
                current = current_raw * 0.00593
                _LOGGER.debug("Extracted current: %s", current)
                
                # Calculate power as voltage * current
                power = voltage * current
                _LOGGER.debug("Calculated power: %s", power)
                
                # Apply correction
                corrected_power = power + self._power_correction
                # Ensure power doesn't go negative
                self._state = max(0, corrected_power)
                self._available = True
                _LOGGER.debug("Power sensor updated successfully. Value: %s", corrected_power)
            except Exception as e:
                _LOGGER.warning("Error decoding power data: %s", e)
                self._available = False
                
        except Exception as e:
            _LOGGER.error("Error updating power sensor: %s", e, exc_info=True)
            self._available = False
            
    @property
    def native_value(self) -> float | None:
        """Return the state of the sensor."""
        if self._state is not None:
            # Convert watts to kilowatts with 2 decimal places as requested
            kw_value = self._state / 1000.0
            return round(kw_value, 2)
        return self._state
        
    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available
