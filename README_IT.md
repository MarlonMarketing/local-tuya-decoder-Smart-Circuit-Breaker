# Local Tuya Decoder per Smart Circuit Breaker

Local Tuya Decoder per Smart Circuit Breaker è un componente personalizzato per Home Assistant che decodifica i dati dei sensori Local Tuya Smart Circuit Breaker e li presenta come sensori separati per tensione, corrente e potenza.

## Caratteristiche

- Decodifica i dati dei sensori Smart Circuit Breaker in formato base64
- Crea tre sensori separati: tensione, corrente e potenza
- Supporta la correzione dei valori per una maggiore precisione
- Configurazione tramite interfaccia utente di Home Assistant
- Supporto per la localizzazione (inglese e italiano)
- Progettato specificamente per integrazione Local Tuya

## Installazione

### Metodo 1: Installazione manuale

1. Scarica l'ultima versione del componente dalla sezione [Releases](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/releases)
2. Estrai il contenuto dell'archivio nella directory `custom_components` di Home Assistant:
   ```
   /config/custom_components/tuya_decoder_manager/
   ```
3. Riavvia Home Assistant

### Metodo 2: Installazione tramite HACS

1. Apri HACS in Home Assistant
2. Vai a "Integrazioni"
3. Clicca sul pulsante con i tre puntini nell'angolo in alto a destra
4. Seleziona "Personalizza repository"
5. Aggiungi il repository: `https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker`
6. Cerca "Local Tuya Decoder per Smart Circuit Breaker" e installa l'integrazione
7. Riavvia Home Assistant

## Configurazione

1. Vai a "Impostazioni" -> "Dispositivi e servizi" in Home Assistant
2. Clicca sul pulsante "Aggiungi integrazione"
3. Cerca "Local Tuya Decoder per Smart Circuit Breaker" e selezionalo
4. Compila i seguenti campi:
   - **Nome**: Nome dell'integrazione (es. "Decoder Smart Circuit Breaker")
   - **Scegli sensore o entità**: Seleziona il sensore Local Tuya che fornisce i dati in base64
   - **Valore correzione tensione (V)**: Valore di correzione per la tensione (valore predefinito: 0)
   - **Valore correzione corrente (A)**: Valore di correzione per la corrente (valore predefinito: 0)
   - **Correzione potenza (W)**: Valore di correzione per la potenza (valore predefinito: 0)
5. Clicca su "Invia" per completare la configurazione

## Utilizzo

Dopo la configurazione, l'integrazione creerà automaticamente tre sensori:

- **Tensione**: Mostra la tensione in Volt (V)
- **Corrente**: Mostra la corrente in Ampere (A)
- **Potenza**: Mostra la potenza in Kilowatt (kW)

I valori vengono calcolati utilizzando i seguenti algoritmi:

### Tensione
1. Decodifica i dati base64 in byte
2. Estrae i primi 2 byte (big-endian)
3. Divide per 10 per ottenere il valore in Volt
4. Applica la correzione configurata

### Corrente
1. Decodifica i dati base64 in byte
2. Estrae il quinto byte (indice 4)
3. Moltiplica per 0.00593 per ottenere il valore in Ampere
4. Applica la correzione configurata
5. Garantisce che il valore non sia negativo

### Potenza
1. Calcola tensione e corrente come descritto sopra
2. Moltiplica tensione per corrente per ottenere la potenza in Watt
3. Applica la correzione configurata
4. Garantisce che il valore non sia negativo
5. Converte in Kilowatt con 2 decimali

## Configurazione avanzata

È possibile modificare i valori di correzione in qualsiasi momento:

1. Vai a "Impostazioni" -> "Dispositivi e servizi"
2. Trova l'integrazione "Local Tuya Decoder per Smart Circuit Breaker"
3. Clicca sui tre puntini nell'angolo in alto a destra
4. Seleziona "Opzioni"
5. Modifica i valori di correzione come necessario
6. Clicca su "Invia" per salvare le modifiche

## Risoluzione dei problemi

Se i sensori non vengono creati o non mostrano dati:

1. Verifica che il sensore Local Tuya fornisca dati in formato base64
2. Controlla i log di Home Assistant per eventuali errori
3. Assicurati che l'integrazione sia stata configurata correttamente
4. Prova a riavviare Home Assistant

## Contributi

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request sul repository GitHub.

## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.