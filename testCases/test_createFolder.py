import time
import pytest
from selenium import webdriver

from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from testCases.test_base import BaseTest
from pageObjects.CreateProjectPage import CreateProjectPage

class Test_createFolder(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code

    base_folder_name= testdata.base_folder_name
    folder_number= testdata.folder_number
    error_msg= testdata.project_error_msg

    def test_create_folder(self):

        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(1)

        self.cf= CreateFolderPage(self.driver)

        time.sleep(1)

        self.cf.selectProject()

        time.sleep(2)

        self.cf.selectFileOption()

        time.sleep(1)

        for i in range(1, 2):

            self.e = self.cf.getFoldercount()

            if self.e >20:

                self.cf.selectFolder()

            else:

                self.cf.createFolder()

                folder_name= self.base_folder_name + " " + str(self.folder_number)

                time.sleep(1)

                self.cf.enterFoldername(folder_name)

                self.cf.clickCreatebtn()

                try:

                    self.e = self.cf.get_element_text()

                    while self.e == testdata.folder_error_msg:

                        time.sleep(1)

                        self.cf.clickDonebtn()

                        self.folder_number += 1

                        folder_name = self.base_folder_name + " " + str(self.folder_number)

                        self.cf.clearFoldernamefield()

                        self.cf.enterFoldername(folder_name)

                        self.cf.clickCreatebtn()

                        self.e = self.cf.get_element_text()

                        time.sleep(1)

                    self.cf.clickDonebtn()
                    self.folder_number += 1
                    time.sleep(1)

                except Exception as e:
                    print(e)

        self.cf.selectFolder()
        time.sleep(2)