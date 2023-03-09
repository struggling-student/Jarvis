#vado a leggere l'immagine domanda se presente
#e il testo della domanda
#navigo nel filesystem per prendere la risposta
#e la restituisco
#se non c'è la risposta resituisico 'non presente'
import os
import re
import shutil

def confronta(img1, img2):
    res = os.system("diff " + img1 +" "+ img2)
    return res

def dammiRisposta():
        ls = os.listdir('Answer')
        fp = open("Answer/"+ls[0], 'r')
        stringa = ""
        for riga in fp:
            if riga != "\n":
                stringa += riga
        fp.close() 
        fp1 = open("risp1.txt", 'r')
        fp2 = open("risp2.txt", 'r')
        fp3 = open("risp3.txt", 'r')
        s1 = fp1.read()
        s2 = fp2.read()
        s3 = fp3.read()
        fp1.close()
        fp2.close()
        fp3.close()
        if s1[-1] == '\n':
            s1 = s1[:-1]
        if s2[-1] == '\n':
            s2 = s2[:-1]
        if s3[-1] == '\n':
            s3 = s3[:-1]
        if s1[0] == '\n':
            s1 = s1[1:]
        if s2[0] == '\n':
            s2 = s2[1:]
        if s3[0] == '\n':
            s3 = s3[1:]
        s1 = s1.strip()
        s2 = s2.strip()
        s3 = s3.strip()
        stringa = stringa[22:]
        stringa = stringa.strip()
        if stringa[0] == '\n':
            stringa = stringa[1:]
        if stringa[-1] == '\n':
            stringa = stringa[:-1]
        if s1 == stringa:
            return 1
        elif s2 == stringa:
            return 2
        elif s3 == stringa:
            return 3
        else:
            return -1
        



def prendiDomanda(x):
    fp = open('domanda.txt', 'r')
    dom = ''
    risp1 = ''
    risp2 = ''
    risp3 = ''
    domanda = 1
    one = 0
    two = 0
    if x == 1: #le risposte sono delle scritte
        for riga in fp:
            if domanda == 1:
                if riga != "Scegli un'alternativa:\n" and riga != "\n" and riga != "1.\n":
                    dom += riga
                elif( riga == "1.\n"):
                    domanda = 0
                    one = 1
            elif one == 1:
                if (riga != "\n" and riga != "2.\n"):
                    risp1 += riga
                elif(riga == "2.\n"):
                    one = 0
                    two = 1 
            elif two == 1:
                if (riga != "\n" and riga != "3.\n"):
                    risp2 += riga
                elif(riga == "3.\n"):
                    two = 0
                    three = 1
            else:
                if riga != "\n":
                    risp3 += riga  
        f1 = open('risp1.txt', 'w')
        f1.write(risp1)
        f1.close()
        f2 = open('risp2.txt', 'w')
        f2.write(risp2)
        f2.close()
        f3 = open('risp3.txt', 'w')
        f3.write(risp3)
    else: #le risposte sono delle immagini
        for riga in fp:
            if riga != "Scegli un'alternativa:\n" and riga != "\n":
                dom += riga
            elif riga == "Scegli un'alternativa:\n":
                break    
    fp.close()

    return dom

def run_domanda(number):
    question_to_search = prendiDomanda(number)[:-1]
    if os.path.exists('Answer'):
        #rimuovi
        shutil.rmtree('Answer')

    #navigo nel filesystem per prendere la risposta
    #e la restituisco
   # trovata = 0
    for dir in os.listdir('./esami'):
        x = re.search("Exam_*", dir) 
        if x != None: #ho fatto match
            quest = os.listdir('./esami/' + dir)  #question
            quest = quest[0]
            for domanda in os.listdir('./esami/' + dir + '/' + quest):
                #dentro domanda ho: answer, question, choice
                #mi serve answer e question
                #apro question
                ls = os.listdir('./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Question/')
                #dentro ls ho question.txt e(forse) question.png
                #apro question.txt
                if (len(ls)) == 1:
                    #ho solo question.txt
                    fp = open('./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Question/' + ls[0], 'r')
                    question = fp.read()[:-1]
                    #print(question)
                    fp.close()
                    #if question == question_to_search:
                    if question in question_to_search:
                        if number == 0: #ho solo immagini
                            os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                            return "guardare answer"
                        else:
                            #confronto la risposta con risp1.txt, risp2.txt, risp3.txt
                            #e creo un file con la risposta:1,2,3
                            os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                            out = dammiRisposta()
                            return out
                       # trovata = 1
                        #break
                else:
                    #ho question.txt e question.png
                    if(ls[0].endswith('.txt') == True):  #question.txt in prima posizione
                        fp = open('./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Question/' + ls[0], 'r')
                        question = fp.read()[:-1]
                        fp.close()
                        # print(question)
                        if question in question_to_search:
                            #cerco anche l'immagine
                            img = ls[1]
                            #confronto img con image.png
                            res = confronta(img, 'image.png')
                            if res == 0: #sono uguali
                                if number == 0: #ho solo immagini
                                    os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                                    return "guardare answer"
                                else:
                                    #confronto la risposta con risp1.txt, risp2.txt, risp3.txt
                                    #e creo un file con la risposta:1,2,3
                                    os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                                    out = dammiRisposta()
                                    return out
                                #trovata = 1
                               # break
                    else:
                        #ho question.png in prima posizione
                        fp = open('./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Question/' + ls[1], 'r')
                        question = fp.read()[:-1]
                        fp.close()
                        #print(question)
                        if question in question_to_search:
                            #cerco anche l'immagine
                            img = ls[0]
                            #confronto img con image.png
                            res = confronta(img, 'image.png')
                            if res == 0: #sono uguali
                                if number == 0: #ho solo immagini
                                    os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                                    return "guardare answer"
                                else:
                                    #confronto la risposta con risp1.txt, risp2.txt, risp3.txt
                                    #e creo un file con la risposta:1,2,3
                                    os.system('cp -r ./esami/' + dir + '/' + quest + '/' + domanda + '/' + 'Answer' +  " .")
                                    out = dammiRisposta()
                                    return out
                               # trovata = 1
                               # break
    return -1

