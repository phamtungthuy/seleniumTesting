from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass

class LumaMainPageLocators(object):
    SIGNUP_LINK = (By.LINK_TEXT, "Create an Account")
    LOGIN_LINK = (By.CSS_SELECTOR, ".authorization-link a")

class LumaSignupPageLocators(object):
    SIGNUP_BUTTON = (By.CLASS_NAME, "submit")

class LumaLoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#send2.login")