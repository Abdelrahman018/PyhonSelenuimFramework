from selenium.webdriver.common.by import By

class AddEmpolyeesPage:
    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here


    roles_menu = (By.XPATH,"//select[@name='role_id']")
    branch_name_field = (By.XPATH,"//option[@value='78']") # select first branch in the menu
    arabic_name_field =(By.NAME,"name")
    english_name_field = (By.NAME,"name_en")
    email_field = (By.NAME, "email")
    password_field = (By.NAME, "password")
    mobile_field = (By.ID, "phone")
    gender_menu=(By.XPATH,"//div[@class='select-label']")

    gender_group = (By.XPATH,"//ul[@class='dropdown-optgroup']")

    enable_online_radio_button =(By.XPATH,"//div[10]//div[1]//input[2]")
    save_button = (By.XPATH,"//button[@value='Submit']")
    page_title = (By.XPATH,"//a[@class='breadcrumb--active']")

    def get_roles_menu(self):
        return self.driver.find_element(*AddEmpolyeesPage.roles_menu)
    def get_branch_name_field(self):
        return self.driver.find_element(*AddEmpolyeesPage.branch_name_field)
    def get_arabic_name(self):
        return self.driver.find_element(*AddEmpolyeesPage.arabic_name_field)
    def get_english_name(self):
        return self.driver.find_element(*AddEmpolyeesPage.english_name_field)

    def get_email_field(self):
        return self.driver.find_element(*AddEmpolyeesPage.email_field)
    def get_password_field(self):
        return self.driver.find_element(*AddEmpolyeesPage.password_field)
    def get_mobile_field(self):
        return self.driver.find_element(*AddEmpolyeesPage.mobile_field)
    def get_gender_menu(self):
        return self.driver.find_element(*AddEmpolyeesPage.gender_menu)
    def get_online_radio_button(self):
        return self.driver.find_element(*AddEmpolyeesPage.enable_online_radio_button)
    def get_save_button(self):
        return self.driver.find_element(*AddEmpolyeesPage.save_button)

    def get_page_title(self):
        return self.driver.find_element(*AddEmpolyeesPage.page_title)

    def get_gender_group(self):
        return self.driver.find_element(*AddEmpolyeesPage.gender_group)
