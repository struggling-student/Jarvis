import get_risposta 
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
    out = get_risposta.start(x)
    fp = open('domanda.txt', 'w')
    fp.close()
    return out

if __name__ == "__main__":
    
    nome_script, primo = sys.argv
    #primo = 2
    out = run(int(primo))
   # out = run(1)
    print(out)