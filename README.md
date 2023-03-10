# Jarvis - Exam Bot & Scraper 

## Requisiti prima di utilizzare il programma
Seguire i seguenti passaggi per poter installare i requisiti necessari per poter utilizzare il programma. 

## Selenium e ChromeDriver
> **ATTENZIONE**: Questa parte è necessaria per poter utilizzare il programma sia per lo scraping che per l'esecuzione durante l'esame.

Installare Selenium con pip.
```
pip install selenium
```

Installare ChromeDriver, controllare la propria versione di Chrome per installare il ChromeDriver compatibile. Scaricare il file dal sito di [ChromeDriver](https://sites.google.com/chromium.org/driver/downloads?authuser=0). Spostare il file in una cartella a scelta.  

Aprire il file `exams.py` e modificare la variabile `service` con il percorso del file `chromedriver.exe` appena scaricato.

```
service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
``` 

### Chrome in remote debugging mode
> **ATTENZIONE**: Questa parte è necessaria per utilizzare il programma durante l'esame.

Per poter utilizzare il programma durante l'esame è necessario aprire Chrome in remote debugging mode. Questo permette di controllare Chrome da un programma esterno. Seguire i seguenti passaggi per aprire Chrome in remote debugging mode. 
> **ATTENZIONE**: I seguenti passaggi sono stati testati su Mac OS e Linux. Per Windows fare riferimento a questa [guida](https://robocorp.com/docs/development-guide/browser/how-to-attach-to-running-chrome-browser). 

1. Aprire una nuova finestra di terminale.
2. Trovare il percorso di Chrome e cercare l'eseguibile `Google Chrome`. Copiare il percorso dell'eseguibile.
3. Sostiutire il percorso `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome` dell'eseguibile con il vostro.
4. Sostituire `/tmp/chrome_dev_session` con il percorso di una cartella a scelta. Questa cartella conterrà i dati di Chrome. 
```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome_dev_session"
```
Una volta eseguito il comando, Chrome si aprirà in una nuova finestra. Utilizzare questa finestra durante l'esame, una volta terminato l'esame chiudere la finestra e il terminale. 

## Come utilizzare il programma durante l'esame
Per poter utilizzare il programma durante l'esame è necessario seguire i seguenti passaggi. Prima di tutto eseguire lo scraper per raccogliere le domande e le risposte. Una volta terminato lo scraping, eseguire il programma su un esame di prova. Assicurarsi che il programma funzioni correttamente. Una volta terminato l'esame di prova, eseguire il programma durante l'esame vero e proprio.

### Utilizzo prima dell'esame 
> **ATTENZIONE**: In questa fase si procede con il scraping delle domande e risposte di ogni esame presente su elearning. Nota bene che il scraper esegue lo scraping per gli esami ma anche per il sample test. Per questo motivo utilizziamo due file `exams.py` e `sample_test.py`.

1. TODO

### Utilizzo durante l'esame
> **ATTENZIONE**: Non toccare il mouse o la tastiera durante l'esecuzione del programma.

1. Iniziare l'esame, avete 30 minuti a disposizione. (Loggare su Moodle e inserire la password data dall'professore per sbloccare l'esame)
2. Aprire il file `jarvis.py` ed eliminare il commento per la funzione `getQuestions()`.    
3. Eseguire il file `jarvis.py` con il comando `python jarvis.py` da terminale. Non toccare il mouse o la tastiera durante l'esecuzione del programma. Il programma utilizzerà la finestra Chrome che abbiamo aperto prima per prendere i dati e salvarli nella cartella `Data`. Questo processo richiede in media 1 o 2 minuti.
4. Una volta terminato il programma, sulla console ci sarà un messaggio che ci dice che il programma è terminato. 
5. Aprire il file `jarvis.py` ed eliminare il commento per la funzione `rispondi()`.
6. TODO 
7. Eseguire il file `jarvis.py` con il comando `python jarvis.py` da terminale. Non toccare il mouse o la tastiera durante l'esecuzione del programma. Il programma utilizzerà la finestra Chrome per inserire le risposte presenti nel file `risposte.txt`. Questo processo richiede in media 1 o 2 minuti.

### Utilizzo dopo l'esame 
Lasciare una stella alla repository se ti è stato utile. Grazie! 

> **ATTENZIONE**: Questo programma è stato realizzato per scopo di esperienza personale. Non mi assumo nessuna responsabilità per l'utilizzo che ne verrà fatto.

## License
[MIT](https://choosealicense.com/licenses/mit/)