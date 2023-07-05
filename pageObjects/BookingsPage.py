from selenium.webdriver.common.by import By


class BookingsPage:

    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here

    search_bar = (By.CLASS_NAME, "form-control")
    client_name = (By.XPATH, "//span[contains(text(), 'معاذ')]")

    def get_search_bar(self):
        return self.driver.find_element(*BookingsPage.search_bar)

    def get_client_name(self):
        return self.driver.find_element(*BookingsPage.client_name)








