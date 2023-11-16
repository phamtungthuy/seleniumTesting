from .element import *
from .locator import *
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class SauceLoginPage(BasePage):
    username = BaseInputElement("user-name")
    password = BaseInputElement("password")

    def is_url_matches(self):
        return self.driver.current_url == "https://www.saucedemo.com/"

    def login(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceLoginPageLocators.LOGIN_BUTTON)
        )
        loginButton = self.driver.find_element(*SauceLoginPageLocators.LOGIN_BUTTON)
        
        self.driver.execute_script("arguments[0].click();", loginButton)


    def is_login_successful(self):
        return self.driver.current_url != "https://www.saucedemo.com/"
    


    
    
class SauceMainPage(BasePage):
    def is_url_matches(self):
        return self.driver.current_url == "https://www.saucedemo.com/inventory.html"

    def logout(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceMainPageLocators.SIGNOUT_BUTTON)
        )

        logoutButton = self.driver.find_element(*SauceMainPageLocators.SIGNOUT_BUTTON)
        
        self.driver.execute_script("arguments[0].click();", logoutButton)

    def open_menu(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceMainPageLocators.MENU)
        )
        menu = self.driver.find_element(*SauceMainPageLocators.MENU)
       
        self.driver.execute_script("arguments[0].click();", menu)

    def add_carts(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_elements(*SauceMainPageLocators.ADD_CART_BUTTON)
        )
        addCartButton = self.driver.find_elements(*SauceMainPageLocators.ADD_CART_BUTTON)
        self.driver.execute_script("arguments[0].click();", addCartButton[0])
        self.driver.execute_script("arguments[0].click();", addCartButton[1])
        self.driver.execute_script("arguments[0].click();", addCartButton[2])

    def move_to_cart_page(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceMainPageLocators.SHOP_CART_LINK)
        )
        shop_cart_link = self.driver.find_element(*SauceMainPageLocators.SHOP_CART_LINK)
        self.driver.execute_script("arguments[0].click();", shop_cart_link)

    def is_logout_successful(self):
        return self.driver.current_url == "https://www.saucedemo.com/"

class SauceCartPage(BasePage):
    def is_url_matches(self):
        return self.driver.current_url == "https://www.saucedemo.com/cart.html"
    
    def remove_a_cart(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceCartPageLocators.REMOVE_CART_BUTTON)
        )

        removeCartButton = self.driver.find_element(*SauceCartPageLocators.REMOVE_CART_BUTTON)
        
        self.driver.execute_script("arguments[0].click();", removeCartButton)


    def go_to_check_out_step_one(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceCartPageLocators.CHECKOUT_BUTTON)
        )
        checkoutButton = self.driver.find_element(*SauceCartPageLocators.CHECKOUT_BUTTON)
        
        self.driver.execute_script("arguments[0].click();", checkoutButton)
        

class SauceCheckoutStepOnePage(BasePage):
    firstName = BaseInputElement("first-name")
    lastName = BaseInputElement("last-name")
    zip = BaseInputElement("postal-code")

    def is_url_matches(self):
        return self.driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    
    def go_to_check_out_step_two(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceCheckoutStepOnePageLocators.CHECKOUT_BUTTON)
        )

        checkoutButton = self.driver.find_element(*SauceCheckoutStepOnePageLocators.CHECKOUT_BUTTON)

        self.driver.execute_script("arguments[0].click();", checkoutButton)


class SauceCheckoutStepTwoPage(BasePage):
    def is_url_matches(self):
        return self.driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    def checkout(self):
        WebDriverWait(self.driver, 100).until(
            lambda driver : driver.find_element(*SauceCheckoutStepTwoPageLocators.CHECKOUT_BUTTON)
        )

        checkoutButton = self.driver.find_element(*SauceCheckoutStepTwoPageLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", checkoutButton)


    def is_checkout_success(self):
        return self.driver.current_url != "https://www.saucedemo.com/checkout-step-two.html"
