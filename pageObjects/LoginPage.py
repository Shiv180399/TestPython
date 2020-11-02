'''
Created on 06-Oct-2020

@author: abhinandan
'''
from selenium import webdriver
import time

class Login:
    
    Link_Login="//*[text()='Login']"
    btn_Signinwithgoogle="(//A[@class='btn btn-secondary btn-lg pl40'])[1]"
    option_usersignin="//*[text()='Use another account']"
    TextBox_Username_Xpath = "//*[@id='identifierId']"
    btn_UsernameNext="//*[@id='identifierNext']//button"
    TextBox_Password_Xpath="//*[@id='password']//input"
    btn_passwordNext="//*[@id='passwordNext']//button"
    
    def __init__(self,driver):
        self.driver = driver
    
    def navigateToLogin(self):
        self.driver.find_element_by_xpath(self.Link_Login).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.btn_Signinwithgoogle).click()  

    def setUsername(self,username):
        self.driver.find_element_by_xpath(self.TextBox_Username_Xpath).clear()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.TextBox_Username_Xpath).send_keys(username)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_UsernameNext).click()
        time.sleep(3)
        
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.TextBox_Password_Xpath).clear()
        time.sleep(3)
        self.driver.find_element_by_xpath(self.TextBox_Password_Xpath).send_keys(password)
        time.sleep(3)
        self.driver.find_element_by_xpath(self.btn_passwordNext).click()
        time.sleep(3)
