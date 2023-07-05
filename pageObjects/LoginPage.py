from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here

    # Enter email
    user_email = (By.XPATH, "//input[@placeholder = \"البريد الالكتروني\"]")
    # Enter password
    user_pass = (By.XPATH, "//input[@placeholder = \"كلمة المرور\"]")
    # Click on login
    Login_button = (By.XPATH, "//*[text() = \"تسجيل الدخول\"]")

    # this method is the navigation to next page(home page)
    def home_tabs(self):
        self.driver.find_element(*LoginPage.Login_button).click()
        homepage = HomePage(self.driver)
        return homepage

    def get_email_naeem(self):
        return self.driver.find_element(*LoginPage.user_email)

    def get_pass_naeem(self):
        return self.driver.find_element(*LoginPage.user_pass)


