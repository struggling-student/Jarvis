from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import datetime

def active_exam(driver):
    driver.get("https://elearning.uniroma1.it/course/view.php?id=11834")
    driver.get("https://elearning.uniroma1.it/mod/quiz/view.php?id=511326")

    time.sleep(2)
    tentativo=driver.find_element(by=By.CSS_SELECTOR, value="[type='submit']")
    tentativo.click()

    time.sleep(2)
    avvia=driver.find_element(by=By.NAME, value="submitbutton")
    avvia.click()

    time.sleep(2)
    termina=driver.find_element(by=By.XPATH, value='//a[@class="endtestlink aalink"]')
    termina.click()

    time.sleep(2)
    invia=driver.find_element(by=By.XPATH, value="//button[@class='btn btn-secondary'][.='Invia e termina']")
    invia.click()

    time.sleep(2)
    confirm=driver.find_element(by=By.XPATH,value='//input[@value="Invia e termina"]')
    confirm.click()

    time.sleep(2)
    visualizza=driver.find_element("link text","Visualizza tutte le domande nella stessa pagina")
    visualizza.click()
def new_exam(driver):
    driver.get("https://elearning.uniroma1.it/course/view.php?id=11834")
    driver.get("https://elearning.uniroma1.it/mod/quiz/view.php?id=511326")
    time.sleep(3)
    visualizza=driver.find_element("link text","Review")
    visualizza.click()
    time.sleep(3)
    domande=driver.find_element("link text", "Show all questions on one page")
    domande.click()
    time.sleep(3)
    #! get the exam name and create the folder for it
    title = driver.find_element(by=By.XPATH, value='//a[@title="Quiz"]')
    date_string = title.text
    date_format = "%Y-%m-%d"
    start = date_string.find("DEL") + 4
    end = date_string.find("- TEST")
    date_str = date_string[start:end].strip()
    date_object = datetime.datetime.strptime(date_str, date_format)
    date_object = date_object.strftime("%d-%m-%Y")
    os.mkdir(date_object)
    os.chdir(date_object)
    os.mkdir("Domande")
    #! get all the questions
    questions = driver.find_elements(by=By.XPATH, value='//div[@class="que multichoice deferredfeedback notanswered"]')
    
    for i, question in enumerate(questions):
        directory = f"Domande/Domanda_{i}"
        os.mkdir(directory)
        directory = f"Domande/Domanda_{i}/Scelte"
        os.mkdir(directory)


    #? Get all the possible answers for a questions
    domande = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
    contatore = 0
    numero = 0
    for domanda in domande:
        if contatore == 3:
            contatore = 0
            numero += 1
        if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
            contatore +=1
            file_name = f"Domande/Domanda_{numero}/Scelte/question_{contatore}.png"
            with open(file_name, 'wb') as file:
                file.write(domanda.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
        else:
            contatore+=1
            file_name = f"Domande/Domanda_{numero}/Scelte/question_{contatore}.txt"
            with open(file_name, 'w') as file:
                file.write(domanda.text)
        
    #? Get all the correct answers
    risposte = driver.find_elements(by=By.XPATH, value='//div[@class="rightanswer"]')
    for i,risposta in enumerate(risposte):
        directory = f"Domande/Domanda_{i}/Risposta"
        os.mkdir(directory)
        if len(risposta.find_elements(by=By.TAG_NAME, value="img")) > 0:
            file_name = f"Domande/Domanda_{i}/Risposta/answer_{i}.png"
            with open(file_name, 'wb') as file:
                file.write(risposta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
        else:
            file_name = f"Domande/Domanda_{i}/Risposta/answer_{i}.txt"
            with open(file_name, 'w') as file:
                file.write(risposta.text)   

def login(driver):
    driver.get('https://elearning.uniroma1.it/auth/mtsaml/')
    username = driver.find_element(by=By.NAME, value="j_username")
    password = driver.find_element(by=By.NAME, value="j_password")
    username.send_keys("")
    password.send_keys("")
    login_button = driver.find_element(by=By.NAME, value="_eventId_proceed")
    login_button.click()
    #active_exam(driver)
    new_exam(driver)

def main():
    service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=service)
    login(driver) 

if __name__ == "__main__":
    main()