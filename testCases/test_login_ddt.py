import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_login:
    baseURL = ReadConfig.getapplicationurl()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    """def test_homePagetitle(self, setup):
        self.logger.info("********Test_001_login**********")
        self.logger.info("********Verifying home page title**********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** home page title test passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********homePage test Failed**********")

            assert False """

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********Test__002_DDT_testLogin**********")
        self.logger.info("********Verifying login test**********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows", self.rows)

        lst_status = []  # Empty list variable to store the expected results

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Passed***")
                    self.lp.clicklogout();
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed*****")
                    self.lp.clicklogout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("****Failed")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Passed*****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test Passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test Failed*******")
            self.driver.close()
            assert False

        self.logger.info("******* END of login DDT Test **********")
        self.logger.info("*********** Completed TC_LoginDDT_002 ********")

        '''self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********login test passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_loginPage.png")
            self.driver.close()
            self.logger.error("********login test Failed**********")

            assert False'''
