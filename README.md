# Jarvis - Il tuo assistente personale

Installa i requisiti tramite il comando:

```
pip install -r requirements.txt
```

Installa il driver per il browser che utilizzerai. Per il momento sono supportati solo Chrome. 

Inserisci il path del driver nel file `scarica_rispondi.py`:

```
service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
```

Esegui l'eseguibile di Chrome tramite console per abilitare il controllo remoto:

```
PATH_DEL_ESEGUIBILE_DI_GOOGLE_CHROME Chrome --remote-debugging-port=8989 --user-data-dir="DIRECTORY_TEMP_PER_CHROME_PROFILE”
```

Lancia il programma con ./run.sh

> **ATTENZIONE**: Questo programma è stato realizzato per scopo di esperienza personale. Non mi assumo nessuna responsabilità per l'utilizzo che ne verrà fatto.

## License
[MIT](https://choosealicense.com/licenses/mit/)