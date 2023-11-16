from testcase.test import *
from testcase2.test import *
import unittest

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteAuthentication))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteShopping))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaWebsiteAuthentication))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaControlAccount))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaShopping))
    unittest.TextTestRunner().run(suite)