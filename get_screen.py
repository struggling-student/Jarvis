from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os


def saveimg(url):
    browser = webdriver.Chrome()
    browser.get(url)
    #aspetta un po' che la pagina si carichi
    time.sleep(1)
    browser.find_element(by=By.TAG_NAME, value="img").screenshot('image.png')
    #browser.save_screenshot('image.png')
    browser.close()

def run_screen():
    #cancello l'immagine
    try:
        os.remove('image.png')
    except:
        pass
    url =''
    fp = open('url.txt', 'r')
    #se il file non è vuoto
    for line in fp:
        if line != '':
            url = line
            saveimg(url)
            break
