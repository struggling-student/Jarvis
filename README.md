# ExamScraper for Moodle
ExamScraper is a tool to scrape exam questions from the web. It is written in Python 3 and uses the Selenium library to interact with the web browser.

## Installation

ExamScraper requires Python 3.6 or higher. It is recommended to use a virtual environment to install the dependencies.

```bash     
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt
```

## Usage

ExamScraper is a command line tool. It can be run with the following command:

```bash 
$ python exam_scraper.py
```

ExamScraper will ask for the URL of the exam. It will then scrape the exam and save the questions in a file called `questions.txt` in the current directory.

## License
[MIT](https://choosealicense.com/licenses/mit/)
