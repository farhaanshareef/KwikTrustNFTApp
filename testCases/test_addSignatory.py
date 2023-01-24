import time

import pytest
from selenium import webdriver

from pageObjects.AddSignatoryPage import AddSignatoryPage
from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from pageObjects.UploadFilePage import UploadFilePage
from testCases.test_base import BaseTest

class Test_AddSignatory(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code

    file_path = testdata.file_path
    file_name= testdata.fileName
    file_description = testdata.fileDescription

    signatory_fname= testdata.signatory_firstname
    signatory_sname = testdata.signatory_surname
    signatory_email= testdata.signatory_list
    signatory_msg= testdata.signatory_msg


    def test_Signatory(self):

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
        time.sleep(2)

        self.asp = AddSignatoryPage(self.driver)

        i=0
        #for i in range(1,3):
        while i<3:

            self.asp.clickAddSignatoryBtn()

            self.asp.enterFirstName(self.signatory_fname)

            time.sleep(1)

            self.asp.enterSurName(self.signatory_sname)

            time.sleep(1)

            self.asp.enterEmail(self.signatory_email[i])

            time.sleep(1)

            self.asp.clickPrority()

            self.asp.clickKYC()

            self.asp.clickAddBtn()

            time.sleep(1)
            i+=1

        self.asp.enterMessage(self.signatory_msg)
        self.asp.clickSendBtn()
        self.asp.clickHomePage()
