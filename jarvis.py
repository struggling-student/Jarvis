#NOTE : Imports, non toccare.
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def main():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
    service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    #creo la directory per salvare le domande
    directory = f"Data"
    os.mkdir(directory)
    #NOTE : Cambiare il range in base al numero di domande
    for i in range(50):
        directory = f'Data/Domanda_{i}'
        os.mkdir(directory)

    #NOTE : Cambiare il range in base al numero di domande
    for i in range(50):
        
        #NOTE: Prende le domande dalla pagina 
        domande = driver.find_elements(by=By.XPATH, value='//div[@class="qtext"]')
        for domanda in domande:
            #NOTE: Se una domanda è un'immagine, allora salva l'immagine
            if len(domanda.find_elements(by=By.TAG_NAME, value="img")) > 0:
                file_name = f"Data/Domanda_{i}/Domanda.png"
                with open(file_name, "wb") as f:
                    f.write(domanda.find_element(by=By.TAG_NAME, value="img").screenshot_as_png) 
            #NOTE: Se una domanda è un testo, allora salva il testo
            else:
                file_name = f"Data/Domanda_{i}/Domanda.txt"
                with open(file_name, "w") as f:
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
                    f.write(scelta.find_element(by=By.TAG_NAME, value="img").screenshot_as_png)
            #NOTE: Se una scelta è un testo, allora salva il testo
            else:
                contatore+=1
                numero+=1
                file_name = f"Data/Domanda_{i}/Scelta_{numero}.txt"
                with open(file_name, "w") as f:
                    f.write(scelta.text)
        

        if i == 49:
            print("Finito")
        else:        
            continua=driver.find_element(by=By.XPATH,value='//input[@value="Next page"]')
            continua.click()
if __name__ == "__main__":
    main()