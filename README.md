# Jarvis - Automated tool for answering questions
> Jarvis is a tool made with Selenium and Python that has the ability to answers questions of a given exam. Also it can be used to download data from each exam and store it for later use.

> **Warning**
> Jarvis currently only works on UNIX based systems. Windows support is not yet available. Please open a pull request if you want to contribute to this project by adding Windows support or any other feature. 

https://user-images.githubusercontent.com/32139751/236615814-bd5a4d6c-01e9-4a33-82d2-0b6576fe8151.mov

## Installation 
> **Note**
> Follow the steps below to install everything that is required to run Jarvis. Once you have installed everything you can skip to the [Usage](#usage) section to learn how to use Jarvis.

### Requirements

Activate virtual environment:
```bash
python3 -m venv venv
```
Before you can start installing packages in your virtual environment, you need to activate it. Do so by running the following command:
```bash
source venv/bin/activate
```
You can use the requirements.txt file to install all the dependencies for this project. Run the following command:
```bash
pip install -r requirements.txt
```

### Webdriver
Install the webdriver for Google Chrome. You can download it from [here](https://chromedriver.chromium.org/downloads). Make sure to download the correct version for your Google Chrome browser. Once you have downloaded the webdriver, move it to a directory to your liking. Then you have to add the path of the webdriver inside some of the files in the project. The files are:
- `scarica_rispondi.py`
- `risposte_sbagliate.py`
- `esami.py`
- `sample_test.py`

Here an example of how to add the path of the webdriver to the `scarica_rispondi.py` file:
```python   
# Insert the path of the webdrive inside the Service() class
def main(domande, risposte, quante_domande, tempo_di_attesa):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
    service = Service('/Users/lucian/Documents/driver/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
```
> **Note**
> There will be a better way to add the path of the webdriver in the future. This is just a temporary solution.

### Google Chrome 
In order for Jarvis to work properly you have to start Google Chrome with the following command:
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/chrome-profile"
```
> **Warning**
> Make sure to create a directory called `chrome-profile` in your home directory. If you don't do so, then Google Chrome will not start. You can delete it once you have finished using Jarvis.

This will start Google Chrome with remote debugging enabled. This is needed for Jarvis to be able to interact with the browser. If the brower starts then you are good to go. If you get an error message saying that the port is already in use, then you have to change the port number. You can do so by changing the number after the `--remote-debugging-port=` flag.
You can close the browser once you have started it by manually closing it or by closing the process in the terminal by pressing `CTRL + C`.

> **Note**
> Now you have everything you need to start using Jarvis. The next steps will show you how to use Jarvis and how to scrape data from the exams.
## Usage
Everything you need to know about how to use Jarvis is explained in the following sections. If you have any questions or problems, feel free to open an issue.

### Step 1 - Start Google Chrome
Start Google Chrome with remote debugging enabled. You can do so by running the following command:
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/chrome-profile"
``` 
Google Chrome will start and you will see a message in the terminal saying that the browser is ready to be used. You can close the browser once you have started it by manually closing it or by closing the process in the terminal by pressing `CTRL + C`. 
Once you have started Google Chrome, you have to login to the website where the exam/test is located. You can do so by going to the website and logging in with your credentials. Once you have logged in, you have to go to the exam/test that you want to use Jarvis on. Once you are on the exam/test page, you can follow the next step. 

### Step 2 - Setup Jarvis
First thing before you start everything, run the script for cleaning the directory of any past data, Jarvis can't work if there is past data from a previous exam in the directory. You can do so by running the following command:
```bash
./scripts/clean.sh
```
If the exam/test has 10 or 50 questions, then you have to edit the `main.py` file. You can do so by changing the `quante_domande` variable to the number of questions that the exam/test has. If the exam/test has 10 questions, then you have to change the variable to `quante_domande = 10`. If the exam/test has 50 questions, then you have to change the variable to `quante_domande = 50`.

### Step 3 - Start Jarvis
Now you can start the exam/test. After you started it you can start Jarvis, you can do so by running the following command:
```bash 
python3 main.py
```
Now Jarvis will start and it will first download all the questions, once all the questions are downloaded Jarvis will proceed to answer them. Once Jarvis has finished answering all the questions, it will stop and you will see a message in the terminal saying that Jarvis has finished answering all the questions. 

> **Warning**
> Do not interact in any way with the browser while Jarvis is running. If you do so, Jarvis will not be able to answer the questions. Once everything is done remember to run the ./clean.sh script to clean the directory. 

## Data scraping 
TODO

## Contributing
TODO

## Disclaimer
> **Warning**
> This tool is made for educational purposes only. I am not responsible for how the tool is used. Jarvis is not intended to be used for cheating on exams, but rather used to learn how to use Selenium and Python for web scraping and automation.
### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details