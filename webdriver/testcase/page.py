from testcase.locator import *
from testcase.element import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
class LumaMainPage(BasePage):
    
    def go_to_account_page(self):
        switchButton = self.driver.find_element(*LumaMainPageLocators.SWITCH_BUTTON)
        switchButton.click()
        acountLink = self.driver.find_element(*LumaMainPageLocators.ACCOUNT_LINK)
        acountLink.click()

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
    
    def is_title_matches(self):
        return "Create New Customer Account" in self.driver.title
    
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
    
    def is_title_matches(self):
        return "Customer Login" in self.driver.title
    
class LumaAccountPage(BasePage):
    

    def go_to_edit_account_information_page(self):
        editInformationLink = self.driver.find_element(*LumaAccountPageLocators.EDIT_INFORMATION)
        editInformationLink.click()
    
    def go_to_edit_address_page(self):
        editAddressLink = self.driver.find_element(*LumaAccountPageLocators.EDIT_ADDRESS)
        editAddressLink.click()

    def go_to_manage_address_page(self):
        manageAddressLink = self.driver.find_element(*LumaAccountPageLocators.MANAGE_ADDRESS)
        manageAddressLink.click()

    def is_title_matches(self):
        return "My Account" in self.driver.title
    
class LumaEditPage(BasePage):
    firstName = BaseInputElement("firstname")
    lastName = BaseInputElement("lastname")
    currentPassword = BaseInputElement("current-password")
    password = BaseInputElement("password")
    confirmPassword = BaseInputElement("password-confirmation")

    def update_account_information(self):
        updateButton = self.driver.find_element(*LumaEditPageLocators.UPDATE_BUTTON)
        updateButton.click()

    def turn_on_edit_password(self):
        passwordCheckbox = self.driver.find_element(*LumaEditPageLocators.PASSWORD_CHECKBOX)
        passwordCheckbox.click()

    def is_updated_successfully(self):
        error_messages = ["message-error"]
        if (any(error_message in self.driver.page_source for error_message in error_messages)):
            return False
        return "Account Information" not in self.driver.title
    
    def is_title_matches(self):
        return "Account Information" in self.driver.title
    
class LumaEditAddressPage(BasePage):
    firstname = BaseInputElement("firstname")
    lastname = BaseInputElement("lastname")
    telephone = BaseInputElement("telephone")
    address1 = BaseInputElement("street_1")
    city = BaseInputElement("city")
    zip = BaseInputElement("zip")
    select = BaseSelectElement("country")

    def update_address_information(self):
        updateButton = self.driver.find_element(*LumaEditAddressPageLocators.UPDATE_BUTTON)
        self.driver.execute_script("arguments[0].click();", updateButton)


    def is_updated_successfully(self):
        error_messages = ["message-error"]
        if (any(error_message in self.driver.page_source for error_message in error_messages)):
            return False
        return "Edit Address" not in self.driver.title

    def is_title_matches(self):
        return "Edit Address" in self.driver.title
    
class LumaManageAddressPage(BasePage):
    
    def go_to_create_new_address_page(self):
        createButton = self.driver.find_element(*LumaManageAddressPageLocators.CREATE_BUTTON)
        self.driver.execute_script("arguments[0].click();", createButton)

    def delete_address(self):
        deleteButton = self.driver.find_element(*LumaManageAddressPageLocators.DELETE_BUTTON)
        if deleteButton: 
            self.driver.execute_script("arguments[0].click()", deleteButton)    

    def accept_delete_address(self):
        acceptButton = self.driver.find_element(*LumaManageAddressPageLocators.ACCEPT_BUTTON)
        if acceptButton:
            self.driver.execute_script("arguments[0].click()", acceptButton)

    def is_deleted_successfully(self):
        success_messages = ["message-success"]
        if any(success_message in self.driver.page_source for success_message in success_messages):
            return True
        error_messages = ["message-error"]
        return all(error_message not in self.driver.page_source for error_message in error_messages)

    def is_title_matches(self):
        return "Address Book" in self.driver.title
    
class LumaCreateNewAddressPage(BasePage):

    firstname = BaseInputElement("firstname")
    lastname = BaseInputElement("lastname")
    telephone = BaseInputElement("telephone")
    address1 = BaseInputElement("street_1")
    city = BaseInputElement("city")
    zip = BaseInputElement("zip")
    select = BaseSelectElement("country")

    def create_new_address(self):
        createButton = self.driver.find_element(*LumaCreateAddressPageLocators.CREATE_BUTTON)
        self.driver.execute_script("arguments[0].click();", createButton)

    def is_created_successfully(self):
        error_messages = ["message-error"]
        if (any(error_message in self.driver.page_source for error_message in error_messages)):
            return False
        return "Add New Address" not in self.driver.title

    def is_title_matches(self):
        return "Add New Address" in self.driver.title