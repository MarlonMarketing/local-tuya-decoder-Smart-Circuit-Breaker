"""Costanti per l'integrazione Tuya Decoder Manager in Home Assistant.
Questo file definisce tutte le costanti utilizzate nell'integrazione,
inclusi i nomi dei domini, le piattaforme, le configurazioni e gli attributi.
"""

# Nome del dominio dell'integrazione, utilizzato come identificatore univoco in Home Assistant
DOMAIN = "tuya_decoder_manager"

# Elenco delle piattaforme supportate dall'integrazione
# In questo caso, l'integrazione supporta solo i sensori
PLATFORMS = ["sensor"]

# Costanti per la configurazione dell'integrazione
# Identificatore del sensore sorgente da cui ottenere i dati Tuya
CONF_SOURCE_SENSOR = "source_sensor"

# Fattore di correzione per la tensione (in volt)
CONF_VOLTAGE_CORRECTION = "voltage_correction"

# Fattore di correzione per la corrente (in ampere)
CONF_CURRENT_CORRECTION = "current_correction"

# Fattore di correzione per la potenza (in watt)
CONF_POWER_CORRECTION = "power_correction"

# Nome del sensore da visualizzare in Home Assistant
CONF_NAME = "name"

# Valori predefiniti per la configurazione dell'integrazione
# Nome predefinito del sensore se non specificato dall'utente
DEFAULT_NAME = "Tuya Breaker"

# Valore predefinito per la correzione della tensione (nessuna correzione)
DEFAULT_VOLTAGE_CORRECTION = 0.0

# Valore predefinito per la correzione della corrente (nessuna correzione)
DEFAULT_CURRENT_CORRECTION = 0.0

# Valore predefinito per la correzione della potenza (nessuna correzione)
DEFAULT_POWER_CORRECTION = 0.0

# Attributi utilizzati dai sensori creati dall'integrazione
# Identificatore del sensore sorgente da cui vengono ottenuti i dati
ATTR_SOURCE_SENSOR = "source_sensor"

# Attributo per il valore della tensione (in volt)
ATTR_VOLTAGE = "voltage"

# Attributo per il valore della corrente (in ampere)
ATTR_CURRENT = "current"

# Attributo per il valore della potenza (in watt)
ATTR_POWER = "power"
