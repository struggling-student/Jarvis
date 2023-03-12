import os
import re
import cv2
from pathlib import Path
from skimage.metrics import structural_similarity 



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




def magicFunction(dom_txt,risp1,risp2,risp3,dom_img = None,incidenza=None):
    if dom_img == None:
        #check solo su domanda txt
        #devo controllare su tutto il db se la domanda è presente più volte
        return naviga1(dom_txt,risp1,risp2,risp3)
       
    else:
        #check su domanda txt e domanda img
        return naviga2(dom_txt,risp1,risp2,risp3,dom_img,incidenza)



def naviga1(file_domanda_esame,risp1,risp2,risp3):
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
                res = confronta_file(file_domanda_esame, file_domanda_corrente)
                if res == 1: #le domande sono uguali
                    file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                    if confronta_file(file_corretto,risp1) == 1:
                        return "1"
                    elif confronta_file(file_corretto,risp2) == 1:
                        return "2"
                    elif confronta_file(file_corretto,risp3) == 1:
                        return "3"
    return "-1"




def naviga2(file_domanda_esame_txt,risp1,risp2,risp3,file_domanda_esame,incidenza):
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
                    res = confronta_file(file_domanda_esame_txt, file_domanda_corrente_txt)
                    if res == 1: #sono uguali,confronto image
                       
                        file_domanda_corrente = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Question/question_' +str(i)+ '.png'
                        res = confronta_img(file_domanda_esame, file_domanda_corrente,incidenza)
                        if res == 1: #sono uguali
                            file_corretto = './esami/' + dir + '/' + esame + '/' + domanda + '/' + 'Answer/answer_' +str(i)+ '.txt'
                            if confronta_file(file_corretto,risp1) == 1:
                                return "1"
                            elif confronta_file(file_corretto,risp2) == 1:
                                return "2"
                            elif confronta_file(file_corretto,risp3) == 1:
                                return "3"
    return "-1"
