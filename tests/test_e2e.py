import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#from pageObjects.CheckoutPage import CheckOutPage
#from pageObjects.HomePage import HomePage
#from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setup")
# we want to remove fixtures from test cases files into seperate class/file
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage

from utilities.BaseClass import BaseClass


class TestOne(BaseClass) : # all of test cases gathered in one class and we can use utilities in BaseClass for any testcase

    def test_e2e(self):
        # using page object we will optimize the code
        log = self.getLogger()
        homepage = HomePage(self.driver) # pass local driver here to the homepage class
        checkoutpage = homepage.shopItems() # here we clicked on shop button in home page -> we made optimization here
        log.info("Get all card titles")
        # below are belong to CheckoutPage class
        #checkoutpage = CheckoutPage(self.driver)
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter().click() # click on add
        checkoutpage.CheckoutItems_1().click() # click on checkout_1
        confirmPage = checkoutpage.CheckoutItems_2() # click on checkout_2

        # below are belong to ConfirmationPage class
        #confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name as ind")
        confirmPage.getCountryName().send_keys("ind")
        self.verifyLinkPresence("India") # call explicit wait from baseClass
        confirmPage.SelCountryName().click()
        confirmPage.CheckBox().click()
        confirmPage.Submit().click()
        Text = confirmPage.GetSucMessage().text
        log.info("Text recieved from apllication is" + Text )
        assert "Success! Thank you!" in Text


