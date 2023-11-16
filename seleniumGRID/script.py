from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     desired_capabilities=DesiredCapabilities.CHROME.copy()
    
# )/

options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

URL = "https://www.python.org/"

driver.get(url=URL)
print(driver.page_source)