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
        
    def test_1_create_an_account_with_existed_email(self):
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

    def test_2_create_an_account_successfully(self):
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

    def test_3_login_fail(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "demoemail@email.com"
        loginPage.password = "password"
        loginPage.login()

        assert not loginPage.is_login_successful()
        time.sleep(2)

    def test_4_login_sucessfully(self):
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


    def test_1_edit_name(self):
        
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

    def test_2_edit_address(self):

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

    def test_3_add_new_address_book(self):
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

    def test_4_delete_address_book(self):
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


class LumaShopping(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(luma_website)
        mainpage = page.LumaMainPage(self.driver)
        mainpage.go_to_login_page()

        loginPage = page.LumaLoginPage(self.driver)
        loginPage.emailAddress = "selenium@selenium.com"
        loginPage.password = "Password123"
        loginPage.login()

    def test_1_add_and_remove_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["hoodie", "jacket"]
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
        shoppingcart.delete_all_carts()

        assert shoppingcart.is_deleted_all_carts()

    def test_2_checkout_carts(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["tee", "tank"]
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

    def test_3_comment(self):
        mainpage = page.LumaMainPage(self.driver)
        assert mainpage.is_title_matches()
        search_array = ["hoodie", "jacket"]
        for idx, search_text in enumerate(search_array):
            if idx == 0:
                mainpage.search = search_text
                mainpage.search.search()
            
            searchpage = page.LumaResultSearchPage(self.driver)
            assert searchpage.is_title_matches()
            searchpage.go_to_random_cart_page()

            cartpage = page.LumaCartPage(self.driver)
            cartpage.display_review()
            cartpage.nickname ="Nick name"
            cartpage.summary ="Good"
            cartpage.review = "This is really an awesome item"
            cartpage.review_comment()

            assert cartpage.is_reviewed_successfully()

            time.sleep(2)
            if idx < len(search_array) - 1:
                cartpage.search = search_array[idx + 1]
                cartpage.search.search()



    def tearDown(self):
        time.sleep(2)
        self.driver.close()