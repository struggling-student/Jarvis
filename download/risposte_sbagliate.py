from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import config
from datetime import datetime
import os


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", config.LOCAL_HOST)
if config.OS == 'WINDOWS':
    service = Service(config.CHROME_DRIVER_PATH_WINDOWS)
elif config.OS == 'UNIX':
    service = Service(config.CHROME_DRIVER_PATH_UNIX)
driver = webdriver.Chrome(service=service, options=chrome_options)


links = [x.get_attribute('href') for x in driver.find_elements(by=By.XPATH,value='//a[contains(@class, "notanswered")]')]

now = datetime.now()
file_name = now.strftime("%H:%M:%S")

directory = f'./esami/Exam_{file_name}'
os.mkdir(directory)
directory = f'./esami/Exam_{file_name}/Questions'
os.mkdir(directory)

for valore,link in enumerate(links):
    driver.get(link)
    question = driver.find_element(by=By.XPATH, value='//div[@class="qtext"]')
    directory = f'./esami/Exam_{file_name}/Questions/Question_{valore}'
    os.mkdir(directory)
    directory = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Question'
    os.mkdir(directory)

    if len(question.find_elements(by=By.TAG_NAME, value="img")) > 0:
            immagine = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Question/question_{valore}.png'
            with open(immagine, 'wb') as file:
                file.write(question.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            testo = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Question/question_{valore}.txt'
            with open(testo, 'w') as file:
                file.write(question.text)
    else:
        testo= f'./esami/Exam_{file_name}/Questions/Question_{valore}/Question/question_{valore}.txt'
        with open(testo, 'w') as file:
            file.write(question.text)
            
    directory = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Choices'
    os.mkdir(directory)
    scelte = driver.find_elements(by=By.XPATH, value='//div[@class="answer"]//div[@class="d-flex w-100"]')
    contatore = 0
    numero = 0
    for scelta in scelte:
        if contatore == 3:
            contatore = 0
            numero += 1
        if len(scelta.find_elements(by=By.TAG_NAME, value="img")) > 0:
            contatore +=1
            immagine = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Choices/choice_{contatore}.png'
            with open(immagine, 'wb') as file:
                file.write(scelta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
        else:
            contatore+=1
            testo = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Choices/choice_{contatore}.txt'
            with open(testo, 'w') as file:
                file.write(scelta.text)

    risposta = driver.find_element(by=By.XPATH, value='//div[@class="rightanswer"]')
    directory = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Answer'
    os.mkdir(directory)
    if len(risposta.find_elements(by=By.TAG_NAME, value="img")) > 0:
            immagine = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Answer/answer_{valore}.png'
            with open(immagine, 'wb') as file:
                file.write(risposta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
    else:
        testo = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Answer/answer_{valore}.txt'
        with open(testo, 'w') as file:
                file.write(risposta.text)  