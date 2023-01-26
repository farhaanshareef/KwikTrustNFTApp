from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StdNFTMintingPage:

    click_start_btn_xpath= "//button[contains(text(),'Start')]"
    click_connect_btn_xpath = "//button[contains(text(),'Connect')]"
    click_std_NFT_option_class= "m-auto"
    click_upload_file_xpath= "//button[contains(text(), '+ Upload file')]"
    click_nft__class= "image-section"
    click_mint_btn_class= "color-white"
    click_copyright_name= "copyright"
    click_next_btn_xpath= "//button[contains(text(), 'Next')]"
    click_currency_dropdown_xpath= "//span[contains(text(),'Select')]"
    click_usd_currency_xpath = "//div[@class='network-names'][normalize-space()='USD']"
    click_KTX_currency_xpath= "//div[@class='network-names'][normalize-space()='KTX']"
    click_pay_btn_xpath= "//button[contains(text(),'PAY')]"
    switch_frame_xpath= "//iframe[@title='Secure payment input frame']"
    enter_card_number_ID = "Field-numberInput"
    enter_expiry_date_XPATH ="//input[@placeholder='MM / YY']"
    enter_cvc_XPATH = "//input[@placeholder='CVC']"
    click_ok_btn_XPATH ="//button[@id='okButton']"
    click_stripe_pay_btn= "//button[contains(text(),'Pay')]"


    def __init__(self,driver):
        self.driver= driver

    def clickSuperNFToption(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.click_std_NFT_option_class)))
        standard_nft_btn = self.driver.find_elements(By.CLASS_NAME, self.click_std_NFT_option_class)
        self.driver.execute_script('arguments[0].click()', standard_nft_btn[0])

    def clickStartbtn(self):

        start_btn= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_start_btn_xpath)))
        self.driver.execute_script("arguments[0].click();", start_btn)

    def clickConnectBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_connect_btn_xpath))).click()

    def clickStdNFTBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_std_NFT_option_class)))

        standard_nft_btn = self.driver.find_elements(By.CLASS_NAME, self.click_std_NFT_option_class)

        self.driver.execute_script('arguments[0].click()', standard_nft_btn[0])

    def clickUploadFilebtn(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_upload_file_xpath)))

        upload_file = self.driver.find_element(By.XPATH, self.click_upload_file_xpath)

        self.driver.execute_script('arguments[0].click()', upload_file)

    def getNFTcount(self):

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, self.click_nft__class)))
            image = self.driver.find_elements(By.CLASS_NAME, self.click_nft__class)
            length_nft = len(image)
            return int(length_nft)

        except:
            return 0

    def clickNFT(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_nft__class))).click()
        i=0
        while i < self.getNFTcount():
            image = self.driver.find_elements(By.CLASS_NAME, self.click_nft__class)
            image[i].click()
            i += 1

    def clickMintBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, self.click_mint_btn_class))).click()

    def clickRadioBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, self.click_copyright_name)))

        radio_btn = self.driver.find_elements(By.NAME, self.click_copyright_name)
        radio_btn[0].click()

    def clickNextBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_next_btn_xpath))).click()

    def clickSelectCurrency(self):

        select_dropdown= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_currency_dropdown_xpath)))
        self.driver.execute_script('arguments[0].click()', select_dropdown)

    def clickUSDCurrency(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_usd_currency_xpath)))
        usd_currency= self.driver.find_element(By.XPATH, self.click_usd_currency_xpath)
        self.driver.execute_script('arguments[0].click()', usd_currency)

    def clickKTXCurrency(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_KTX_currency_xpath)))
        KTX_currency= self.driver.find_element(By.XPATH, self.click_KTX_currency_xpath)
        self.driver.execute_script('arguments[0].click()', KTX_currency)

    def clickPayBtn(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_pay_btn_xpath)))
        pay_btn= self.driver.find_element(By.XPATH, self.click_pay_btn_xpath)
        self.driver.execute_script('arguments[0].click()', pay_btn)

    def switchframestripe(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.switch_frame_xpath)))
        iframe_by_title = self.driver.find_element(By.XPATH, self.switch_frame_xpath)
        self.driver.switch_to.frame(iframe_by_title)

    def entercardDetails(self, cardnumber, expirydate, cvc):

        card_number = self.driver.find_element(By.ID, self.enter_card_number_ID).send_keys(cardnumber)

        expiry_date= self.driver.find_element(By.XPATH, self.enter_expiry_date_XPATH).send_keys(expirydate)

        cvc= self.driver.find_element(By.XPATH, self.enter_cvc_XPATH).send_keys(cvc)

    def clickStripePaybtn(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_stripe_pay_btn)))
        pay_btn = self.driver.find_element(By.XPATH, self.click_stripe_pay_btn)
        self.driver.execute_script('arguments[0].click()', pay_btn)

    def clickOkBtn(self):
        WebDriverWait(self.driver, 120).until(
            EC.element_to_be_clickable((By.XPATH, self.click_ok_btn_XPATH)))
        ok_btn = self.driver.find_element(By.XPATH, self.click_ok_btn_XPATH)
        self.driver.execute_script('arguments[0].click()', ok_btn)





