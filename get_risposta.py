
import os
import re
from pathlib import Path
import cv2
from skimage.metrics import structural_similarity 
import numpy as np


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



def domanda_img_risp_test(domandatxt_now,incidenza):
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

                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(domandatxt_now, file_domanda_corrente_txt)
                    if res == 1: #sono uguali,confronto image
                        file_domanda_esame = 'Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: #sono uguali
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                            risp1 =  'risp1.txt'
                            risp2 =  'risp2.txt'
                            risp3 =  'risp3.txt'
                            if confronta_file(file_corretto,risp1) == 1:
                                return "1"
                            elif confronta_file(file_corretto,risp2) == 1:
                                return "2"
                            elif confronta_file(file_corretto,risp3) == 1:
                                return "3"
    return "?" #non ho trovato la domanda corretta

def domanda_img_risp_img(domandatxt_now,incidenza):
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
                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(domandatxt_now, file_domanda_corrente_txt)
                    if res == 1: #sono uguali,confronto image
                        file_domanda_esame = 'Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: #sono uguali
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                            os.system("cp  " + file_corretto + " ./risposta.png")
                            return "Immagine"
    return "?" #non ho trovato la domanda corretta


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
    f = open('domanda.txt', 'w')
    f.write(dom)
    f.close()
    return "domanda.txt"


def start(num):
    num = int(num)
    if num == 1 or num == 2:
        dom = prendiDomanda(1)
    else:
        dom = prendiDomanda(0)
    if num == 1:  #test-> test
            risposta = domanda_test_risp_test(dom)
    elif num == 11: #test->img
        risposta = domanda_test_risp_img(dom)
    elif num == 2: #img->test
        risposta = domanda_img_risp_test(dom,0.77)
    elif num == 22: #img->img
        risposta = domanda_img_risp_img(dom,0.77)
    return risposta

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



def domanda_test_risp_test(domanda_now):
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
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(domanda_now, file_domanda_corrente)
                    if res == 1: #sono uguali
                        file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                        risp1 =  'risp1.txt'
                        risp2 =  'risp2.txt'
                        risp3 =  'risp3.txt'
                        if confronta_file(file_corretto,risp1) == 1:
                            return "1"
                        elif confronta_file(file_corretto,risp2) == 1:
                            return "2"
                        elif confronta_file(file_corretto,risp3) == 1:
                            return "3"
                        
     return "?" #non ho trovato la domanda corretta

def domanda_test_risp_img(domanda_now):
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
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(domanda_now, file_domanda_corrente)
                    if res == 1: #sono uguali
                        file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                        os.system("cp " + file_corretto + " ./risposta.png")
                        return "Immagine"
                    
    return "?" #non ho trovato la domanda corretta
