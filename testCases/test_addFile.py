import time

import pytest
from selenium import webdriver

from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from pageObjects.UploadFilePage import UploadFilePage
from testCases.test_base import BaseTest

class Test_AddFile(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code

    file_path = testdata.file_path
    file_name= testdata.fileName
    file_description = testdata.fileDescription


    def test_addFile(self):

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(2)

        self.cf= CreateFolderPage(self.driver)
        self.cf.selectProject()
        time.sleep(2)
        self.cf.selectFileOption()
        time.sleep(2)
        self.cf.selectFolder()
        time.sleep(2)

        self.uf= UploadFilePage(self.driver)
        time.sleep(2)
        self.uf.clickAddFileBtn()
        self.uf.uploadFile(self.file_path)
        self.uf.enterFileName(self.file_name)
        self.uf.enterFileDescription(self.file_description)
        self.uf.clickDocType()
        self.uf.clickNextBtn()
        time.sleep(5)





