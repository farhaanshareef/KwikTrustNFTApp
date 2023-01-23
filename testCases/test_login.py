import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from testCases.test_base import BaseTest

class Test_Login(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code

    def test_login(self):

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(2)


