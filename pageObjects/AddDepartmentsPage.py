from selenium.webdriver.common.by import By

class AddDepartmentsPage:
    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here

    arabic_name_field = (By.XPATH, "//input[@name='name']")
    english_name_field = (By.XPATH, "//input[@name='name_en']")
    activate_radio_button =(By.XPATH,"//input[@value='1']")
    upload_image = (By.NAME,"image")
    save_button = (By.ID,"myP")



    def get_arabic_name(self):
        return self.driver.find_element(*AddDepartmentsPage.arabic_name_field)
    def get_english_name(self):
        return self.driver.find_element(*AddDepartmentsPage.english_name_field)

    def get_activate_radio_button(self):
        return self.driver.find_element(*AddDepartmentsPage.activate_radio_button)

    def get_image_upload(self):
        return self.driver.find_element(* AddDepartmentsPage.upload_image)
    def get_save_button(self):
        return self.driver.find_element(* AddDepartmentsPage.save_button)
