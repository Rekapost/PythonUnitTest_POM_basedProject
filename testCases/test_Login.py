from selenium import webdriver
import unittest
import HtmlTestRunner
import sys;
import os

# we need to import by sys called as system variable  (sys, path , append project path)
os.environ['PATH']="C:/Users/Reka/PycharmProject/PythonUnitTest_POMBasedPRoject"   # method  specify environment variable
#sys.path.append('C:/Users/Reka/PycharmProject/PythonUnitTest_POMBasedPRoject')
# this stmt is to add project path to environment variable  path variable
# as we are going to run the project through cmd prompt and  to get reports , we need sys path

from pageObjects.loginPage import Login

class test_login(unittest.TestCase):  # it should start with test or end with test
    baseURL = "https://admin-demo.nopcommerce.com"
    useremail = "admin@yourstore.com"
    password = "admin"

    @classmethod
    def setUpClass(cls):
#       driver=webdriver.Chrome(executable_path="C://Users//Reka//PycharmProjects//PythonUnitTestProject_POMBased//drivers//chromedriver.exe")
#       serv_object = Service("C:/Users/Reka/Drivers/chromedriver.exe")
#       driver = webdriver.Chrome(service=serv_object)
        cls.driver=webdriver.Chrome()
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def loginLink_test(self):  # creating object for  pageObjects LoginPage class, loginPage has constructor and constructor is expecting driver parameter
        self.driver=webdriver.Chrome()
        lp = Login(self.driver)
        lp.setUserName(self.useremail)
        lp.setPassword(self.password)
        lp.clickLogin()
        """  Reka
        if self.driver.title=="Dashboard / nopCommerce administration"  # writing assertion command  to validate
            assert True
        """
        # writing assertion command  to validate
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration", "webpage title is not equal")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C://Users//Reka//PycharmProject//PythonUnitTest_POMBasedPRoject//reports"))
