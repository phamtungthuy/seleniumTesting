from testcase.test import *
from testcase2.test import *
import unittest
from testcase2 import *

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteAuthentication))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SauceWebsiteShopping))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaWebsiteAuthentication))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaControlAccount))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LumaShopping))
    unittest.TextTestRunner().run(suite)