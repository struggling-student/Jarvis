#vado a leggere l'immagine domanda se presente
#e il testo della domanda
#navigo nel filesystem per prendere la risposta
#e la restituisco
#se non c'è la risposta resituisico 'non presente'
import os
import re
#import shutil
from pathlib import Path
import cv2
import numpy as np

from skimage.metrics import structural_similarity 

def main(valore):
    start(valore)
def start(valore):
    #incidenza = float(input("Inserisci l'incidenza di somiglianza tra le immagini(consiglio:partire da 0.9,se il foglio output resistuisce ? a qualche domanda, allora mettere 0.87,poi 0.85,0.83,etc.. fin quando non ci sono piu ?,se scende sotto 0.75 probabilmente la domanda non c'è): "))
    incidenza = float(valore)
    out = open('output.txt', 'w')
    for index in range(0, 50):
        if index == 12:
            pass
        enter = 0
        dir = 'Domanda_' + str(index)
        pat_img = Path('./Data/' + dir + '/Domanda.png')
        if not pat_img.exists(): #ho una sola domanda(testuale)
            #controllo le risposte
            file = Path('./Data/' + dir + '/Scelta_1.txt')
            if file.exists():  #ho risposte testuali
               risposta = domanda_test_risp_test(index)
            else:
                #confronto direttamente le immagini
                risposta = domanda_test_risp_img(index)
        else: #ho una domanda con immagine
            #controllo le risposte
            file = Path('./Data/' + dir + '/Scelta_1.txt')
            if file.exists():  #ho risposte testuali
                risposta = domanda_img_risp_test(index,incidenza)
            else:
                #confronto direttamente le immagini
                risposta = domanda_img_risp_img(index,incidenza)
        out.write(str(risposta)+'\n')
    out.close()

def confronta_file(file1, file2):
    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    stringa1 = f1.read()
    stringa2 = f2.read()
    stringa1, n = re.subn('The correct answer is:', '', stringa1)
    if stringa2.startswith("1.\n"):
        stringa2 = stringa2[3:]
    elif stringa2.startswith("2.\n"):
        stringa2 = stringa2[3:]
    elif stringa2.startswith("3.\n"):
        stringa2 = stringa2[3:]
    stringa1, n = re.subn(' ', '', stringa1)
    stringa1, n = re.subn('\n', '', stringa1)
    stringa2, n = re.subn(' ', '', stringa2)
    stringa2, n = re.subn('\n', '', stringa2)
    if stringa1 != stringa2:
        return 0
    return 1

def confronta_img(img1,img2,incidenza):
   imm1 = cv2.imread(img1)
   r = cv2.resize(imm1, dsize=(500, 500))
   imm2 = cv2.imread(img2)
   r2 = cv2.resize(imm2, dsize=(500, 500))
   gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
   gray2 = cv2.cvtColor(r2, cv2.COLOR_BGR2GRAY)
   (p,d) = structural_similarity(gray, gray2, full=True) #p è la percentuale di somiglianza, d è la matrice di differenza
   if p > incidenza:
        return 1
   return 0
       
   #cv2.imshow("image",gray)
   #cv2.imshow("image2",gray2)
   #cv2.waitKey(0)
   #cv2.destroyAllWindows()

  # return 0

def domanda_test_risp_test(index):
     for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  #question
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                #mi scarto tutte quelle che hanno domanda non testuale e/o risposta non testuale
                dom_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png')
                if not dom_img.exists() and not risp_img.exists():
                    #confronto question
                    file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame, file_domanda_corrente)
                    if res == 1: #sono uguali
                        file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                        risp1 =  './Data/Domanda_' + str(index)  + '/Scelta_1.txt'
                        risp2 =  './Data/Domanda_' + str(index)  + '/Scelta_2.txt'
                        risp3 =  './Data/Domanda_' + str(index)  + '/Scelta_3.txt'
                        if confronta_file(file_corretto,risp1) == 1:
                            return "1"
                        elif confronta_file(file_corretto,risp2) == 1:
                            return "2"
                        elif confronta_file(file_corretto,risp3) == 1:
                            return "3"
                        else:
                            return "-1"  #non ho trovato la risposta corretta(se succede controllare le risposte perche molto strano)
     return "?" #non ho trovato la domanda corretta

