from selenium.webdriver.common.by import By

class SauceLoginPageLocators(object):
    LOGIN_BUTTON = (By.ID, "login-button")

class SauceMainPageLocators(object):
    MENU = (By.ID, "react-burger-menu-btn")
    SIGNOUT_BUTTON = (By.ID, "logout_sidebar_link")
    ADD_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    SHOP_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

class SauceCartPageLocators(object):
    REMOVE_CART_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

class SauceCheckoutStepOnePageLocators(object):
    CHECKOUT_BUTTON = (By.ID, "continue")

class SauceCheckoutStepTwoPageLocators(object):
    CHECKOUT_BUTTON = (By.ID, "finish")