from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")

class SearchResultsPageLocators(object):
    pass

class LumaMainPageLocators(object):
    SIGNUP_LINK = (By.LINK_TEXT, "Create an Account")
    LOGIN_LINK = (By.CSS_SELECTOR, ".authorization-link a")
    SWITCH_BUTTON = (By.CLASS_NAME, "switch")
    ACCOUNT_LINK = (By.LINK_TEXT, "My Account")

class LumaSignupPageLocators(object):
    SIGNUP_BUTTON = (By.CLASS_NAME, "submit")

class LumaLoginPageLocators(object):
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#send2.login")

class LumaAccountPageLocators(object):
    EDIT_ADDRESS = (By.LINK_TEXT, "Edit Address")
    EDIT_INFORMATION = (By.CSS_SELECTOR, ".box-information .box-actions .edit")
    MANAGE_ADDRESS = (By.CSS_SELECTOR, ".items .item:nth-child(6)")

class LumaEditPageLocators(object):
    UPDATE_BUTTON = (By.CLASS_NAME, "save")
    PASSWORD_CHECKBOX = (By.ID, "change-password")

class LumaEditAddressPageLocators(object):
    UPDATE_BUTTON = (By.CLASS_NAME, "save")
    
class LumaManageAddressPageLocators(object):
    CREATE_BUTTON = (By.CLASS_NAME, "add")
    DELETE_BUTTON = (By.CLASS_NAME, "delete")
    ACCEPT_BUTTON = (By.CLASS_NAME, "action-accept")

class LumaCreateAddressPageLocators(object):
    CREATE_BUTTON = (By.CLASS_NAME, "save")