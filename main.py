#NOTE: trova le risposte
import time
import cerca.cerca_risposte as cerca_risposte
#NOTE: scarica le domande e risponde alle domande
import scarica.scarica_rispondi as scarica_rispondi

# per il time.sleep() ovvero quanti secondi vuoi che aspetta tra un'operazione e l'altra
tempo_di_attesa = 0
quante_domande = 10
domande = True
risposte = False
# Scarica le domande
time.sleep(tempo_di_attesa)
scarica_rispondi.main(domande, risposte, quante_domande, tempo_di_attesa)

parametro = 0.90
# Trova le risposte
while parametro <= 0.90 and parametro >= 0.70:
    cerca_risposte.main(parametro, quante_domande)
    parametro -= 0.01
    parametro = round(parametro, 2)

domande = False
risposte = True
# NOTE: se metti qui sotto tempo_di_attesa = 5, ci mette 5 secondi tra il rispondere a una domanda e l'altra.
# tempo_di_attesa = 5

# Risponde alle domande
time.sleep(tempo_di_attesa)
scarica_rispondi.main(domande, risposte, quante_domande, tempo_di_attesa)
