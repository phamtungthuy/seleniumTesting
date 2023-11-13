from testcase.locator import *
from testcase.element import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
class LumaMainPage(BasePage):
    
    def go_to_signup_page(self):
        element = self.driver.find_element(*LumaMainPageLocators.SIGNUP_LINK)
        element.click()
    
    def go_to_login_page(self):
        element = self.driver.find_element(*LumaMainPageLocators.LOGIN_LINK)
        element.click()

    def is_title_matches(self):
        return "Home Page" in self.driver.title
    
class LumaSignupPage(BasePage):
    firstName = BaseInputElement("firstname")
    lastName = BaseInputElement("lastname")
    emailAddress = BaseInputElement("email_address")
    password = BaseInputElement("password")
    confirmPassword = BaseInputElement("password-confirmation")

    def create_account(self):
        signupButton = self.driver.find_element(*LumaSignupPageLocators.SIGNUP_BUTTON)
        signupButton.click()

    def is_created_successfully(self):
        if "Create New Customer Account" not in self.driver.title:
            return True
        error_messages = ["Please enter the same value again.", "This is a required field.", "Please enter a valid email address", "message-error"]
        return all(error_message not in self.driver.page_source for error_message in error_messages)
    
class LumaLoginPage(BasePage):
    emailAddress = BaseInputElement("email")
    password = BaseInputElement("pass")

    def login(self):
        loginButton = self.driver.find_element(*LumaLoginPageLocators.LOGIN_BUTTON)
        loginButton.click()

    def is_login_successful(self):
        if "Customer Login" not in self.driver.title:
            return True
        error_messages = ["message-error", "This is a required field.", "Please enter a valid email address"]
        return all(error_message not in self.driver.page_source for error_message in error_messages)
    