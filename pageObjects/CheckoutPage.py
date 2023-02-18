from selenium.webdriver.common.by import By

#from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_css_selector(".card-title a")
    # driver.find_element_by_xpath("//button[@class='btn btn-success']")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutItems_1 = (By.CLASS_NAME, "btn-primary")
    checkOutItems_2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckoutPage.cardFooter)

    def CheckoutItems_1(self):
        return self.driver.find_element(*CheckoutPage.checkOutItems_1)

    def CheckoutItems_2(self):
       self.driver.find_element(*CheckoutPage.checkOutItems_2).click()
       confirmPage = ConfirmPage(self.driver)
       return confirmPage


