from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddSignatoryPage:

    click_signatory_icon_xpath= "//img[@src='./../../../../../assets/images/Icons/ADD_ICON.svg']"
    enter_name_xpath= "//input[@placeholder='Name']"
    enter_surname_xpath= "//input[@placeholder='Surname']"
    enter_email_xpath= "//input[@placeholder='Email']"
    click_priorities_name = "priority"
    click_KYC_required_name= "required_identity"
    click_add_btn_xpath= "//button[contains(text(),'ADD')]"
    click_send_btn_xpath= "//button[contains(text(), 'Send')]"
    enter_signatory_msg_xpath= "//input[@placeholder='Write a Message for signatories']"
    click_homepage_xpath = "//button[contains(text(), 'Homepage')]"

    def __init__(self,driver):
        self.driver= driver

    def clickAddSignatoryBtn(self):

        plus_icon= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_signatory_icon_xpath)))
        self.driver.execute_script("arguments[0].click();", plus_icon)

    def enterFirstName(self, signfirstName):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_name_xpath))).send_keys(signfirstName)

    def enterSurName(self, signsurame):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_surname_xpath))).send_keys(signsurame)

    def enterEmail(self, signEmail):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.enter_email_xpath))).send_keys(signEmail)

    def clickPrority(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME,self.click_priorities_name)))
        must_sign= self.driver.find_elements(By.NAME, self.click_priorities_name)
        must_sign[0].click()

    def clickKYC(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, self.click_KYC_required_name)))
        required_kyc= self.driver.find_elements(By.NAME, self.click_KYC_required_name)
        required_kyc[1].click()

    def clickAddBtn(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_add_btn_xpath))).click()

    def enterMessage(self, message):

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.enter_signatory_msg_xpath))).send_keys(message)


    def clickSendBtn(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_send_btn_xpath))).click()

    def clickHomePage(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.click_homepage_xpath))).click()
