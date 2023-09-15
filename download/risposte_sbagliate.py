from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from datetime import datetime
import os
import config
from PIL import Image
import base64
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
            with open(immagine, 'wb') as f:
                imgurl = question.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                if imgurl.startswith("data:image"):
                    imgurl = imgurl.split(",")[1]
                    f.write(base64.urlsafe_b64decode(imgurl)) 
                    im = Image.open(immagine)
                    fill_color = (255, 255, 255)
                    im = im.convert("RGBA")   # it had mode P after DL it from OP
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1]) # omit transparency
                        im = background
                    im.convert("RGB").save(immagine, 'PNG')
                else:
                    f.write(get_image(driver, imgurl)) 
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
            with open(immagine, 'wb') as f:
                imgurl = scelta.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                if imgurl.startswith("data:image"):
                    imgurl = imgurl.split(",")[1]
                    f.write(base64.urlsafe_b64decode(imgurl)) 
                    im = Image.open(immagine)
                    fill_color = (255, 255, 255)
                    im = im.convert("RGBA")   # it had mode P after DL it from OP
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1]) # omit transparency
                        im = background
                    im.convert("RGB").save(immagine, 'PNG')
                else:
                    f.write(get_image(driver, imgurl)) 
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
            with open(immagine, 'wb') as f:
                imgurl = risposta.find_element(by=By.TAG_NAME, value="img").get_attribute('src')
                if imgurl.startswith("data:image"):
                    imgurl = imgurl.split(",")[1]
                    f.write(base64.urlsafe_b64decode(imgurl)) 
                    im = Image.open(immagine)
                    fill_color = (255, 255, 255)
                    im = im.convert("RGBA")   # it had mode P after DL it from OP
                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1]) # omit transparency
                        im = background
                    im.convert("RGB").save(immagine, 'PNG')
                else:
                    f.write(get_image(driver, imgurl)) 
    else:
        testo = f'./esami/Exam_{file_name}/Questions/Question_{valore}/Answer/answer_{valore}.txt'
        with open(testo, 'w') as file:
                file.write(risposta.text)  