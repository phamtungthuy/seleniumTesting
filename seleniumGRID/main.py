from testcase.test import *
from testcase2.test import *
import unittest
from testcase2 import *

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteAuthentication))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteShopping))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaWebsiteSignin))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaWebsiteSignup))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaShoppingWithoutCartsBefore))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaShoppingHavingCartsBefore))
    unittest.TextTestRunner().run(suite)