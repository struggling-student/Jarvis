import base64
import json
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def get_data_new(driver,directory_finale):
    esame = { x:{} for x in range(10)}

    questions = driver.find_elements(by=By.XPATH, value='//div[@class="qtext"]')
    directory = f"Foto"
    os.mkdir(directory)
    for i, question in enumerate(questions):
        if len(question.find_elements(by=By.TAG_NAME, value="img")) > 0:
            file_name = f"Foto/answer_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(question.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            with open(file_name, mode='rb') as old_file:
                img = old_file.read()
            esame[i]["domanda-immagine"] = base64.encodebytes(img).decode('utf-8')
            esame[i]["domanda"] = question.text
        else:
            esame[i]["domanda"] = question.text
    shutil.rmtree(directory)

    domande = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
    contatore = 0
    numero = 0
    directory = f"Foto"
    os.mkdir(directory)
    risposte = []
    for domanda in domande:
        if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
            contatore +=1
            file_name = f"Foto/answer_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(domanda.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            with open(file_name, mode='rb') as old_file:
                img = old_file.read()
            risposte.append(base64.encodebytes(img).decode('utf-8'))
        else:
            contatore+=1
            risposte.append(domanda.text)
        if contatore == 3:
            esame[numero]["scelte"] = risposte
            numero += 1
            contatore = 0
            risposte = []
    shutil.rmtree(directory)
    
    risposte = driver.find_elements(by=By.XPATH, value='//div[@class="rightanswer"]')
    directory = f"Foto"
    os.mkdir(directory)
    for i,risposta in enumerate(risposte):
        if len(risposta.find_elements(by=By.TAG_NAME, value="img")) > 0:
            file_name = f"Foto/answer_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(risposta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            with open(file_name, mode='rb') as old_file:
                img = old_file.read()
            esame[i]["risposta-immagine"] = base64.encodebytes(img).decode('utf-8')
        else:
            esame[i]["risposta"] = risposta.text
    shutil.rmtree(directory)

    now = datetime.now()
    file_name = now.strftime("%H:%M:%S")
    t = f"{file_name}.json"
    file_json = directory_finale + "/" + t
    with open(file_json, mode='w') as file:
        json.dump(esame, file, indent=4)

def start_new_exam(driver, course_link, exam_link,i, directory, value):
    for i in range(value):
        driver.get(course_link)
        driver.get(exam_link)
                
        time.sleep(3)
        tentativo=driver.find_element(by=By.CSS_SELECTOR, value="[type='submit']")
        tentativo.click()

        time.sleep(3)
        avvia=driver.find_element(by=By.XPATH, value='//input[@id="id_submitbutton"]')
        avvia.click()

        time.sleep(3)
        termina=driver.find_element(by=By.XPATH, value='//a[@class="endtestlink aalink"]')
        termina.click()

        time.sleep(3)
        invia=driver.find_element(by=By.XPATH, value="//button[text()='Submit all and finish']")
        invia.click()

        time.sleep(3)
        confirm=driver.find_element(by=By.XPATH,value='//input[@value="Submit all and finish"]')
        confirm.click()

        time.sleep(3)
        get_data_new(driver,i, directory)
    
def login(driver, course_link, exam_link, i, directory, value):
    driver.get('https://elearning.uniroma1.it/auth/mtsaml/')
    username = driver.find_element(by=By.NAME, value="j_username")
    password = driver.find_element(by=By.NAME, value="j_password")
    username.send_keys()
    password.send_keys()
    login_button = driver.find_element(by=By.NAME, value="_eventId_proceed")
    login_button.click()
    start_new_exam(driver, course_link, exam_link, i, directory, value)

def main(link):
    directory = "/Users/lucian/Documents/GitHub/ExamScraper/sample_test_data"
    service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
    course_link = "https://elearning.uniroma1.it/course/view.php?id=11834" 
    driver = webdriver.Chrome(service=service)
    value = 5
    time.sleep(5)
    login(driver, course_link, link, 0, directory, value)
    pass

if __name__ == '__main__':
    link = "https://elearning.uniroma1.it/mod/quiz/view.php?id=362243"
    main(link)
    pass