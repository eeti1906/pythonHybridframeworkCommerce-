import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getapplicationurl()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePagetitle(self, setup):
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

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********Verifying login test**********")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
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

            assert False