def domanda_test_risp_img(index):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  #question
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                #mi scarto tutte quelle che hanno domanda non testuale e/o risposta non testuale
                dom_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_txt = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt')
                if not dom_img.exists() and not risp_txt.exists():
                    #confronto question
                    file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame, file_domanda_corrente)
                    if res == 1: #sono uguali
                        file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                        risp1 = './Data/Domanda_' + str(index)  + '/Scelta_1.png'
                        risp2 = './Data/Domanda_' + str(index)  + '/Scelta_2.png'
                        risp3 = './Data/Domanda_' + str(index)  + '/Scelta_3.png'
                        os.system("cp " + file_corretto + " ./risposta_" + str(index) + ".png")
                        return "Immagine"
                       # if confronta_img(file_corretto,risp1) == 0:
                        #    return "1"
                       # elif confronta_img(file_corretto,risp2) == 0:
                        #    return "2"
                        #elif confronta_img(file_corretto,risp3) == 0:
                        #    return "3"
                      #  else:
                           # return "-1"  #non ho trovato la risposta corretta(se succede controllare le risposte perche molto strano)
    return "?" #non ho trovato la domanda corretta

def domanda_img_risp_test(index,incidenza):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  #question
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                #mi scarto tutte quelle che hanno domanda non testuale e/o risposta non testuale
                dom_png = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png')
                if dom_png.exists() and not risp_img.exists():
                    #confronto question.png e txt
                    file_domanda_esame_txt = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame_txt, file_domanda_corrente_txt)
                    if res == 1: #sono uguali,confronto image
                        file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: #sono uguali
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                            risp1 =  './Data/Domanda_' + str(index)  + '/Scelta_1.txt'
                            risp2 =  './Data/Domanda_' + str(index)  + '/Scelta_2.txt'
                            risp3 =  './Data/Domanda_' + str(index)  + '/Scelta_3.txt'
                            if confronta_file(file_corretto,risp1) == 1:
                                return "1"
                            elif confronta_file(file_corretto,risp2) == 1:
                                return "2"
                            elif confronta_file(file_corretto,risp3) == 1:
                                return "3"
                            else:
                                return "-1"  #non ho trovato la risposta corretta(se succede controllare le risposte perche molto strano)
    return "?" #non ho trovato la domanda corretta

def domanda_img_risp_img(index,incidenza):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  #question
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                #mi scarto tutte quelle che hanno domanda non testuale e/o risposta non testuale
                dom_png = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_txt = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt')
                if dom_png.exists() and not risp_txt.exists():
                     #confronto question.png e txt
                    file_domanda_esame_txt = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame_txt, file_domanda_corrente_txt)
                    if res == 1: #sono uguali,confronto image
                        file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: #sono uguali
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                            risp1 = './Data/Domanda_' + str(index)  + '/Scelta_1.png'
                            risp2 = './Data/Domanda_' + str(index)  + '/Scelta_2.png'
                            risp3 = './Data/Domanda_' + str(index)  + '/Scelta_3.png'
                            os.system("cp  " + file_corretto + " ./risposta_" + str(index) + ".png")
                            return "Immagine"
                        # if confronta_img(file_corretto,risp1) == 0:
                        #     return "1"
                        #  elif confronta_img(file_corretto,risp2) == 0:
                        #      return "2"
                        #  elif confronta_img(file_corretto,risp2) == 0:
                        #      return "3"
                        #  else:
                        #      return "-1"  #non ho trovato la risposta corretta(se succede controllare le risposte perche molto strano)
    return "?" #non ho trovato la domanda corretta

if __name__ == '__main__':
    start()