import unittest
from selenium import webdriver
from . import page
from . import *
import time
import random
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

class LumaControlAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        mainpage = page.LumaMainPage(self.driver)
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()

        mainpage.go_to_account_page()


    def test_edit_name(self):
        
        accountPage = page.LumaAccountPage(self.driver)
        assert accountPage.is_title_matches()
        accountPage.go_to_edit_account_information_page()
        
        editPage = page.LumaEditPage(self.driver)
        assert editPage.is_title_matches()
        editPage.turn_on_edit_password()
        editPage.firstName = "Marry"
        editPage.lastName = "Queen"
        editPage.currentPassword = "Password123"
        editPage.password = "Password123"
        editPage.confirmPassword = "Password123"

        editPage.update_account_information()

        assert editPage.is_updated_successfully()

    def test_edit_address(self):

        accountPage = page.LumaAccountPage(self.driver)
        assert accountPage.is_title_matches()
        accountPage.go_to_edit_address_page()

        editAddressPage = page.LumaEditAddressPage(self.driver)
        assert editAddressPage.is_title_matches()
        editAddressPage.firstname = "Marry"
        editAddressPage.lastname = "Queen"
        editAddressPage.telephone = "11111111"
        editAddressPage.address1 = "Viet nam"
        editAddressPage.zip = "000000"
        editAddressPage.city = "Viet nam"
        editAddressPage.select = "Vietnam"
        
        editAddressPage.update_address_information()

        assert editAddressPage.is_updated_successfully()

    def test_add_new_address_book(self):
        accountPage = page.LumaAccountPage(self.driver)
        assert accountPage.is_title_matches()
        accountPage.go_to_manage_address_page()

        manageAddressPage = page.LumaManageAddressPage(self.driver)
        assert manageAddressPage.is_title_matches()
        manageAddressPage.go_to_create_new_address_page()

        createAddressPage = page.LumaCreateNewAddressPage(self.driver)
        assert createAddressPage.is_title_matches()
        createAddressPage.firstname = "Marry" + str(random.randint(1000, 10000))
        createAddressPage.lastname = "Queen" + str(random.randint(100, 10000))
        createAddressPage.telephone = str(random.randint(100000000, 900000000))
        createAddressPage.address1 = "Viet nam"
        createAddressPage.zip = str(random.randint(100000000, 900000000))
        createAddressPage.city = "Viet name"
        createAddressPage.select = "Vietnam"

        createAddressPage.create_new_address()

        assert createAddressPage.is_created_successfully()

    def test_delete_address_book(self):
        accountPage = page.LumaAccountPage(self.driver)
        assert accountPage.is_title_matches()
        accountPage.go_to_manage_address_page()

        manageAddressPage = page.LumaManageAddressPage(self.driver)
        assert manageAddressPage.is_title_matches()
        
        manageAddressPage.delete_address()
        manageAddressPage.accept_delete_address()

        assert manageAddressPage.is_deleted_successfully()


    def tearDown(self):
        time.sleep(2)
        self.driver.close()
