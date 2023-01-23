from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateProjectPage:
    main_create_project_btn_class= "heading"
    project_logo_ID= "file-input"
    project_name_xpath= "//input[@placeholder='Project Name']"
    create_project_btn_class= "create-btn"
    modal_error_msg_xpath= "//div[@id='swal2-content']"
    modal_done_btn_class= "alert-success-class"

    def __init__(self,driver):
        self.driver= driver

    def clickMainprojectbtn(self):

        element= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.main_create_project_btn_class)))
        #element= self.driver.find_element(By.CLASS_NAME,self.main_create_project_btn_class)
        self.driver.execute_script('arguments[0].click()', element)

    def uploadLogo(self, logo):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID,self.project_logo_ID))).send_keys(logo)

    def enterProjectname(self, projectname):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.project_name_xpath))).send_keys(projectname)

    def clickCreatebtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.create_project_btn_class))).click()

    def get_element_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.modal_error_msg_xpath)))
        return element.text

    def clearprojectnamefield(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.project_name_xpath))).clear()

    def clickDonebtn(self):

        element= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.modal_done_btn_class)))
        self.driver.execute_script('arguments[0].click()', element)