import os 
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

chrome_driver_location = os.getenv('CHROME_DRIVER_LOCATION')
luma_website = os.getenv('LUMA_WEBSITE')
os.environ['PATH'] += chrome_driver_location

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")