# the concept of page objects is to hold all locators of every single page in the flow into single class
# to be more readable
# we will make single method for each and every locator
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver # set the driver from test case to be local her also

    shop = (By.CSS_SELECTOR, "a[href*='shop']") # class variable

    name =(By.NAME,"name")
    password = (By.ID,"exampleInputPassword1")
    email = (By.CSS_SELECTOR,"input[name ='email']")
    checkbox = (By.CLASS_NAME,"form-check-label")
    gender= (By.ID, "exampleFormControlSelect1")
    radiobut = (By.CSS_SELECTOR,"label[for='inlineRadio2']")
    submit = (By.XPATH,"//input[@type='submit']")
    message = (By.CLASS_NAME,"alert")


    def shopItems(self): # this method is the navigation to next page
        self.driver.find_element(*HomePage.shop).click() # equivelant to self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getPass(self):
            return self.driver.find_element(*HomePage.password)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
            return self.driver.find_element(*HomePage.checkbox)

    def getRadiobut(self):
        return self.driver.find_element(*HomePage.radiobut)

    def getSubmitbut(self):
            return self.driver.find_element(*HomePage.submit)

    def getMsg(self):
            return self.driver.find_element(*HomePage.message)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
