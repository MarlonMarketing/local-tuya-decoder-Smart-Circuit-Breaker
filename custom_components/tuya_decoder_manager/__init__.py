"""L'integrazione Tuya Decoder Manager per Home Assistant.
Questa integrazione consente di decodificare i dati dei dispositivi Tuya.
"""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Configura l'integrazione Tuya Decoder Manager a partire da una voce di configurazione.
    
    Questa funzione viene chiamata quando l'integrazione viene caricata in Home Assistant.
    Si occupa di inizializzare l'integrazione e di registrare un listener per gli aggiornamenti.
    
    Args:
        hass (HomeAssistant): L'istanza di Home Assistant.
        entry (ConfigEntry): La voce di configurazione dell'integrazione.
        
    Returns:
        bool: True se l'impostazione è avvenuta con successo, False altrimenti.
    """
    # Configura le piattaforme dell'integrazione (in questo caso, solo i sensori)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    # Registra un listener per gli aggiornamenti della configurazione
    # Questo listener verrà chiamato quando la configurazione dell'integrazione viene modificata
    entry.async_on_unload(entry.add_update_listener(update_listener))
    
    # Restituisce True per indicare che l'impostazione è avvenuta con successo
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Rimuove l'integrazione Tuya Decoder Manager da Home Assistant.
    
    Questa funzione viene chiamata quando l'integrazione viene rimossa da Home Assistant.
    Si occupa di rimuovere tutte le piattaforme associate all'integrazione.
    
    Args:
        hass (HomeAssistant): L'istanza di Home Assistant.
        entry (ConfigEntry): La voce di configurazione dell'integrazione.
        
    Returns:
        bool: True se la rimozione è avvenuta con successo, False altrimenti.
    """
    # Rimuove tutte le piattaforme associate all'integrazione
    # In questo caso, rimuove i sensori creati dall'integrazione
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Listener per gli aggiornamenti della configurazione.
    
    Questa funzione viene chiamata quando la configurazione dell'integrazione viene modificata.
    Si occupa di ricaricare l'integrazione per applicare le nuove impostazioni.
    
    Args:
        hass (HomeAssistant): L'istanza di Home Assistant.
        entry (ConfigEntry): La voce di configurazione dell'integrazione.
    """
    # Ricarica l'integrazione per applicare le nuove impostazioni
    await hass.config_entries.async_reload(entry.entry_id)
