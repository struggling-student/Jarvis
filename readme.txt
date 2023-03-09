Bisogna aggiungere la directory "esami" con dentro tutte le directory "Exam_*"
Per eseguirlo lanciare il file run.sh passand in input 1 se la risposta ha del txt, 0 se ha immagini
Inserire nl file "domanda.txt", l'intera domanda comprese le risposte(copiare e incollare tutto il testo)
Il programma stampa a video un numero compreso tra 1 e 3 se la risposta è testuale, e il numero indica l'indice della risposta giusta
Se la risposta è un immagine, viene caricata la cartella "Answer" nella dir dove si è lanciato il programma e da li si confronta l'immagine con quelle del testo
Se non trova la domanda ritorna -1
il file url.txt e get_screen servono per le domande con immagine ma per il momento non vengono usati
