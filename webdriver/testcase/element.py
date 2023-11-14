from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class BasePageElement(object):
    
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.NAME, self.locator)
        )
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")
    
class BaseInputElement(object):
    def __init__(self, locator):
        self.locator = locator
    
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.ID, self.locator)
        )
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