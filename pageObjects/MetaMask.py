import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MetaMaskPage:

    enter_password_field_ID= "password"
    click_unlock_btn_class= "btn-default"
    click_confirm_btn_css= ".btn--rounded.btn-primary"

    def __init__(self,driver):
        self.driver= driver

    def openMetaMask(self):

        self.driver.execute_script("window.open('about:blank', 'tab2');")

        self.driver.switch_to.window('tab2')

        tab2 = self.driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")

    def enterPassword(self, password):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,self.enter_password_field_ID))).send_keys(password)

    def clickUnblockBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.click_unlock_btn_class))).click()
        time.sleep(5)
        self.driver.close()

    def switchWindow(self):

        self.driver.switch_to.window(self.driver.window_handles[0])

    def clickConfirmBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_confirm_btn_css)))

        # click on the next button in MetaMask
        next_btn = self.driver.find_element(By.CSS_SELECTOR, self.click_confirm_btn_css)

        self.driver.execute_script('arguments[0].click()', next_btn)
