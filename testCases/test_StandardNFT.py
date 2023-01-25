import time

import pytest
from selenium import webdriver

from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from pageObjects.MetaMask import MetaMaskPage
from pageObjects.StandardNFTMintingPage import StdNFTMintingPage
from pageObjects.UploadFilePage import UploadFilePage
from testCases.test_base import BaseTest

class Test_StandardNFT(BaseTest):

    baseURL = testdata.app_url
    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code
    metamask_wallet_pass= testdata.metaMask_wallet_pass

    file_path = testdata.nft_file_path
    file_name = testdata.nft_file_Name
    file_description = testdata.nft_file_Description

    card_number= testdata.card_number
    cvc_number= testdata.card_cvc
    expiry_date= testdata.card_expiry_date

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
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)

        self.sn.clickStdNFTBtn()
        time.sleep(1)
        self.sn.clickUploadFilebtn()
        time.sleep(1)

        self.uf= UploadFilePage(self.driver)
        self.uf.uploadFile(self.file_path)
        self.uf.enterFileName(self.file_name)
        self.uf.enterFileDescription(self.file_description)
        self.uf.clickDocType()
        self.uf.clickNextBtn()
        time.sleep(1)

        self.sn.clickNFT()
        time.sleep(1)

        self.sn.clickMintBtn()
        self.sn.clickRadioBtn()
        self.sn.clickNextBtn()
        self.sn.clickSelectCurrency()
        time.sleep(2)
        self.sn.clickUSDCurrency()
        time.sleep(1)
        self.sn.clickPayBtn()
        time.sleep(5)
        self.sn.switchframestripe()
        self.sn.entercardDetails(self.card_number, self.expiry_date, self.cvc_number)
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.sn.clickPayBtn()
        time.sleep(5)