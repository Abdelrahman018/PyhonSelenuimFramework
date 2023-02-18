from selenium.webdriver.common.by import By

#from pageObjects.ConfirmPage import ConfirmPage


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver
        #self.driver.find_element(By.ID, "country").send_keys("ind")

    GetcountryName = (By.ID, "country")
    countyName = (By.LINK_TEXT,"India")
    Checkbox = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    SubmitButton = (By.CSS_SELECTOR,"[type='submit']")
    SucMsg = (By.CLASS_NAME,"alert-success")

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.GetcountryName)

    def SelCountryName(self):
        return self.driver.find_element(*ConfirmPage.countyName)

    def CheckBox(self):
        return self.driver.find_element(*ConfirmPage.Checkbox)

    def Submit(self):
        return self.driver.find_element(*ConfirmPage.SubmitButton)

    def GetSucMessage(self):
        return self.driver.find_element(*ConfirmPage.SucMsg)

