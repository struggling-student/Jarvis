from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

continua=driver.find_element(by=By.XPATH,value='//span[@class="thispageholder"]')
continua.click()
