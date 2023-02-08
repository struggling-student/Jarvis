import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

'''
Start the sample test.
NOTE: This function needs to be implemented.
'''
def start_sample_test():
    pass
'''
Get all the data from the exam page.
'''
def get_data(driver,x):
    # Create the exam directory
    directory = f"Exam_{x}"
    os.mkdir(directory)
    directory = f"Exam_{x}/Questions"
    os.mkdir(directory)

    # Create the directories
    for i in range(50):
        directory = f"Exam_{x}/Questions/Question_{i}"
        os.mkdir(directory)
        directory = f"Exam_{x}/Questions/Question_{i}/Choices"
        os.mkdir(directory)

    # Get all the questions
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

    # Get the choices
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
        
    # Get the right answers
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
Start a new exam. It's the same function of review_old_exam() but it starts the exam.
'''
def start_new_exam(driver, course_link, exam_link,i):
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
    visualizza=driver.find_element("link text","Show all questions on one page")
    visualizza.click()

    time.sleep(3)
    get_data(driver,i)
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
    get_data(driver,i)
'''
Login function for the elearning website. After login it starts scraping the exams inside the exams.txt file.
NOTE: Insert your username and password in the send_keys() function.
'''
def login(driver):
    # Login inside the website
    driver.get('https://elearning.uniroma1.it/auth/mtsaml/')
    username = driver.find_element(by=By.NAME, value="j_username")
    password = driver.find_element(by=By.NAME, value="j_password")
    username.send_keys()
    password.send_keys()
    login_button = driver.find_element(by=By.NAME, value="_eventId_proceed")
    login_button.click()
    course_link = "https://elearning.uniroma1.it/course/view.php?id=11834" 
    # Get all the exams links and either start a new exam or review an old one.
    with open("exams.txt", "r") as file:
        for i,line in enumerate(file):
            exam_link = line.strip()
            # Start a new exam and scrape the data
            time.sleep(10)
            start_new_exam(driver, course_link, exam_link, i)
            print("Exam at linl " + exam_link + " scraped.")
            # Review an old exam and scrape the data
            # review_old_exam(driver, course_link, exam_link, i)
    # open the folder with the exams and iterate over the files and open them

''' 
Main function of the program for running the scraper.
NOTE : The path to the chromedriver must be changed to the path of the chromedriver on your computer.
'''
def main():
    service = Service('/Users/lucian/Documents/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=service)
    login(driver) 
# Run the main function
if __name__ == "__main__":
    main()