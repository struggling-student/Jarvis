import time
import search.cerca_risposte as cerca_risposte
import download.scarica_rispondi as scarica_rispondi

tempo_di_attesa = 0
quante_domande = 0
domande = True
risposte = False

time.sleep(tempo_di_attesa)
scarica_rispondi.main(domande, risposte, quante_domande, tempo_di_attesa)

parametro = 0.90

while parametro <= 0.90 and parametro >= 0.70:
    cerca_risposte.main(parametro, quante_domande)
    parametro -= 0.01
    parametro = round(parametro, 2)

domande = False
risposte = True

time.sleep(tempo_di_attesa)
scarica_rispondi.main(domande, risposte, quante_domande, tempo_di_attesa)