# seleniumTesting
## Prerequisites

Before you can start performing **Python** automation testing with **Selenium**, you would need to:

* Install the latest Python build from the [official website](https://www.python.org/downloads/). We recommend using the latest version.
* Make sure **pip** is installed in your system. You can install **pip** from [here](https://pip.pypa.io/en/stable/installation/).
### Installing Selenium Dependencies And Tutorial Repo

**Step 1:** Clone the LambdaTest’s python-selenium-sample repository and navigate to the code directory as shown below:

```bash
git clone https://github.com/LambdaTest/python-selenium-sample
cd webdriver
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
```

**Step 4:** Create file .env.

Copy file .env.sample to .env and fill value to variables

## Run Your First Test
```bash
python main.py
(or python3 main.py)
```
