
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CandidateEmail:

    
    Emailbutton = "//a[@id='btn-email']"
    EmailSubject = "//input[@name='subject']"
    emailIframe = "//div[@class='tox-edit-area']/iframe"
    EmailBody = "//*[@id='tinymce']"
    AddCCEmailOption = "//*[text()='Add CC Emails']"
    AddCCTextBox = "//label[text()='CC']/following-sibling::div//input"
    AddCCEmailValue = "//*[@aria-label='test+06@getbrokerkit.com']"
    CancelAndHideOption = "//a[text()='Cancel and hide']"
    AddAttachmentBtn = "//div[text()='Add Attachment']"
    SelectTemplateDropdown = "//div[text()='Select a template']"
    SelectTemplateOptions = "//*[text()='Mail with all variables']"
    
    def __init__(self,driver):
        self.driver = driver

    def AddCandidateStatusEmail(self,subject,body):
        print("set subject & body of email")  
        self.driver.find_element_by_xpath(self.Emailbutton).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.EmailSubject).send_keys(subject)
        time.sleep(5)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath(self.emailIframe))
        
        self.driver.find_element_by_xpath(self.EmailBody).send_keys(body)       
        self.driver.switch_to_default_content()
        time.sleep(5)
      
    def ClickAddCCEmailOption(self):
        print("Click on add cc email option")  
        self.driver.find_element_by_xpath(self.AddCCEmailOption).click()
        time.sleep(5)

        
    def SetAddCCTextBox(self,CCemail):
        print("set value for cc email")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.AddCCTextBox).send_keys(CCemail)   
        time.sleep(2)
        self.driver.find_element_by_xpath(self.AddCCTextBox).send_keys(Keys.ENTER)
        
        time.sleep(2)
        
    def ClickAddCCEmailValue(self):
        print("Click on Add cc email value")
        self.driver.find_element_by_xpath(self.AddCCEmailValue).click()
        time.sleep(3)
        
    def ClickCancelAndHideOption(self):
        print("Click on cancel hide options")
        self.driver.find_element_by_xpath(self.CancelAndHideOption).click()
        time.sleep(2)
        
    def ClickAddAttachmentBtn(self):
        print("Click on add attachment button & upload attachment")
        self.driver.find_element_by_xpath(self.AddAttachmentBtn).click()
        time.sleep(5)
        
        
    def SetEmailTemplate(self):
        print("Set email template")
        self.driver.find_element_by_xpath(self.SelectTemplateDropdown).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.SelectTemplateOptions).click()
        
