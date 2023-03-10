#NOTE: trova le risposte
import cerca_risposte
#NOTE: scarica le domande e risponde alle domande
import scarica_rispondi

domande = True
risposte = False
# Scarica le domande
scarica_rispondi.main(domande, risposte)

parametro = 0.90
# Trova le risposte
while parametro <= 0.90 and parametro >= 0.70:
    cerca_risposte.main(parametro)
    parametro -= 0.01
    parametro = round(parametro, 2)

domande = False
risposte = True
# Risponde alle domande
scarica_rispondi.main(domande, risposte)

print("Finito")