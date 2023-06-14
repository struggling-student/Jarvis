#NOTE : Imports, non toccare.
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

def get_image(driver, imgurl):
    headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    s = requests.session()
    s.headers.update(headers)

    for cookie in driver.get_cookies():
        c = {cookie['name']: cookie['value']}
        s.cookies.update(c)

    return s.get(imgurl, allow_redirects=True).content

def get_questions(driver, quante_domande, tempo_di_attesa):
    if quante_domande == 50:
       limite = 49 
    elif quante_domande == 10:
        limite = 9
    else:
        limite = 39
    #creo la directory per salvare le domande
    directory = f"Data"
    os.mkdir(directory)
    #NOTE : Cambiare il range in base al numero di domande
    for i in range(quante_domande):
        directory = f'Data/Domanda_{i}'
        os.mkdir(directory)

    #NOTE : Cambiare il range in base al numero di domande
    for i in range(quante_domande):
        time.sleep(tempo_di_attesa)
        #NOTE: Prende le domande dalla pagina 
        domande = driver.find_elements(by=By.XPATH, value='//div[@class="qtext"]')
        for domanda in domande:
            #NOTE: Se una domanda è un'immagine, allora salva l'immagine
            if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
                text_file = f"Data/Domanda_{i}/Domanda.txt"
                with open(text_file, "w", encoding="utf-8") as f:
                    f.write(domanda.text)

                photo_file = f"Data/Domanda_{i}/Domanda.png"
                with open(photo_file, "wb") as f:
                    imgurl = domanda.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                    #f.write(domanda.find_element(by=By.TAG_NAME, value="img").screenshot_as_png) 
                    f.write(get_image(driver, imgurl)) 
            #NOTE: Se una domanda è un testo, allora salva il testo
            else:
                file_name = f"Data/Domanda_{i}/Domanda.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(domanda.text)

        #NOTE: Prende le scelte dalla pagina 
        scelte = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
        contatore = 0
        numero = 0
        for scelta in scelte:
            if contatore == 3:
                contatore = 0
                numero=0
            #NOTE: Se una scelta è un'immagine, allora salva l'immagine
            if len(scelta.find_elements(by=By.TAG_NAME, value="img")) > 0:
                contatore+=1
                numero+=1
                file_name = f"Data/Domanda_{i}/Scelta_{numero}.png"
                with open(file_name, "wb") as f:
                    imgurl = scelta.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                    #f.write(scelta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
                    f.write(get_image(driver, imgurl)) 
            #NOTE: Se una scelta è un testo, allora salva il testo
            else:
                contatore+=1
                numero+=1
                file_name = f"Data/Domanda_{i}/Scelta_{numero}.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(scelta.text)
        
        if i == limite:
            print("Scaricato tutte le domande.")
            continua=driver.find_element(by=By.XPATH,value='//span[@class="thispageholder"]')
            continua.click()            
        else:        
            continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
            continua.click()

def rispondi(driver, quante_domande, tempo_di_attesa):
    if quante_domande == 50:
       limite = 49 
    elif quante_domande == 10:
        limite = 9
    else:
        limite = 39
    domanda = 0
    #NOTE: Prende il file output.txt    
    with open("./output.txt", "r") as f:
        output = f.read()
        output = output.split("\n")
        for risposta in output:
            time.sleep(tempo_di_attesa)
            if risposta == "Immagine":
                if domanda == limite:
                    print("Risposta nella cartella immagine.")
                    print("Risposto a tutte le domande.")
                else:
                    print("Risposta nella cartella immagine.")
                
                    domanda += 1      

                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click() 
            elif risposta == "1": 
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer0")]')
                    scelta.click()
                    print("Risposto a tutte le domande.")
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer0")]')
                    scelta.click()  

                    domanda += 1 

                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()                
            elif risposta == "2":
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer1")]')
                    scelta.click()
                    print("Risposto a tutte le domande.") 
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer1")]')
                    scelta.click()  

                    domanda += 1 

                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()                
            elif risposta == "3":
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer2")]')
                    scelta.click() 
                    print("Risposto a tutte le domande.")
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer2")]')
                    scelta.click()  

                    domanda += 1 

                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()
            else:
                if domanda == limite:
                    pass
                else:
                    print("Risposta non trovata.")

                    domanda += 1 

                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()   

def main(domande, risposte, quante_domande, tempo_di_attesa):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
    service = Service(r'C:\chromedriver\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    if domande == True:
        #NOTE : Prende le domande dalla pagina e le salva nella cartella data
        get_questions(driver, quante_domande, tempo_di_attesa)
    if risposte == True:
        #NOTE: Risponde alle domande in base al contenuto del file output.txt
        rispondi(driver, quante_domande, tempo_di_attesa)