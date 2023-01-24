from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadFilePage:

    click_add_file_btn_xpath= "//button[normalize-space()='+ New file']"
    upload_file_widget_ID= "undefined"
    enter_file_name_xpath= "//input[@placeholder='Name of file']"
    enter_file_description_xpath = "//input[@placeholder='Description of file']"
    click_file_type_class= "documentType"
    click_next_btn_class = "width100-pre"

    def __init__(self,driver):
        self.driver= driver

    def clickAddFileBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_add_file_btn_xpath))).click()

    def uploadFile(self, filepath):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,self.upload_file_widget_ID))).send_keys(filepath)

    def enterFileName(self, name):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_file_name_xpath))).send_keys(name)

    def enterFileDescription(self, desc):

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.enter_file_description_xpath))).send_keys(desc)

    def clickDocType(self):

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.click_file_type_class)))
        doc= self.driver.find_elements(By.CLASS_NAME, self.click_file_type_class)
        doc[4].click()

    def clickNextBtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.click_next_btn_class))).click()