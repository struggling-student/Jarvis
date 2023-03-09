import get_risposta
import get_screen
import os
import sys

def run(x):
    #cancello risp
    try:
        os.remove('risp1.txt')
        os.remove('risp2.txt')
        os.remove('risp3.txt')
        os.remove('risposta.txt')
    except:
        pass
    #scarico immagine
    #get_screen.run_screen()
    #avvio programma
    out = get_risposta.run_domanda(x)
    fp = open('domanda.txt', 'w')
    fp.close()
    fp = open('url.txt', 'w')
    fp.close()
    return out




if __name__ == "__main__":

    print("inserire 1 se le risposte sono scritte, 0 se sono immagini")
    nome_script, primo = sys.argv
    out = run(int(primo))
   # out = run(1)
    print(out)
