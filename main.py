#NOTE: trova le risposte
import trova_risposte
#NOTE: scarica le domande e risponde alle domande
import scarica_domande

domande = True
risposte = False
# Scarica le domande
scarica_domande.main(domande, risposte)

parametro = 0.90
# Trova le risposte
while parametro <= 0.90 and parametro >= 0.70:
    trova_risposte.main(parametro)
    parametro -= 0.01
    parametro = round(parametro, 2)

domande = False
risposte = True
# Risponde alle domande
scarica_domande.main(domande, risposte)