from datetime import datetime
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import json
import base64

'''
Get all the data from the exam page.
NOTE: this function is not used anymore, but it's still here for reference. You can use it if you want to download the exams via txt files.
'''

def get_data_files(driver,x):
    directory = f"Exam_{x}"
    os.mkdir(directory)
    directory = f"Exam_{x}/Questions"
    os.mkdir(directory)
        
    for i in range(50):
        directory = f"Exam_{x}/Questions/Question_{i}"
        os.mkdir(directory)
        directory = f"Exam_{x}/Questions/Question_{i}/Choices"
        os.mkdir(directory)

    questions = driver.find_elements(by=By.XPATH, value='//div[@class="qtext"]')
    for i, question in enumerate(questions):
        directory = f"Exam_{x}/Questions/Question_{i}/Question"
        os.mkdir(directory)
        if len(question.find_elements(by=By.TAG_NAME, value="img")) > 0:
            file_name = f"Exam_{x}/Questions/Question_{i}/Question/question_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(question.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            file_name = f"Exam_{x}/Questions/Question_{i}/Question/question_{i}.txt"
            with open(file_name, 'w') as file:
                file.write(question.text)
        else:
            file_name = f"Exam_{x}/Questions/Question_{i}/Question/question_{i}.txt"
            with open(file_name, 'w') as file:
                file.write(question.text)

    domande = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
    contatore = 0
    numero = 0
    for domanda in domande:
        if contatore == 3:
            contatore = 0
            numero += 1
        if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
            contatore +=1
            file_name = f"Exam_{x}/Questions/Question_{numero}/Choices/choice_{contatore}.png"
            with open(file_name, 'wb') as file:
                file.write(domanda.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
        else:
            contatore+=1
            file_name = f"Exam_{x}/Questions/Question_{numero}/Choices/choice_{contatore}.txt"
            with open(file_name, 'w') as file:
                file.write(domanda.text)

    risposte = driver.find_elements(by=By.XPATH, value='//div[@class="rightanswer"]')
    for i,risposta in enumerate(risposte):
        directory = f"Exam_{x}/Questions/Question_{i}/Answer"
        os.mkdir(directory)
        if len(risposta.find_elements(by=By.TAG_NAME, value="img")) > 0:
            file_name = f"Exam_{x}/Questions/Question_{i}/Answer/answer_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(risposta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
        else:
            file_name = f"Exam_{x}/Questions/Question_{i}/Answer/answer_{i}.txt"
            with open(file_name, 'w') as file:
                file.write(risposta.text)  

'''
Get all the data from the exam page.
NOTE: this function is not used anymore, but it's still here for reference.
'''

def get_data_new(driver, directory_finale):
    esame = { x:{} for x in range(50)}

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

'''
Start a new exam. It's the same function of review_old_exam() but it starts the exam.
'''

def start_new_exam(driver, course_link, exams, directory):
    for link in exams:
        print(link)
        driver.get(course_link)
        driver.get(link)
                
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
        visualizza=driver.find_element("link text","Show all questions on one page")
        visualizza.click()

        time.sleep(3)
        get_data_new(driver,directory)

'''
Review the old exams. It's the same function of start_new_exam() but it doesn't start the exam.
'''

def review_old_exam(driver, course_link, exam_link,i):
    driver.get(course_link)
    driver.get(exam_link)
    time.sleep(3)
    visualizza=driver.find_element("link text","Review")
    visualizza.click()
    time.sleep(3)
    domande=driver.find_element("link text", "Show all questions on one page")
    domande.click()
    time.sleep(3)
    get_data_new(driver,i)

'''
Login function for the elearning website. After login it starts scraping the exams inside the exams.txt file.
NOTE: Insert your username and password in the send_keys() function.
'''

def login(driver, course_link, exams,directory):
    driver.get('https://elearning.uniroma1.it/auth/mtsaml/')
    username = driver.find_element(by=By.NAME, value="j_username")
    password = driver.find_element(by=By.NAME, value="j_password")
    username.send_keys("")
    password.send_keys("")
    login_button = driver.find_element(by=By.NAME, value="_eventId_proceed")
    login_button.click()
    start_new_exam(driver, course_link, exams, directory)

''' 
Main function of the program for running the scraper.
NOTE : The path to the chromedriver must be changed to the path of the chromedriver on your computer.
'''

def main(exams):
    directory = "/Users/lucian/Documents/GitHub/ExamScraper/exams_data"
    service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
    course_link = "https://elearning.uniroma1.it/course/view.php?id=11834" 
    driver = webdriver.Chrome(service=service)
    time.sleep(5)
    login(driver, course_link, exams, directory)

if __name__ == "__main__":
    exams = [
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=529645",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=444693",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=448926",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=470022",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=482897",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=487620",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=489901",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=511326",
        #! 40 domande con pagina full
        #"https://elearning.uniroma1.it/mod/quiz/view.php?id=429255",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=412503",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=408285",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=406112",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=385932",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=529645",
        "https://elearning.uniroma1.it/mod/quiz/view.php?id=533412",
    ]
    main(exams)
    pass