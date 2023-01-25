from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateFolderPage:

    main_view_btn_class= "m-auto"
    click_file_option_xpath= "(//button[@class='pay-button d-flex m-auto'][normalize-space()='VIEW'])[5]"
    view_btn_xpath= "(//button[contains(text(),'VIEW')])"
    folder_no=1
    select_folder_xpath= "(//button[contains(text(),'VIEW')])" + "[" + str(folder_no) + "]"
    click_add_folder_btn_xpath= "//button[normalize-space()='+ New Folder']"
    enter_folder_name_field_xpath = "//input[@placeholder='Folder Name']"
    click_create_folder_btn_class= "create-btn"
    modal_error_msg_xpath= "//div[@id='swal2-content']"
    modal_done_btn_class= "alert-success-class"

    def __init__(self,driver):
        self.driver= driver

    def selectProject(self):

        i=2
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.main_view_btn_class)))
        projectno= self.driver.find_elements(By.CLASS_NAME, self.main_view_btn_class)
        self.driver.execute_script('arguments[0].click()', projectno[i])

    def selectFileOption(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,self.click_file_option_xpath)))
        select_file= self.driver.find_element(By.XPATH, self.click_file_option_xpath)
        self.driver.execute_script('arguments[0].click()', select_file)

    def getFoldercount(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,self.main_view_btn_class)))
        folder_list = self.driver.find_elements(By.CLASS_NAME, self.main_view_btn_class)
        length_folder = len(folder_list)
        return length_folder

    def selectFolder(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH,self.view_btn_xpath)))

        view_btn = self.driver.find_element(By.XPATH, self.select_folder_xpath)

        self.driver.execute_script('arguments[0].click()', view_btn)

    def createFolder(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.click_add_folder_btn_xpath))).click()

    def enterFoldername(self, folderName):

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,self.enter_folder_name_field_xpath))).send_keys(folderName)

    def clickCreatebtn(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.click_create_folder_btn_class))).click()

    def get_element_text(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.modal_error_msg_xpath)))
        return element.text

    def clearFoldernamefield(self):

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.enter_folder_name_field_xpath))).clear()

    def clickDonebtn(self):

        element= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,self.modal_done_btn_class)))
        self.driver.execute_script('arguments[0].click()', element)