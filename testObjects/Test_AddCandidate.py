
import time
import unittest  
from selenium import webdriver   
from pageObjects.LoginPage import Login 
from utilities import ReadExcelData as rd  
from pageObjects.AddCandidatePage import Candidate
from pageObjects.CandidateEmail import CandidateEmail 


rows = rd.totalRows(rd.filePath, "AddCandidate")
print(rows)  
cols = rd.totalColumns(rd.filePath, "AddCandidate")
print(cols)  


class Test_BrokerAdmin(unittest.TestCase):
    baseURL ="https://next.getbrokerkit.com/home/"
    homepageURL = "https://next.getbrokerkit.com/recruiter/today"
    username="test@getbrokerkit.com"
    password="task.test.GBK"
        
    
    @classmethod
    def setUpClass(self):
        print("=========================before Class=========================")   
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

        self.ac = Candidate(self.driver)
        self.ce = CandidateEmail(self.driver)
            
    @classmethod
    def tearDownClass(self):
        print("=========================After Class=========================") 
        time.sleep(10)     
        #self.driver.close()
    
    @classmethod
    def setUp(self):
        print("=========================before method=========================")
        
    @classmethod
    def tearDown(self):   
        print("=========================After method=========================")    
    
        
    def AddCandidate(self):
        
        self.ac.NavigateToAddCandidate()
        for r in range(2, rows+1):
            
            print("Running testAddCandidate")   
            self.ac.clickAddcandidate()  
            self.ac.setFirstname(rd.readData(rd.filePath, "AddCandidate", r, 1))
            self.ac.setLastname(rd.readData(rd.filePath, "AddCandidate", r, 2))
            self.ac.setEmail(rd.readData(rd.filePath, "AddCandidate", r, 3)) 
            self.ac.selectReferrer()     
            self.ac.SaveRecord()    
            self.driver.get(self.homepageURL)                                      
            print("Candidate added")  
     
     
    def testCandidateEmail(self):      
        self.ac.NavigateToAddCandidate()      
        for r in range(2, rows+1):     
            
            print("Running testAddCandidate")        
            self.ac.clickAddcandidate()    
            self.ac.setFirstname(rd.readData(rd.filePath, "AddCandidate", r, 1))
            self.ac.setLastname(rd.readData(rd.filePath, "AddCandidate", r, 2))
            self.ac.setEmail(rd.readData(rd.filePath, "AddCandidate", r, 3)) 
            self.ac.selectReferrer()  
            self.ac.SaveRecord()                                   
            print("Candidate added")      
            
            self.ce.AddCandidateStatusEmail(rd.readData(rd.filePath, "Email", r, 6), rd.readData(rd.filePath, "Email", r, 7))
            self.ce.ClickAddCCEmailOption() 
            self.ce.SetAddCCTextBox(rd.readData(rd.filePath, "Email", r, 8))
            #self.ce.ClickAddCCEmailValue()
            self.ce.ClickCancelAndHideOption()
            self.ce.SetEmailTemplate()
            self.driver.get(self.homepageURL) 
            print("Candidate Email operations performed")
       
        
           
if __name__ == '__main__':   
    unittest.main()    
    
    
    
    
    
    
     
    