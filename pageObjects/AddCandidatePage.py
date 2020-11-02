
from selenium import webdriver
import time

class Candidate:

    ChangeTeamDropdown = "//*[text()='JigneshGBK AdminGBK']"
    ChangeTeamOption = "//a[text()='JP-BK-945']"
    AddCandidateButton = "//a[text()=' Add Candidate']"
    Firstname = "//label[text()='First Name']/following::input[1]"
    Lastname = "//label[text()='Last Name']/following::input[1]"
    Email = "//label[text()='Email']/following::input[1]"
    ReferrerButton = "//*[@id='react-select-9--value']"
    ReferrerOption = "//*[@aria-label='JigneshGBK AdminGBK']"
    Save = "//a[text()='Save']"


    def __init__(self,driver):
        self.driver = driver

    def NavigateToAddCandidate(self):
        print("")  
        self.driver.find_element_by_xpath(self.ChangeTeamDropdown).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.ChangeTeamOption).click()
        time.sleep(5)
      
    def clickAddcandidate(self):
        self.driver.find_element_by_xpath(self.AddCandidateButton).click()
        time.sleep(5)
    
    def setFirstname(self, firstname):
        print("set firstname")
        self.driver.find_element_by_xpath(self.Firstname).send_keys(firstname)
        time.sleep(2)
        
    def setLastname(self, lastname):
        print("set lastname")
        self.driver.find_element_by_xpath(self.Lastname).send_keys(lastname)
        time.sleep(2)
        
    def setEmail(self, email):
        print("set email")
        self.driver.find_element_by_xpath(self.Email).send_keys(email)
        time.sleep(2)
        
    def selectReferrer(self):
        print("select Referrer")
        self.driver.find_element_by_xpath(self.ReferrerButton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.ReferrerOption).click()
        
    def SaveRecord(self):
        print("Candidate Saved")
        self.driver.find_element_by_xpath(self.Save).click()
        time.sleep(5)
        
        
        
        