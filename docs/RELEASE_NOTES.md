# Tuya Decoder Manager - Release Notes

## Version 1.0.2

### Nuove funzionalità
- Aggiunta la possibilità di correggere i valori di tensione, corrente e potenza tramite parametri configurabili
- Implementata la decodifica dei dati in formato base64
- Creati tre sensori separati per tensione, corrente e potenza
- Aggiunto supporto per la localizzazione (inglese e italiano)
- Configurazione tramite interfaccia utente di Home Assistant

### Correzioni di bug
- Risolto il problema con il calcolo della potenza negativa
- Corretto l'algoritmo per l'estrazione della corrente dai dati base64
- Fix per garantire che i valori dei sensori non siano negativi

### Miglioramenti
- Aggiunta la documentazione completa in italiano e inglese
- Migliorata la gestione degli errori
- Ottimizzato il codice per una migliore efficienza
- Aggiunta la possibilità di modificare i valori di correzione senza dover riavviare Home Assistant

## Version 1.0.1

### Correzioni di bug
- Risolto un problema con la decodifica dei dati base64
- Corretta la definizione dei sensori nel file manifest.json

### Miglioramenti
- Aggiunta la documentazione iniziale

## Version 1.0.0

### Funzionalità iniziali
- Implementata la decodifica dei dati dei sensori Tuya
- Creati i sensori per tensione, corrente e potenza
- Configurazione iniziale tramite file di configurazione
