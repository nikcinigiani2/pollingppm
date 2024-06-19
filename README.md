# PollingApp

PollingApp è un'applicazione web basata su Django che consente agli utenti di creare, condividere e rispondere ai sondaggi.

## Funzionalità

- Creazione di sondaggi: gli utenti possono creare nuovi sondaggi con una domanda e diverse opzioni di risposta.
- Risposta ai sondaggi: gli utenti possono rispondere ai sondaggi esistenti selezionando una delle opzioni di risposta.
- Visualizzazione dei risultati: dopo aver risposto a un sondaggio, gli utenti possono vedere i risultati attuali del sondaggio.
- Autenticazione: gli utenti possono registrarsi, accedere e uscire dall'applicazione.

## Requisiti

- Python 3.12.0
- Django 5.0.6
- Django Rest Framework 3.15.1
- Gunicorn 22.0.0
- Whitenoise 6.6.0

Per installare tutte le dipendenze, eseguire il seguente comando:

```bash
pip install -r requirements.txt
```

## Esecuzione dell'applicazione

Per eseguire l'applicazione, utilizzare il seguente comando:

```bash
gunicorn PollingApp.wsgi:application --bind 0.0.0.0:$PORT
```

## Struttura del progetto

Il progetto è strutturato come un'applicazione Django standard. Il codice dell'applicazione si trova nella directory `polls_app`. Questa directory contiene i seguenti file:

- `Models.py`: definisce i modelli di dati per i sondaggi e le opzioni di risposta.
- `Views.py`: gestisce le richieste HTTP e restituisce le risposte HTTP.
- `urls.py`: definisce le rotte URL per l'applicazione.

## Contatti

Nik Cinigiani
nik.cinigiani@edu.unifi.it
