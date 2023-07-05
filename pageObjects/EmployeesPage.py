from selenium.webdriver.common.by import By
from pageObjects.AddEmployeePage import AddEmpolyeesPage
class EmpolyeesPage:

    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here

    add_empolyee_button= (By.CSS_SELECTOR,".button.text-white.bg-theme-1.shadow-md.mr-2")


    def get_add_empolyee_page(self):
        self.driver.find_element(*EmpolyeesPage.add_empolyee_button).click()
        add_employees_page = AddEmpolyeesPage(self.driver)
        return add_employees_page
