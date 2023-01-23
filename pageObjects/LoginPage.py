from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    email_field_xpath = "//input[@placeholder='Your E-mail']"
    password_field_xpath= "//input[@placeholder='Password']"
    login_btn_class= "submit-btn"
    verification_code_name= "name"
    submit_btn_class= "submit-btn"

    def __init__(self,driver):
        self.driver= driver

    def enterEmail(self, email):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.email_field_xpath)))
        self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(email)

    def enterPassword(self, password):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.password_field_xpath)))
        self.driver.find_element(By.XPATH,self.password_field_xpath).send_keys(password)

    def clickLoginbtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.login_btn_class))).click()

    def enterverificationcode(self, verificationcode):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME,self.verification_code_name))).send_keys(verificationcode)

    def clicksubmitbutton(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.submit_btn_class))).click()