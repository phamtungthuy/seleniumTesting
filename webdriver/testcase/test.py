import unittest
from selenium import webdriver
from . import page
from . import *
import time
import random
class LumaWebsiteSignin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)

    def test_1_login_with_valid_username_and_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()
        assert loginPage.is_login_successful()

    def test_2_login_with_invalid_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "passworasddd123"
        loginPage.login()
        assert not loginPage.is_login_successful()
        
    def test_3_login_with_invalid_username(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.coma"
        loginPage.password = "Password123"
        loginPage.login()
        assert not loginPage.is_login_successful()
        
    def test_4_login_with_invalid_username_and_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "demoemail@email.com"
        loginPage.password = "passwordasdasdasdad"
        loginPage.login()
        assert not loginPage.is_login_successful()



    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        
class LumaWebsiteSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        
    def test_1_create_an_account_with_valid_parameters(self):
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
        
    def test_2_create_an_account_with_invalid_confirm_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email{round(time.time())}@email.com"
        signupPage.password = "Password123@"
        signupPage.confirmPassword = "Password123"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    
    def test_3_create_an_account_with_invalid_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email{round(time.time())}@email.com"
        signupPage.password = "123"
        signupPage.confirmPassword = "123"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
        
    def test_4_create_an_account_with_invalid_password_and_confirm_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email{round(time.time())}@email.com"
        signupPage.password = "123"
        signupPage.confirmPassword = "123456"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    
    def test_5_create_an_account_with_invalid_email(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email"
        signupPage.password = "Password123@"
        signupPage.confirmPassword = "Password123@"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    
    def test_6_create_an_account_with_invalid_email_and_confirm_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email"
        signupPage.password = "Password123@"
        signupPage.confirmPassword = "123"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    
    def test_7_create_an_account_with_invalid_email_and_password(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email"
        signupPage.password = "123"
        signupPage.confirmPassword = "123"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    
    def test_8_create_an_account_with_invalid_parameters(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_signup_page()

        signupPage = page.LumaSignupPage(self.driver)
        signupPage.firstName = "Marry"
        signupPage.lastName = "Queen"
        
        signupPage.emailAddress = f"email"
        signupPage.password = "123"
        signupPage.confirmPassword = "123456"
        signupPage.create_account()
        assert not signupPage.is_created_successfully()
    

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

class LumaShoppingWithoutCartsBefore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        mainpage = page.LumaMainPage(self.driver)
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()


    def test_1_checkout_carts_after_adding_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["tee"]
        for idx, search_text in enumerate(search_array):
            if idx == 0:
                mainpage.search = search_text
                mainpage.search.search()

            searchpage = page.LumaResultSearchPage(self.driver)
            assert searchpage.is_title_matches()
            searchpage.go_to_random_cart_page()

            cartpage = page.LumaCartPage(self.driver)
            cartpage.add_cart()
            assert cartpage.is_added_successfully()

            if idx < len(search_array) - 1:
                cartpage.search = search_array[idx + 1]
                cartpage.search.search()
            else:
                cartpage.move_to_shopping_cart()

        shoppingcart = page.LumaShoppingCartPage(self.driver)
        assert shoppingcart.is_title_matches()
        shoppingcart.move_to_checkout_page()

        checkoutpage =page.LumaCheckoutPage(self.driver)
        checkoutpage.continue_checkout()
        checkoutpage.complete_checkout()

        assert checkoutpage.is_checkout_successful()
        
    def test_2_checkout_carts_without_adding_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()

        assert not mainpage.can_move_to_checkout_page()
        


    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        
class LumaShoppingHavingCartsBefore(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        mainpage = page.LumaMainPage(self.driver)
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()
        
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["hoodie"]
        for idx, search_text in enumerate(search_array):
            if idx == 0:
                mainpage.search = search_text
                mainpage.search.search()

            searchpage = page.LumaResultSearchPage(self.driver)
            searchpage.go_to_random_cart_page()

            cartpage = page.LumaCartPage(self.driver)
            cartpage.add_cart()

            if idx < len(search_array) - 1:
                cartpage.search = search_array[idx + 1]
                cartpage.search.search()
                
        
        searchpage = page.LumaResultSearchPage(self.driver)
        searchpage.move_to_main_page()
            
        
    def test_1_checkout_carts_after_adding_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["tank"]
        for idx, search_text in enumerate(search_array):
            if idx == 0:
                mainpage.search = search_text
                mainpage.search.search()

            searchpage = page.LumaResultSearchPage(self.driver)
            assert searchpage.is_title_matches()
            searchpage.go_to_random_cart_page()

            cartpage = page.LumaCartPage(self.driver)
            cartpage.add_cart()
            assert cartpage.is_added_successfully()

            if idx < len(search_array) - 1:
                cartpage.search = search_array[idx + 1]
                cartpage.search.search()
            else:
                cartpage.move_to_shopping_cart()

        shoppingcart = page.LumaShoppingCartPage(self.driver)
        assert shoppingcart.is_title_matches()
        shoppingcart.move_to_checkout_page()

        checkoutpage =page.LumaCheckoutPage(self.driver)
        checkoutpage.continue_checkout()
        checkoutpage.complete_checkout()

        assert checkoutpage.is_checkout_successful()
    
    def test_2_checkout_carts_without_adding_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        assert mainpage.can_move_to_checkout_page()
        mainpage.move_to_shopping_cart_page()
        
        shoppingcart = page.LumaShoppingCartPage(self.driver)
        assert shoppingcart.is_title_matches()
        shoppingcart.move_to_checkout_page()

        checkoutpage =page.LumaCheckoutPage(self.driver)
        checkoutpage.continue_checkout()
        checkoutpage.complete_checkout()

        assert checkoutpage.is_checkout_successful()
    def tearDown(self):
        time.sleep(2)
        self.driver.close()