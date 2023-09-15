import os
import re
import config
from pathlib import Path
import cv2
from search.risposte_immagini import magicFunction
from skimage.metrics import structural_similarity 

def main(valore, quante_domande):
    start(valore, quante_domande)

def start(valore, quante_domande):
    incidenza = float(valore)
    out = open('output.txt', 'w')
    for index in range(0, quante_domande):
        if index == 12:
            pass
        dir = 'Domanda_' + str(index)
        pat_img = Path('./Data/' + dir + '/Domanda.png')
        if not pat_img.exists(): 
            file = Path('./Data/' + dir + '/Scelta_1.txt')
            if file.exists():
               risposta = domanda_test_risp_test(index)
            else:
                risposta = domanda_test_risp_img(index,incidenza)
        else: 
            file = Path('./Data/' + dir + '/Scelta_1.txt')
            if file.exists():  
                risposta = domanda_img_risp_test(index,incidenza)
            else:
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
   (p,d) = structural_similarity(gray, gray2, full=True) 
   if p > incidenza:
        return 1
   return 0
       
def confronta(img1,img2):
   imm1 = cv2.imread(img1)
   r = cv2.resize(imm1, dsize=(500, 500))
   imm2 = cv2.imread(img2)
   r2 = cv2.resize(imm2, dsize=(500, 500))
   gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
   gray2 = cv2.cvtColor(r2, cv2.COLOR_BGR2GRAY)
   (p,d) = structural_similarity(gray, gray2, full=True) 
   return p

def domanda_test_risp_test(index):
     for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                dom_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png')
                if not dom_img.exists() and not risp_img.exists():
                    file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame, file_domanda_corrente)
                    if res == 1: 
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
                            return magicFunction(file_domanda_esame,risp1,risp2,risp3)  
     return "?" 

def domanda_test_risp_img(index,incidenza):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir) 
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                dom_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_txt = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt')
                if not dom_img.exists() and not risp_txt.exists():
                    file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame, file_domanda_corrente)
                    if res == 1:
                        file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                        risp1 = './Data/Domanda_' + str(index)  + '/Scelta_1.png'
                        risp2 = './Data/Domanda_' + str(index)  + '/Scelta_2.png'
                        risp3 = './Data/Domanda_' + str(index)  + '/Scelta_3.png'
                        if config.OS == 'WINDOWS':
                            os.system("copy " + file_corretto.replace('/','\\') + " .\\risposta_" + str(index) + ".png")
                        elif config.OS == 'UNIX':
                            os.system("cp  " + file_corretto + " ./risposta_" + str(index) + ".png")
                        value1 = confronta(file_corretto,risp1)
                        value2 = confronta(file_corretto,risp2)
                        value3 = confronta(file_corretto,risp3)
                        if value1 == max(value1,value2,value3):
                            return "1"
                        elif value2 == max(value1,value2,value3):
                            return "2"
                        elif value3 == max(value1,value2,value3):
                            return "3"
                        return "Immagine"
    return "?" 

def domanda_img_risp_test(index,incidenza):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                dom_png = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_img = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png')
                if dom_png.exists() and not risp_img.exists():
                    file_domanda_esame_txt = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame_txt, file_domanda_corrente_txt)
                    if res == 1: 
                        file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1:
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
                                return magicFunction(file_domanda_esame_txt,risp1,risp2,risp3,file_domanda_esame,incidenza) 
    return "?" 

def domanda_img_risp_img(index,incidenza):
    for dir in os.listdir('./esami'):
            esame = os.listdir('./esami/' + dir)  
            esame = esame[0]
            num_domande = len(os.listdir('./esami/' + dir + '/' + esame))
            for i in range(num_domande):
                domanda = 'Question_' + str(i)
                ls = os.listdir('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/')
                dom_png = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png')
                risp_txt = Path('./esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt')
                if dom_png.exists() and not risp_txt.exists():
                    file_domanda_esame_txt = './Data/Domanda_' + str(index)  + '/Domanda.txt'
                    file_domanda_corrente_txt = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.txt'
                    res = confronta_file(file_domanda_esame_txt, file_domanda_corrente_txt)
                    if res == 1:
                        file_domanda_esame = './Data/Domanda_' + str(index)  + '/Domanda.png'
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: 
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.png'
                            risp1 = './Data/Domanda_' + str(index)  + '/Scelta_1.png'
                            risp2 = './Data/Domanda_' + str(index)  + '/Scelta_2.png'
                            risp3 = './Data/Domanda_' + str(index)  + '/Scelta_3.png'
                            if config.OS == 'WINDOWS':
                                os.system("copy " + file_corretto.replace('/','\\') + " .\\risposta_" + str(index) + ".png")
                            elif config.OS == 'UNIX':
                                os.system("cp  " + file_corretto + " ./risposta_" + str(index) + ".png")
                            value1 = confronta(file_corretto,risp1)
                            value2 = confronta(file_corretto,risp2)
                            value3 = confronta(file_corretto,risp3)
                            if value1 == max(value1,value2,value3):
                                return "1"
                            elif value2 == max(value1,value2,value3):
                                return "2"
                            elif value3 == max(value1,value2,value3):
                                return "3"
                            return "Immagine"
    return "?" 