import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from testCases.test_base import BaseTest
from pageObjects.CreateProjectPage import CreateProjectPage

class Test_CreatePrjt(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code
    base_project_name= testdata.base_project_name
    project_number = testdata.project_number
    project_logo= testdata.projectlogo
    error_msg= testdata.project_error_msg

    def test_create_project(self):

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(1)

        self.cp= CreateProjectPage(self.driver)

        for i in range(1, 3):
            self.cp.clickMainprojectbtn()
            project_name = self.base_project_name + " " + str(self.project_number)
            self.cp.enterProjectname(project_name)
            self.cp.uploadLogo(self.project_logo)
            self.cp.clickCreatebtn()
            self.e = self.cp.get_element_text()

            while self.e == testdata.project_error_msg:

                time.sleep(1)

                self.cp.clickDonebtn()

                self.project_number += 1

                project_name = self.base_project_name + " " + str(self.project_number)

                self.cp.clearprojectnamefield()

                self.cp.enterProjectname(project_name)

                self.cp.clickCreatebtn()

                self.e = self.cp.get_element_text()

                time.sleep(1)

            self.cp.clickDonebtn()
            self.project_number += 1
            time.sleep(1)