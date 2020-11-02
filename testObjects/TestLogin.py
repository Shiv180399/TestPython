
import time
import unittest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.CommonMethods import globalUtilities
from lib2to3.tests.support import driver


class Test_Login(unittest.TestCase):
    driver
    
    @classmethod
    def setUpClass(self):
        print("=========================before Class=========================") 
        self.gu = globalUtilities(self) 
            
    @classmethod
    def tearDownClass(self):
        print("=========================After Class=========================") 
    
    @classmethod
    def setUp(self):
        print("=========================before method=========================")
        
    @classmethod
    def tearDown(self):
        print("=========================After method=========================")    
    
    def testLoginThroughGmail(self):
        
        self.gu.LoginAdmin()
        
       
    
if __name__ == '__main__': 
    unittest.main()     
    