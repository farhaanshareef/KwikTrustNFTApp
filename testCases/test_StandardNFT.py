import time

import pytest
from selenium import webdriver

from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from pageObjects.MetaMask import MetaMaskPage
from pageObjects.StandardNFTMintingPage import StdNFTMintingPage
from testCases.test_base import BaseTest

class Test_StandardNFT(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code
    metamask_wallet_pass= testdata.metaMask_wallet_pass

    def test_StandardNFT(self):

        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(1)

        self.cf = CreateFolderPage(self.driver)
        self.cf.selectProject()
        time.sleep(1)

        self.sn= StdNFTMintingPage(self.driver)
        self.sn.clickSuperNFToption()
        time.sleep(1)
        self.sn.clickStartbtn()
        time.sleep(1)
        self.sn.clickConnectBtn()
        time.sleep(1)

        self.mw = MetaMaskPage(self.driver)
        self.mw.openMetaMask()
        self.mw.enterPassword(self.metamask_wallet_pass)
        self.mw.clickUnblockBtn()
        time.sleep(2)
        self.mw.switchWindow()

