from selenium.webdriver.common.by import By
from pageObjects.AddDepartmentsPage import AddDepartmentsPage

class DepartmentsPage:
    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here


    add_new_dep_button = (By.CSS_SELECTOR,".button.text-white.bg-theme-1.shadow-md.mr-2")

    def get_add_new_dep_page(self):
         self.driver.find_element(*DepartmentsPage.add_new_dep_button).click()
         add_deps_page = AddDepartmentsPage(self.driver)
         return add_deps_page

