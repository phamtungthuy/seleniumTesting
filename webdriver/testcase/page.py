from testcase.locator import *
from testcase.element import *
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
class LumaMainPage(BasePage):
    
    search = BaseSearchElement("q")

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

    def can_move_to_checkout_page(self):
        try:
            showCart = self.driver.find_element(*LumaCartPageLocators.SHOW_CART)
            self.driver.execute_script("arguments[0].click();", showCart)
            WebDriverWait(self.driver, 3).until(
                lambda driver: driver.find_element(*LumaCartPageLocators.VIEW_CART))
            viewCart = self.driver.find_element(*LumaCartPageLocators.VIEW_CART)
            if viewCart:
                return True
            else: return False
        except:
            return False

    def move_to_shopping_cart_page(self):
        showCart = self.driver.find_element(*LumaCartPageLocators.SHOW_CART)
        self.driver.execute_script("arguments[0].click();", showCart)
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCartPageLocators.VIEW_CART))
        viewCart = self.driver.find_element(*LumaCartPageLocators.VIEW_CART)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", viewCart)
        self.driver.execute_script("arguments[0].click();", viewCart)
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
        return all(error_message not in self.driver.page_source for error_message in error_messages) \
            and self.driver.current_url != "https://magento.softwaretestingboard.com/customer/account/create/"
    
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
        return all(error_message not in self.driver.page_source for error_message in error_messages) and self.driver.current_url == "https://magento.softwaretestingboard.com/"
    
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
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.find_element(*LumaManageAddressPageLocators.ACCEPT_BUTTON))
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
    
class LumaResultSearchPage(BasePage):
    search = BaseSearchElement("q")

    def go_to_random_cart_page(self):
        card_images = self.driver.find_elements(*LumaResultSearchPageLocators.CARD_IMAGE)
        card_image = random.choice(card_images)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", card_image)
        ActionChains(self.driver).move_to_element(card_image).perform()
        self.driver.execute_script("arguments[0].click();", card_image)


    def is_title_matches(self):
        return "Search results" in self.driver.title
    
    def move_to_main_page(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaResultSearchPageLocators.LOGO)
        )
        logo = self.driver.find_element(*LumaResultSearchPageLocators.LOGO)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", logo)
        self.driver.execute_script("arguments[0].click();", logo)
    
class LumaCartPage(BasePage):
    search = BaseSearchElement("q")
    quantity = BaseInputElement("qty")
    nickname = BaseInputElement("nickname_field")
    summary = BaseInputElement("summary_field")
    review = BaseInputElement("review_field")


    def add_cart(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCartPageLocators.SIZE))
        sizes = self.driver.find_elements(*LumaCartPageLocators.SIZE)
        self.driver.execute_script("arguments[0].click();", random.choice(sizes))

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCartPageLocators.COLOR))
        colors = self.driver.find_elements(*LumaCartPageLocators.COLOR)
        self.driver.execute_script("arguments[0].click();", random.choice(colors))

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCartPageLocators.ADD_CART))
        self.quantity = str(random.randint(1, 10))

        addButton = self.driver.find_element(*LumaCartPageLocators.ADD_CART)
        addButton.click()

    def is_added_successfully(self):
        success_messages = ["message-success"]
        if any(success_message in self.driver.page_source for success_message in success_messages):
            return True
        error_messages = ["message-error"]
        return all(error_message not in self.driver.page_source for error_message in error_messages)
    
    def move_to_shopping_cart(self):
        showCart = self.driver.find_element(*LumaCartPageLocators.SHOW_CART)
        self.driver.execute_script("arguments[0].click();", showCart)
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCartPageLocators.VIEW_CART))
        viewCart = self.driver.find_element(*LumaCartPageLocators.VIEW_CART)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", viewCart)
        self.driver.execute_script("arguments[0].click();", viewCart)

    def display_review(self):
        showReview = self.driver.find_element(*LumaCartPageLocators.SHOW_REVIEW)
        ActionChains(self.driver).move_to_element(showReview).perform()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", showReview)
        self.driver.execute_script("arguments[0].click();", showReview)

    def review_comment(self):
        starRating = self.driver.find_element(*LumaCartPageLocators.STAR)
        ActionChains(self.driver).move_to_element(starRating).perform()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", starRating)
        self.driver.execute_script("arguments[0].click();", starRating)

        submitButton = self.driver.find_element(*LumaCartPageLocators.SUBMIT_BUTTON)
        ActionChains(self.driver).move_to_element(submitButton).perform()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", submitButton)
        self.driver.execute_script("arguments[0].click();", submitButton)

    def is_reviewed_successfully(self):
        success_messages = ["message-success"]
        if any(success_message in self.driver.page_source for success_message in success_messages):
            return True
        error_messages = ["message-error"]
        return all(error_message not in self.driver.page_source for error_message in error_messages)

class LumaShoppingCartPage(BasePage):
    def is_title_matches(self):
        return "Shopping Cart" in self.driver.title
    
    def delete_all_carts(self):
        while(len(self.driver.find_elements(*LumaShoppingCartLocators.DELETE_CART)) != 0):
            deleteCart = self.driver.find_element(*LumaShoppingCartLocators.DELETE_CART)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", deleteCart)
            self.driver.execute_script("arguments[0].click();", deleteCart)
        
    def is_deleted_all_carts(self):
        if(len(self.driver.find_elements(*LumaShoppingCartLocators.DELETE_CART)) != 0):
            return False
        return True
            
    def move_to_checkout_page(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaShoppingCartLocators.CHECKOUT_BUTTON))
        checkoutButton = self.driver.find_element(*LumaShoppingCartLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", checkoutButton)
        self.driver.execute_script("arguments[0].click();", checkoutButton)
        

        

class LumaCheckoutPage(BasePage):
    def is_title_matches(self):
        return "Checkout" in self.driver.title
    
    def continue_checkout(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCheckoutPageLocators.CONTINUE_BUTTON))
        continueButton = self.driver.find_element(*LumaCheckoutPageLocators.CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", continueButton)
        self.driver.execute_script("arguments[0].click();", continueButton)

    def complete_checkout(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element(*LumaCheckoutPageLocators.CHECKOUT_BUTTON))
        checkoutButton = self.driver.find_element(*LumaCheckoutPageLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", checkoutButton)
        self.driver.execute_script("arguments[0].click();", checkoutButton)
        
    def is_checkout_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains("Success Page"))
            return "Success Page" in self.driver.title
        
        except:
            return False
        
        