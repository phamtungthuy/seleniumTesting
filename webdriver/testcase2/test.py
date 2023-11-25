import unittest
from selenium import webdriver
from . import *
from . import page
import time
class SauceWebsiteAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(sauce_website)

    def test_1_login_with_valid_username_and_password(self):

        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()

        loginpage.username = "standard_user"
        loginpage.password = "secret_sauce"

        loginpage.login()

        assert loginpage.is_login_successful()

    def test_2_login_with_invalid_password(self):
        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()

        loginpage.username = "standard_user"
        loginpage.password = "password"

        loginpage.login()

        assert not loginpage.is_login_successful()
        
    def test_3_login_with_invalid_username(self):
        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()
        
        loginpage.username = "aklsjdlaksjd"
        loginpage.password = "secret_sauce"
        
        loginpage.login()
        
        assert not loginpage.is_login_successful()
        
    def test_4_login_with_invalid_username_and_password(self):
        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()
        
        loginpage.username = "aklsjdlaksjd"
        loginpage.password = "asdasdasd"
        
        loginpage.login()
        
        assert not loginpage.is_login_successful()
        
        

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

class SauceWebsiteShopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(sauce_website)
        loginpage = page.SauceLoginPage(self.driver)
        loginpage.username = "standard_user"
        loginpage.password = "secret_sauce"
        loginpage.login()

    def test_1_add_carts_and_valid_address(self):
        mainpage = page.SauceMainPage(self.driver)
        assert mainpage.is_url_matches()

        mainpage.add_carts()
        time.sleep(1)
        mainpage.move_to_cart_page()

        cartpage = page.SauceCartPage(self.driver)
        assert cartpage.is_url_matches()
        time.sleep(1)
        cartpage.go_to_check_out_step_one()

        checkoutStepOne = page.SauceCheckoutStepOnePage(self.driver)
        assert checkoutStepOne.is_url_matches()
        checkoutStepOne.firstName ="John"
        checkoutStepOne.lastName = "Jumson"
        checkoutStepOne.zip = "123456789"
        time.sleep(1)
        checkoutStepOne.go_to_check_out_step_two()
        time.sleep(1)
        checkoutStepTwo = page.SauceCheckoutStepTwoPage(self.driver)
        assert checkoutStepTwo.is_url_matches()
        checkoutStepTwo.checkout()
        assert checkoutStepTwo.is_checkout_success()

    def test_2_no_carts_and_valid_address(self):
        mainpage = page.SauceMainPage(self.driver)
        assert mainpage.is_url_matches()

        mainpage.move_to_cart_page()

        cartpage = page.SauceCartPage(self.driver)
        assert cartpage.is_url_matches()
        time.sleep(1)
        cartpage.go_to_check_out_step_one()
        checkoutStepOne = page.SauceCheckoutStepOnePage(self.driver)
        assert checkoutStepOne.is_url_matches()
        checkoutStepOne.firstName ="John"
        checkoutStepOne.lastName = "Jumson"
        checkoutStepOne.zip = "123456789"
        time.sleep(1)
        checkoutStepOne.go_to_check_out_step_two()
        time.sleep(1)
        checkoutStepTwo = page.SauceCheckoutStepTwoPage(self.driver)
        assert checkoutStepTwo.is_url_matches()
        checkoutStepTwo.checkout()
        assert checkoutStepTwo.is_checkout_success()

    def test_3_add_carts_and_invalid_address(self):
        mainpage = page.SauceMainPage(self.driver)
        assert mainpage.is_url_matches()

        mainpage.add_carts()
        time.sleep(1)
        mainpage.move_to_cart_page()

        cartpage = page.SauceCartPage(self.driver)
        assert cartpage.is_url_matches()
        time.sleep(1)
        cartpage.go_to_check_out_step_one()

        checkoutStepOne = page.SauceCheckoutStepOnePage(self.driver)
        assert checkoutStepOne.is_url_matches()
        time.sleep(1)
        checkoutStepOne.go_to_check_out_step_two()
        time.sleep(1)
        checkoutStepTwo = page.SauceCheckoutStepTwoPage(self.driver)
        assert not checkoutStepTwo.is_url_matches()

    def test_4_no_carts_and_invalid_address(self):
        mainpage = page.SauceMainPage(self.driver)
        assert mainpage.is_url_matches()
        mainpage.move_to_cart_page()

        cartpage = page.SauceCartPage(self.driver)
        assert cartpage.is_url_matches()
        time.sleep(1)
        cartpage.go_to_check_out_step_one()

        checkoutStepOne = page.SauceCheckoutStepOnePage(self.driver)
        assert checkoutStepOne.is_url_matches()
        time.sleep(1)
        checkoutStepOne.go_to_check_out_step_two()
        time.sleep(1)
        checkoutStepTwo = page.SauceCheckoutStepTwoPage(self.driver)
        assert not checkoutStepTwo.is_url_matches()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()