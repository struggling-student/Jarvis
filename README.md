# Jarvis - Automated tool for answering questions
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![opencv](https://img.shields.io/badge/opencv-%230C55A5.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) 
![macOS](https://img.shields.io/badge/mac%20os-white?style=for-the-badge&logo=macos&logoColor=black)

> Jarvis is a tool made with Selenium and Python that has the ability to answer questions of a Quiz on the Moodle website. If there are any new questions, Jarvis is able to download them and store them for use in a new quiz.

https://user-images.githubusercontent.com/32139751/236615814-bd5a4d6c-01e9-4a33-82d2-0b6576fe8151.mov

## :pushpin: Installation 
> **Note**
> Follow the steps below to install everything that is required to run Jarvis. Once you have installed everything you can skip to the [Usage](#usage) section to learn how to use Jarvis.

### Requirements
Once you have cloned the repository, you will need to follow the steps below to install everything that is required to run Jarvis.

#### Step 1 - Install dependencies 
You can use the requirements.txt file to install all the dependencies for this project. Run the following command:
```bash
pip install -r requirements.txt
```
#### Step 2 - Install ChromeDriver
You can download the ChromeDriver from the following [link](https://chromedriver.chromium.org/downloads) make sure to download the version that matches your Chrome browser version. Once you have downloaded the ChromeDriver, extract the file and move it to the Jarvis directory.

## :unlock: Usage
> **Note**
> This part is divided into two sections. The first section is for Unix users and the second section is for Windows users. Follow the steps for your operating system to learn how to use Jarvis.
### :orange_book: How to use Jarvis - Unix 
This part is only for Unix users (MacOS and Linux). If you are a Windows user, you can skip this part and go to the [How to use Jarvis - Windows](#how-to-use-jarvis---windows) section.
#### Step 1 - Start Google Chrome in remote debugging mode
You will need to start Google Chrome in remote debugging mode. To do this, you have to find the path to the Google Chrome executable file. You can do this by running the following command:
```bash
which google-chrome-stable
```
Once you have the path to the Google Chrome executable file, you will need to specify a user data directory. This is where Google Chrome will store all the data. You can create one wherever you want. For example, you can create a directory called "chrome-data" in the Jarvis directory. Once you have created the directory, you can run the following command to start Google Chrome in remote debugging mode:

```bash
CHROME_EXECUTABLE_PATH  --remote-debugging-port=9222 --user-data-dir="PATH_TO_USER_DATA_DIRECTORY"
```
After running the command, a Google Chrome window should open. This window will be used by Jarvis to perform the actions. **Do not close this window**.

Now that you have started Google Chrome in remote debugging mode, you can run Jarvis, but first you have to do some configuration.
#### Step 2 - Configure Jarvis
Open the config.py file and change the following variables:
```python
# This variable is used to determine which operating system you are using. 
OS = "UNIX"
# NOTE: We are using port 9222 because that is the port that we used to start Google Chrome in remote debugging mode. If you are using a different port, make sure to change it here as well.
LOCAL_HOST = 'localhost:9222'
# NOTE: You will need to change the path to the ChromeDriver that you downloaded in the installation section. 
CHROME_DRIVER_PATH_UNIX = '/Users/lucian/Documents/driver/chromedriver'
# NOTE: Do not youch the CHROME_DRIVER_PATH_WINDOWS variable.
```
Once you have changed the variables, Jarvis is suited for your system.
#### Step 3 - Start using Jarvis
Now that you have configured Jarvis, you can start using it. Login to your Moodle account by using the Google Chrome window that you opened in step 1. Once you have logged in, you can choose a quiz that you want Jarvis to answer. Once you have chosen a quiz, you have to edit the main.py file. You will need to change the following variables:
```python
# per il time.sleep() ovvero quanti secondi vuoi che aspetta tra un'operazione e l'altra
tempo_di_attesa = 0
# NOTE: You will need to change this variable base on the number of questions that are in the quiz. For example, if there are 50 questions in the quiz, you will need to change this variable to 50.
quante_domande = 50
```
Once you have changed the variables, you can run the main.py file. By doing so, Jarvis will start answering the questions, **make sure that after you run the main.py file, you jump back to the Google Chrome window that you opened in step 1**. Jarvis will start downloading first the questions and then will proceed to answer them. Do not worry if it takes some seconds for Jarvis to start answering the questions, it is normal since the process to find all the answers may take some time.

Once Jarvis has finished answering the questions, and you want to use Jarvis to answer a new quiz, you will need to delete the questions that Jarvis downloaded. You can do this by manually deleting the Data directory that has been created or by running the following command:
```bash
./scripts/clean.sh
```
After you have deleted the previous questions, you can run the main.py file again and Jarvis will start answering the questions of the new quiz.

### :green_book: How to use Jarvis - Windows
This part is only for Windows users. If you are a Unix user (MacOS and Linux), you can skip this part and go to the [How to use Jarvis - Unix](#how-to-use-jarvis---unix) section.
#### Step 1 - Start Google Chrome in remote debugging mode
You will need to start Google Chrome in remote debugging mode. To do this, you have to find the path to the Google Chrome executable file. You can do this by taking a look at this [link](https://techdows.com/2009/02/how-to-find-location-of-google-chrome.html). 

Once you have the path to the Google Chrome executable file, you will need to specify a user data directory. This is where Google Chrome will store all the data. You can create one wherever you want. For example, you can create a directory called "chrome-data" in the Jarvis directory. Once you have created the directory, you can run the following command to start Google Chrome in remote debugging mode:

```bash
"CHROME_EXECUTABLE_PATH"  --remote-debugging-port=9222 --user-data-dir="PATH_TO_USER_DATA_DIRECTORY"
```
> **Note**
> You can also use the bat file (chrome.bat) inside the scripts directory to start Google Chrome in remote debugging mode. You will need to change the path to the Google Chrome executable file and the path to the user data directory for it to work properly.

After running the command, a Google Chrome window should open. This window will be used by Jarvis to perform the actions. **Do not close this window**.

Now that you have started Google Chrome in remote debugging mode, you can run Jarvis, but first you have to do some configuration.
#### Step 2 - Configure Jarvis
Open the config.py file and change the following variables:
```python
# This variable is used to determine which operating system you are using. 
OS = "WINDOWS"
# NOTE: We are using port 9222 because that is the port that we used to start Google Chrome in remote debugging mode. If you are using a different port, make sure to change it here as well.
LOCAL_HOST = 'localhost:9222'
# NOTE: You will need to change the path to the ChromeDriver that you downloaded in the installation section. 
CHROME_DRIVER_PATH_WINDOWS = r"C:\chromedriver\chromedriver.exe"
# NOTE: Do not youch the CHROME_DRIVER_PATH_UNIX variable.
```
Once you have changed the variables, Jarvis is suited for your system.
#### Step 3 - Start using Jarvis
Now that you have configured Jarvis, you can start using it. Login to your Moodle account by using the Google Chrome window that you opened in step 1. Once you have logged in, you can choose a quiz that you want Jarvis to answer. Once you have chosen a quiz, you have to edit the main.py file. You will need to change the following variables:
```python
# per il time.sleep() ovvero quanti secondi vuoi che aspetta tra un'operazione e l'altra
tempo_di_attesa = 0
# NOTE: You will need to change this variable base on the number of questions that are in the quiz. For example, if there are 50 questions in the quiz, you will need to change this variable to 50.
quante_domande = 50
```
Once you have changed the variables, you can run the main.py file. By doing so, Jarvis will start answering the questions, **make sure that after you run the main.py file, you jump back to the Google Chrome window that you opened in step 1**. Jarvis will start downloading first the questions and then will proceed to answer them. Do not worry if it takes some seconds for Jarvis to start answering the questions, it is normal since the process to find all the answers may take some time.

Once Jarvis has finished answering the questions, and you want to use Jarvis to answer a new quiz, you will need to delete the questions that Jarvis downloaded. You can do this by manually deleting the Data directory that has been created or by running the following command:
```bash
./scripts/clean.bat
```
After you have deleted the previous questions, you can run the main.py file again and Jarvis will start answering the questions of the new quiz.

## :mortar_board: Contributing
Thank you for considering contributing to Jarvis! If you would like to contribute, feel free to open a pull request. If you have any questions, feel free to open an issue.

I would like to thank the following people for their contributions:
- [Davide](https://github.com/davidebelcastro-sig)
    - Added the whole search engine for searching the right answers to the questions.
- [Ryho](https://github.com/ryyhho)
    - Added Windows support to Jarvis.    

## :loudspeaker: Disclaimer
> **Warning**
> This tool is made for educational purposes only. I am not responsible for how the tool is used. Jarvis is not intended to be used for cheating on exams, but rather used to learn how to use Selenium and Python for web scraping and automation.

## :scroll: License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
