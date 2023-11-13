import unittest
from selenium import webdriver
from . import page
from . import *
import time

class LumaWebsiteAuthentication(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        
    def test_create_an_account_with_existed_email(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "John"
        signupPage.lastName = "Jumson"
        signupPage.emailAddress = "email@email.com"
        signupPage.password = "Password123@"
        signupPage.confirmPassword = "Password123@"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()

        time.sleep(2)

    def test_create_an_account_successfully(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email{round(time.time())}@email.com"
        signupPage.password = "Password123@"
        signupPage.confirmPassword = "Password123@"
        signupPage.create_account()
        assert signupPage.is_created_successfully()
        time.sleep(2)

    def test_login_fail(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "demoemail@email.com"
        loginPage.password = "password"
        loginPage.login()

        assert not loginPage.is_login_successful()
        time.sleep(2)

    def test_login_sucessfully(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()

        assert loginPage.is_login_successful()
        time.sleep(5)
    def tearDown(self):
        self.driver.close()


