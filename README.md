# Jarvis - Automated tool for answering questions
> Jarvis is a tool made with Selenium and Python that has the ability to answers questions of a given exam. Also it can be used to download data from each exam and store it for later use.

> **Warning**
> Jarvis currently only works on UNIX based systems. Windows support is not yet available. Please open a pull request if you want to contribute to this project by adding Windows support or any other feature. 

https://user-images.githubusercontent.com/32139751/236615814-bd5a4d6c-01e9-4a33-82d2-0b6576fe8151.mov

## Installation 
> **Note**
> This is a note

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
Install the webdriver for Google Chrome. You can download it from [here](https://chromedriver.chromium.org/downloads). Make sure to download the correct version for your Google Chrome browser. Once you have downloaded the webdriver, move it to a directory to your liking. Then you have to add teh path of the webdriver inside some of the files in the project. The files are:
- `jarvis.py`
- `data_scraper.py`
- `data_scraper.py`

Here an example of how to add the path of the webdriver to the `jarvis.py` file:
```python   
# Path to the webdriver
PATH = "/home/username/Downloads/chromedriver"
```
### Google Chrome 
In order for Jarvis to work properly you have to start Google Chrome with the following command:
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="~/chrome-profile"
```
This will start Google Chrome with remote debugging enabled. This is needed for Jarvis to be able to interact with the browser. If the brower starts then you are good to go. If you get an error message saying that the port is already in use, then you have to change the port number. You can do so by changing the number after the `--remote-debugging-port=` flag.
You can close the browser once you have started it by manually closing it or by closing the process in the terminal by pressing `CTRL + C`.

> **Note**
> Now you have everything you need to start using Jarvis. The next steps will show you how to use Jarvis and how to scrape data from the exams.
## Usage




## Data scraping 
TODO

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
TODO

## Disclaimer
> **Warning**
> This tool is made for educational purposes only. I am not responsible for how the tool is used. Jarvis is not intended to be used for cheating on exams, but rather used to learn how to use Selenium and Python for web scraping and automation.
### License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details