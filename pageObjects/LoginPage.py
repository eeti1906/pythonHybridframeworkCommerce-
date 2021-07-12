import pytest
from selenium import webdriver
# from selenium.webdriver.common.keys import
# driver = webdriver.Chrome(executable_path="C:\chromedriver_win32")


class LoginPage:
    text_username_id = "Email"
    text_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()



