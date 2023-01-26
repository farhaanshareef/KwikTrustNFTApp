from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferNFTPage:

    click_view_btn_class= "w-100"
    click_transfer_btn_xpath= "//button[contains(text(),'Transfer')]"
    enter_wallet_address_xpath= "//input[@placeholder='Wallet address']"
    click_send_btn_xpath= "//button[contains(text(),'Send')]"
    enter_verification_code_name= "name"
    click_submit_btn_class= "submit-btn"
    click_connect_btn_xpath= "//button[contains(text(),'Connect')]"

    def __init__(self,driver):
        self.driver= driver

    def clickNFT(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.click_view_btn_class)))

        view_btn = self.driver.find_elements(By.CLASS_NAME, self.click_view_btn_class)
        view_btn[2].click()

    def clickTransferBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_transfer_btn_xpath)))

        transfer_btn = self.driver.find_element(By.XPATH, self.click_transfer_btn_xpath).click()

    def enterWalletaddr(self, wallet_address):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_wallet_address_xpath)))

        receiver_wallet = self.driver.find_element(By.XPATH, self.enter_wallet_address_xpath).send_keys(wallet_address)

    def clickSendbtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_send_btn_xpath))).click()

    def enterVerificationcode(self, verificationcode):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_verification_code_name)))

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME,self.enter_verification_code_name))).send_keys(verificationcode)

    def clicksubmitbutton(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.click_submit_btn_class))).click()

    def clickConnectBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_connect_btn_xpath))).click()



