# Local Tuya Decoder per Smart Circuit Breaker

Local Tuya Decoder per Smart Circuit Breaker è un componente personalizzato per Home Assistant che decodifica i dati dei sensori Local Tuya Smart Circuit Breaker e li presenta come sensori separati per tensione, corrente e potenza.

## Caratteristiche

- Decodifica i dati dei sensori Smart Circuit Breaker in formato base64
- Crea tre sensori separati: tensione, corrente e potenza
- Supporta la correzione dei valori per una maggiore precisione
- Configurazione tramite interfaccia utente di Home Assistant
- Supporto per la localizzazione (inglese e italiano)
- Progettato specificamente per integrazione Local Tuya

## Prerequisiti

**⚠️ Requisito Importante**: Questo componente richiede che l'integrazione [Local Tuya](https://github.com/rospogrigio/localtuya) sia **installata e completamente funzionante** nella tua istanza di Home Assistant.

### Prima di Installare Questo Componente

1. **Installa Local Tuya prima** - Segui la [guida di installazione ufficiale di Local Tuya](https://github.com/rospogrigio/localtuya/wiki/Installation)
2. **Configura il tuo Smart Circuit Breaker** - Assicurati che il tuo Smart Circuit Breaker sia configurato correttamente e funzionante in Local Tuya
3. **Verifica i dati base64** - Assicurati che il tuo sensore Local Tuya stia fornendo dati in formato base64
4. **Testa l'integrazione Local Tuya** - Conferma che i tuoi dispositivi Local Tuya sono responsivi e stanno inviando dati

### Cosa Fornisce Local Tuya

- Scoperta e comunicazione con i dispositivi
- Dati del sensore in base64 dal tuo Smart Circuit Breaker
- Creazione di entità per i dati grezzi del sensore

Questa integrazione **si basa su** Local Tuya decodificando i dati base64 in valori significativi di tensione, corrente e potenza.

## Installazione

### Metodo 1: Installazione manuale

**⚠️ Controllo Prerequisiti**: Assicurati che Local Tuya sia installato e funzionante prima di procedere.

1. Scarica l'ultima versione del componente dalla sezione [Releases](https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker/releases)
2. Estrai il contenuto dell'archivio nella directory `custom_components` di Home Assistant:
   ```
   /config/custom_components/tuya_decoder_manager/
   ```
3. Riavvia Home Assistant

### Metodo 2: Installazione tramite HACS

**⚠️ Controllo Prerequisiti**: Assicurati che Local Tuya sia installato e funzionante prima di procedere.

1. Apri HACS in Home Assistant
2. Vai a "Integrazioni"
3. Clicca sul pulsante con i tre puntini nell'angolo in alto a destra
4. Seleziona "Personalizza repository"
5. Aggiungi il repository: `https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker`
6. Cerca "Local Tuya Decoder per Smart Circuit Breaker" e installa l'integrazione
7. Riavvia Home Assistant

## Configurazione

**📋 Prerequisiti**: La tua integrazione Local Tuya deve essere completamente configurata e il tuo Smart Circuit Breaker deve fornire dati prima di procedere.

1. Vai a "Impostazioni" -> "Dispositivi e servizi" in Home Assistant
2. Clicca sul pulsante "Aggiungi integrazione"
3. Cerca "Local Tuya Decoder per Smart Circuit Breaker" e selezionalo
4. Compila i seguenti campi:
   - **Nome**: Nome dell'integrazione (es. "Decoder Smart Circuit Breaker")
   - **Scegli sensore o entità**: Seleziona l'entità sensore Local Tuya che fornisce dati in formato base64 (questa entità dovrebbe essere creata dalla tua integrazione Local Tuya)
   - **Valore correzione tensione (V)**: Valore di correzione per la tensione (valore predefinito: 0)
   - **Valore correzione corrente (A)**: Valore di correzione per la corrente (valore predefinito: 0)
   - **Correzione potenza (W)**: Valore di correzione per la potenza (valore predefinito: 0)
5. Clicca su "Invia" per completare la configurazione

**💡 Suggerimento**: Se non vedi il tuo sensore nell'elenco a discesa, torna alla configurazione di Local Tuya e assicurati che il tuo Smart Circuit Breaker sia configurato correttamente e stia fornendo dati.

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

### Problemi Relativi a Local Tuya

- **🔍 Controlla Installazione Local Tuya**: Assicurati che l'integrazione Local Tuya sia installata correttamente e abilitata
- **📡 Verifica Connessione Dispositivo**: Assicurati che il tuo Smart Circuit Breaker sia connesso a Local Tuya e responsivo
- **📊 Controlla Dati Grezzi**: Verifica che il sensore Local Tuya fornisca dati in formato base64
- **🔄 Testa Entità Local Tuya**: Conferma che la tua entità Local Tuya si stia aggiornando con nuovi dati in Strumenti per Sviluppatori

### Problemi di Integrazione

- **📋 Controlla Configurazione**: Assicurati che l'integrazione sia stata configurata correttamente
- **🔍 Seleziona Entità Corretta**: Assicurati di aver selezionato l'entità Local Tuya corretta durante la configurazione
- **📝 Controlla Log di Home Assistant**: Cerca eventuali errori nei log di Home Assistant relativi a questa integrazione
- **🔄 Riavvia Home Assistant**: Prova a riavviare Home Assistant dopo le modifiche alla configurazione

### Problemi Comuni

- **Nessuna entità disponibile nell'elenco**: Questo di solito significa che Local Tuya non è configurato o il dispositivo non sta fornendo dati
- **Sensori mostrano unavailable**: Controlla se il dispositivo Local Tuya è online e connesso
- **Valori errati**: Verifica i valori di correzione e assicurati che il tuo dispositivo sia il modello Smart Circuit Breaker previsto
- **Integrazione non trovata**: Assicurati che i file del componente personalizzato siano nella directory corretta

### Per Ottenere Aiuto

- Controlla la [documentazione di Local Tuya](https://github.com/rospogrigio/localtuya/wiki) per la configurazione del dispositivo
- Apri una issue su questo repository con i log di Home Assistant
- Verifica che la tua configurazione Local Tuya funzioni prima di configurare questo decoder

## Contributi

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request sul repository GitHub.

## Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file [LICENSE](LICENSE) per i dettagli.