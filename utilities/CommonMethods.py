from selenium import webdriver
from pageObjects.LoginPage import Login
import time

class globalUtilities:
    baseURL ="https://next.getbrokerkit.com/home/"
    username="test@getbrokerkit.com"
    password="task.test.GBK"
    
    def __init__(self,driver):
        self.driver = driver
    
    
    def LoginAdmin(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
        actualTitle = self.driver.title
        print("Login Page title is: ",actualTitle)
        
        self.lp = Login(self.driver)
        self.lp.navigateToLogin()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)   
        print("Logged in to BK")
        time.sleep(10)
    
    
