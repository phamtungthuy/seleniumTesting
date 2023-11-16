from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class BasePageElement(object):
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        self.driver = obj.driver
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()

        driver.find_element(By.NAME, self.locator).send_keys(value)

    
class BaseInputElement(object):
    def __init__(self, locator):
        self.locator = locator
    
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.ID, self.locator)
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", driver.find_element(By.ID, self.locator))
        driver.find_element(By.ID, self.locator).clear()
        driver.find_element(By.ID, self.locator).send_keys(value)

class BaseSelectElement(object):
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver : driver.find_element(By.ID, self.locator)
        )
        Select(driver.find_element(By.ID, self.locator)).select_by_visible_text(value)

class BaseSearchElement(object):
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        self.driver = obj.driver
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def search(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        self.driver.find_element(By.NAME, self.locator).send_keys(Keys.ENTER)