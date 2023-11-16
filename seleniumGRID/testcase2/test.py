import unittest
from selenium import webdriver
from . import *
from . import page
import time
class SauceWebsiteAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
        self.driver.get(sauce_website)

    def test_1_login_fail(self):
        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()

        loginpage.username = "standard_user"
        loginpage.password = "password"

        loginpage.login()

        assert not loginpage.is_login_successful()

    def test_2_login_success(self):
        loginpage = page.SauceLoginPage(self.driver)
        assert loginpage.is_url_matches()

        loginpage.username = "standard_user"
        loginpage.password = "secret_sauce"

        loginpage.login()

        assert loginpage.is_login_successful()

        mainpage = page.SauceMainPage(self.driver)

        assert mainpage.is_url_matches()

        mainpage.open_menu()
        time.sleep(2)
        mainpage.logout()

        assert mainpage.is_logout_successful()
        

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

class SauceWebsiteShopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
        self.driver.get(sauce_website)
        loginpage = page.SauceLoginPage(self.driver)
        loginpage.username = "standard_user"
        loginpage.password = "secret_sauce"
        loginpage.login()

    def test_1_add_and_remove_carts(self):
        mainpage = page.SauceMainPage(self.driver)
        assert mainpage.is_url_matches()

        mainpage.add_carts()
        time.sleep(1)
        mainpage.move_to_cart_page()

        cartpage = page.SauceCartPage(self.driver)
        assert cartpage.is_url_matches()
        cartpage.remove_a_cart()
        time.sleep(1)
        cartpage.go_to_check_out_step_one()

        checkoutStepOne = page.SauceCheckoutStepOnePage(self.driver)
        assert checkoutStepOne.is_url_matches()
        checkoutStepOne.firstName ="John"
        checkoutStepOne.lastName = "Jumson"
        checkoutStepOne.zip = "123456789"
        time.sleep(2)
        checkoutStepOne.go_to_check_out_step_two()
        time.sleep(1)
        checkoutStepTwo = page.SauceCheckoutStepTwoPage(self.driver)
        assert checkoutStepTwo.is_url_matches()
        checkoutStepTwo.checkout()
        assert checkoutStepTwo.is_checkout_success()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()