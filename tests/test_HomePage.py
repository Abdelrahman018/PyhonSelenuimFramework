# this file catch all homepage related test cases -> fill the form in https://www.rahulshettyacademy.com/angularpractice/

from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

#from TestData.HomePageData import HomePageData
from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("Firstname is "+ getData["Firstname"])
        homepage.getName().send_keys(getData["Firstname"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPass().send_keys(getData["Password"])
        homepage.getCheckbox().click()
        self.selectOptionByText(homepage.getGender(),getData["Gender"])
        homepage.getRadiobut().click()  # click radio button
        homepage.getSubmitbut().click()
        message = homepage.getMsg().text
        # print(message)

        assert ("Success" in message)  # if condition is false it will print error -- just test case to validate messgae appear after submit
        self.driver.refresh() # refesh the page to load new datasets after each exection

    # we will create fixture special for this test case so we will not place it in conftest or BaseClass
    @pytest.fixture(params = HomePageData.test_HomePage_data) # the test case will be executed two time with two datasets
    def getData(self, request):
        return request.param



