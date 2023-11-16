import os 
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

firefox_driver_location = os.getenv('FIREFOX_DRIVER_LOCATION')
sauce_website = os.getenv('SAUCEDEMO_WEBSITE')
os.environ['PATH'] += firefox_driver_location

options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")