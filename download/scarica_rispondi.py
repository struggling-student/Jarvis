import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import config
import base64
from PIL import Image
from colorama import init, Fore, Style

init(autoreset=True)
ok_text = "[DOWNLOAD]"
done_text = "[DONE]"
answer_text = "[ANSWER]"
error = "[ERROR]"

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
    directory = f"Data"
    os.mkdir(directory)
    for i in range(quante_domande):
        directory = f'Data/Domanda_{i}'
        os.mkdir(directory)
    for i in range(quante_domande):
        time.sleep(tempo_di_attesa)
        domande = driver.find_elements(by=By.XPATH, value='//div[@class="qtext"]')
        for domanda in domande:
            if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
                text_file = f"Data/Domanda_{i}/Domanda.txt"
                with open(text_file, "w", encoding="utf-8") as f:
                    f.write(domanda.text)
                photo_file = f"Data/Domanda_{i}/Domanda.png"
                with open(photo_file, "wb") as f:
                    imgurl = domanda.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                    if imgurl.startswith("data:image"):
                        imgurl = imgurl.split(",")[1]
                        f.write(base64.urlsafe_b64decode(imgurl)) 
                        im = Image.open(photo_file)
                        fill_color = (255, 255, 255)
                        im = im.convert("RGBA")  
                        if im.mode in ('RGBA', 'LA'):
                            background = Image.new(im.mode[:-1], im.size, fill_color)
                            background.paste(im, im.split()[-1]) 
                            im = background
                        im.convert("RGB").save(photo_file, 'PNG')
                    else:
                        f.write(get_image(driver, imgurl)) 
            else:
                file_name = f"Data/Domanda_{i}/Domanda.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(domanda.text)
        scelte = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
        contatore = 0
        numero = 0
        for scelta in scelte:
            if contatore == 3:
                contatore = 0
                numero=0
            if len(scelta.find_elements(by=By.TAG_NAME, value="img")) > 0:
                contatore+=1
                numero+=1
                file_name = f"Data/Domanda_{i}/Scelta_{numero}.png"
                with open(file_name, "wb") as f:
                    imgurl = scelta.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                    if imgurl.startswith("data:image"):
                        imgurl = imgurl.split(",")[1]
                        f.write(base64.urlsafe_b64decode(imgurl)) 
                        im = Image.open(file_name)
                        fill_color = (255, 255, 255)
                        im = im.convert("RGBA")   
                        if im.mode in ('RGBA', 'LA'):
                            background = Image.new(im.mode[:-1], im.size, fill_color)
                            background.paste(im, im.split()[-1]) 
                            im = background
                        im.convert("RGB").save(file_name, 'PNG')
                    else:
                        f.write(get_image(driver, imgurl)) 
            else:
                contatore+=1
                numero+=1
                file_name = f"Data/Domanda_{i}/Scelta_{numero}.txt"
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(scelta.text)
        if i == limite:
            downloaded_text = f"Question {i+1}"
            print(f"{Fore.GREEN}{Style.BRIGHT}{ok_text} {Fore.WHITE}{downloaded_text}")
            all_done_text = f"All questions downloaded"
            print(f"{Fore.GREEN}{Style.BRIGHT}{done_text} {Fore.WHITE}{all_done_text}")
            continua=driver.find_element(by=By.XPATH,value='//span[@class="thispageholder"]')
            continua.click()            
        else:    
            downloaded_text = f"Question {i+1}"
            print(f"{Fore.GREEN}{Style.BRIGHT}{ok_text} {Fore.WHITE}{downloaded_text}")
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
    with open("./output.txt", "r") as f:
        output = f.read()
        output = output.split("\n")
        for risposta in output:
            time.sleep(tempo_di_attesa)
            if risposta == "Immagine":
                if domanda == limite:
                    done_ok_text = f"All questions answered"
                    print(f"{Fore.GREEN}{Style.BRIGHT}{done_text} {Fore.WHITE}{done_ok_text}")
                else:
                    domanda += 1      
                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click() 
            elif risposta == "1": 
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer0")]')
                    scelta.click()
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}")
                    done_ok_text = f"All questions answered" 
                    print(f"{Fore.GREEN}{Style.BRIGHT}{done_text} {Fore.WHITE}{done_ok_text}")
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer0")]')
                    scelta.click()  
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}")
                    domanda += 1 
                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()                
            elif risposta == "2":
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer1")]')
                    scelta.click()
                    done_ok_text = f"All questions answered"
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}")
                    print(f"{Fore.GREEN}{Style.BRIGHT}{done_text} {Fore.WHITE}{done_ok_text}") 
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer1")]')
                    scelta.click()  
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}")
                    domanda += 1 
                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()                
            elif risposta == "3":
                if domanda == limite:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer2")]')
                    scelta.click()
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}") 
                    done_ok_text = f"All questions answered"
                    print(f"{Fore.GREEN}{Style.BRIGHT}{done_text} {Fore.WHITE}{done_ok_text}")
                else:
                    scelta=driver.find_element(by=By.XPATH,value='//input[contains(@id, "answer2")]')
                    scelta.click()  
                    answer_ok_text = f"Question {domanda+1}"
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{answer_text} {Fore.WHITE}{answer_ok_text}")
                    domanda += 1 
                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()
            else:
                if domanda == limite:
                    pass
                else:
                    error_msg = f"Error while answering question {domanda+1}"
                    print(f"{Fore.RED}{Style.BRIGHT}{error} {Fore.WHITE}{error_msg}")
                    domanda += 1 
                    continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
                    continua.click()   

def main(domande, risposte, quante_domande, tempo_di_attesa):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", config.LOCAL_HOST)
    if config.OS == 'WINDOWS':
        service = Service(config.CHROME_DRIVER_PATH_WINDOWS)
    elif config.OS == 'UNIX':
        service = Service(config.CHROME_DRIVER_PATH_UNIX)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    if domande == True:
        get_questions(driver, quante_domande, tempo_di_attesa)
    if risposte == True:
        rispondi(driver, quante_domande, tempo_di_attesa)