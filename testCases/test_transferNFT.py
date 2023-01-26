import time

import pytest
from selenium import webdriver

from pageObjects.CreateFolderPage import CreateFolderPage
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from pageObjects.MetaMask import MetaMaskPage
from pageObjects.StandardNFTMintingPage import StdNFTMintingPage
from pageObjects.TransferNFT import TransferNFTPage
from testCases.test_base import BaseTest

class Test_Transfer(BaseTest):

    email = testdata.file_uploader_email
    password = testdata.file_uploader_password
    verification_code= testdata.verification_code
    wallet_address= testdata.user_hyperledger_address
    metamask_wallet_pass = testdata.metaMask_wallet_pass

    card_number = testdata.card_number
    cvc_number = testdata.card_cvc
    expiry_date = testdata.card_expiry_date

    @pytest.mark.skip
    def test_transfer_card(self):
        self.lp= LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(2)

        self.cf = CreateFolderPage(self.driver)
        self.cf.selectProject()
        time.sleep(1)

        self.sn = StdNFTMintingPage(self.driver)
        self.sn.clickSuperNFToption()
        time.sleep(5)

        self.tn= TransferNFTPage(self.driver)
        self.tn.clickNFT()
        self.tn.clickTransferBtn()
        self.tn.enterWalletaddr(self.wallet_address)
        self.tn.clickSendbtn()

        time.sleep(20)
        self.lp.enterverificationcode(self.verification_code)
        time.sleep(10)
        self.lp.clicksubmitbutton()

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
        self.sn.clickStripePaybtn()
        self.sn.clickOkBtn()
        time.sleep(2)

    def test_transfer_MetaMask(self):
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginbtn()
        self.lp.enterverificationcode(self.verification_code)
        self.lp.clicksubmitbutton()
        time.sleep(2)

        self.cf = CreateFolderPage(self.driver)
        self.cf.selectProject()
        time.sleep(1)

        self.sn = StdNFTMintingPage(self.driver)
        self.sn.clickSuperNFToption()
        time.sleep(5)

        self.tn = TransferNFTPage(self.driver)
        self.tn.clickNFT()
        self.tn.clickTransferBtn()
        self.tn.enterWalletaddr(self.wallet_address)
        self.tn.clickSendbtn()

        time.sleep(10)
        self.lp.enterverificationcode(self.verification_code)
        time.sleep(10)
        self.lp.clicksubmitbutton()

        self.sn.clickSelectCurrency()
        time.sleep(2)
        self.sn.clickKTXCurrency()
        time.sleep(1)
        self.sn.clickPayBtn()
        self.sn.clickConnectBtn()

        self.mw = MetaMaskPage(self.driver)
        self.mw.openMetaMask()
        self.mw.enterPassword(self.metamask_wallet_pass)
        self.mw.clickUnblockBtn()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(1)

        self.sn.clickNextBtn()
        time.sleep(10)

        self.mw.openMetaMask()
        self.mw.clickConfirmBtn()
        time.sleep(5)



