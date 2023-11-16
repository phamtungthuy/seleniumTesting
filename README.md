# seleniumTesting
## Prerequisites

Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
* Install Chrome driver in https://chromedriver.chromium.org/downloads
* Install Firefox driver in https://github.com/mozilla/geckodriver/releases
### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s python-selenium-sample repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/phamtungthuy/seleniumTesting.git
```

**Step 2:** Create virtual environment:
```bash
virtualenv venv
source ./venv/bin/activate (Linux/MacOs)
source ./venv/Script/active (Window)
```

**Step 3:** Download the driver from the link, or you can use **pip** to install it.
```bash
pip install selenium
pip install python-dotenv
```

## Run Webdriver Selenium Testcases
**Step 1:** Go to direction of Webdriver folder
```bash
cd webdriver
```
**Step 2:** Create file .env.

Copy file .env.sample to .env and fill value to variables

In .env file:
```bash
CHROME_DRIVER_LOCATION= (location of chrome driver in your computer)
LUMA_WEBSITE=https://magento.softwaretestingboard.com/
SAUCEDEMO_WEBSITE=http://www.sauce.demo.com/
FIREFOX_DRIVER_LOCATION= (location of firefox driver in your computer)
```
**Step 3:** Run file main.py
```bash
python main.py
(or python3 main.py)
```


## Run seleniumIDE
**Step 1:** Go to [Selenium IDE](https://chromewebstore.google.com/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd?pli=1)

Click **Add extension**
**Step 2:** Open IDE extension

import seleniumIDE.side from seleniumIDE folder to seleniumIDE extension.
**Step 3:** Run testcases in IDE extension
(It's really easy for almost everyone even though they don't understand deeply programming language

## Run seleniumGRID
### Prerequisities
Before you start seleniumGRID in my project, you need install [Docker](https://docs.docker.com/get-docker/)

After that, you need to install [Docker compose](https://docs.docker.com/compose/install/)
**Step 1:** Go to direction of seleniumGRID folder:
```bash
cd seleniumGRID
```
**Step 2:** Create file .env.

Copy file .env.sample to .env and fill value to variables

In .env file:
```bash
CHROME_DRIVER_LOCATION= (location of chrome driver in your computer)
LUMA_WEBSITE=https://magento.softwaretestingboard.com/
SAUCEDEMO_WEBSITE=http://www.sauce.demo.com/
FIREFOX_DRIVER_LOCATION= (location of firefox driver in your computer)
```
**Step 3:** Run docker-compose file
```bash
docker-compose up
```
If limitation of permissin, you need to run the code below instead
```bash
sudo docker-compose up
```
**Step 4:** Run file main.py
```bash
python main.py
```
or
```bash
python3 main.py
```


