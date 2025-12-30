# Istruzioni per la pubblicazione su GitHub

## Creazione del repository

1. Accedi al tuo account GitHub
2. Clicca sul pulsante "New" per creare un nuovo repository
3. Inserisci il nome del repository: `local-tuya-decoder-Smart-Circuit-Breaker`
4. Aggiungi una descrizione (opzionale)
5. Scegli se rendere il repository pubblico o privato
6. Non inizializzare il repository con un README, .gitignore o licenza
7. Clicca su "Create repository"

## Caricamento dei file

1. Apri una finestra del terminale o del prompt dei comandi
2. Naviga fino alla directory del progetto:
   ```
   cd percorso/del/progetto/local-tuya-decoder-Smart-Circuit-Breaker
   ```
3. Inizializza il repository Git:
   ```
   git init
   ```
4. Aggiungi tutti i file al repository:
   ```
   git add .
   ```
5. Crea il primo commit:
   ```
   git commit -m "Initial commit"
   ```
6. Aggiungi il repository remoto (usa l'URL del tuo repository GitHub):
   ```
     git remote add origin https://github.com/MarlonMarketing/local-tuya-decoder-Smart-Circuit-Breaker.git
   ```
7. Carica i file su GitHub:
   ```
   git push -u origin master
   ```

## Creazione di una release

1. Vai alla pagina del tuo repository su GitHub
2. Clicca su "Releases" nella barra laterale destra
3. Clicca su "Draft a new release"
4. Inserisci un tag version (es. v1.0.2)
5. Inserisci un titolo per la release (es. Version 1.0.2)
6. Aggiungi una descrizione della release (puoi copiare il contenuto del file RELEASE_NOTES.md)
7. Allega il file `tuya_decoder_manager_v1.0.2.zip` alla release
8. Clicca su "Publish release"

## Aggiornamento della documentazione

Dopo aver creato il repository, puoi aggiornare i file README per includere i link corretti alle release e ad altri file del repository.
