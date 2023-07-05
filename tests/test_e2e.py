from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.AddEmployeePageData import AddEmployeeData
from TestData.AddDepsPageData import AddDepsData
from selenium.webdriver.common.by import By

import pytest


class TestOne(BaseClass):
    """All of test cases gathered in one class and
       we can use utilities in BaseClass for any test case"""


    @pytest.mark.skip(reason="skipping this test for now")
    def test_booking(self):
        # using page object we will optimize the code
        self.implicit_wait(8)  # Global implicit wait
        log = self.get_logger()
        login_page = LoginPage(self.driver)  # Pass local driver here
        log.info("Enter user credentials")
        login_page.get_email_naeem().send_keys("test2@admin.com")  # enter email
        login_page.get_pass_naeem().send_keys("123456")  # enter password

        # switch to home page
        homepage = login_page.home_tabs()
        log.info("View home page")
        homepage.get_booking_tab().click()  # click on booking tab

        # switch to booking list page
        bookings_page = homepage.booking_index()  # switch to bookings page
        log.info("View booking index page")
        bookings_page.get_search_bar().send_keys("معا")
        # here we better add explicit wait here to search bar results
        log.info("view specific user bookings")
        bookings_page.get_client_name().click()  # show client's booking
        assert ("Success" in "fail")

    @pytest.mark.skip(reason="skipping this another test for now")
    def test_pos_calender_booking(self):  # first pos test cases
        self.implicit_wait(15)  # Global implicit wait
        log = self.get_logger()
        login_page = LoginPage(self.driver)  # Pass local driver here
        log.info("Enter user credentials")
        login_page.get_email_naeem().send_keys("test2@admin.com")  # enter email
        login_page.get_pass_naeem().send_keys("123456")  # enter password



    @pytest.mark.skip(reason="skipping this another test for now")
    def test_add_employee(self,getData):
        self.implicit_wait(15)  # Global implicit wait
        log = self.get_logger()
        homepage = HomePage(self.driver) # Pass local driver here
        #log.info("Enter user credentials")

        #login_page.get_email_naeem().send_keys(
        #    "test2@admin.com")  # enter email
        #login_page.get_pass_naeem().send_keys("123456")  # enter password

        # switch to home page
        #homepage = login_page.home_tabs()
        #log.info("View home page")

#--------------------------- Start of test cases -------------------------------------
        #click on empolyees main
        homepage.get_employees_main_tab().click()

        # switch to employees
        empolyees_page = homepage.get_employees_page()
        log.info("View employees page")


        #switch to add employee page
        add_employees_page = empolyees_page.get_add_empolyee_page() # click add new employee



        self.select_option_by_text(add_employees_page.get_roles_menu(),getData["Role"])
        add_employees_page.get_branch_name_field().click()
        add_employees_page.get_arabic_name().send_keys(getData["arabic_name"])
        add_employees_page.get_english_name().send_keys(getData["English_name"])
        add_employees_page.get_email_field().send_keys(getData["Email"])

        # we need to add scroll down here
        self.scroll_down()

        add_employees_page.get_password_field().send_keys(getData["Password"])
        add_employees_page.get_mobile_field().send_keys(getData["Mobile_number"])

        add_employees_page.get_gender_menu().click() # click on gender field
        gender_options = add_employees_page.get_gender_group().find_elements(By.CLASS_NAME,"dropdown-option")

        for option in gender_options:
            if option.get_attribute('data-key') == getData["Gender"]:
                option.click()
                break

        add_employees_page.get_online_radio_button().click()
        add_employees_page.get_save_button().click()
        
        page_title = add_employees_page.get_page_title().text
        print(page_title)

        assert ("قائمة الموظفين" in page_title)

        #self.driver.quit()  # close the browser after each test case execution


        # we will create fixture special for this test case so we will not place it in conftest or BaseClass
    @pytest.fixture(params=AddEmployeeData.test_e2e_data_2)  # the test case will be executed three times
    def getData(self, request):
        return request.param



    def test_add_department(self,getData):
        self.implicit_wait(15)  # Global implicit wait
        homepage = HomePage(self.driver)
        homepage.get_branch_tab().click() # click on branch tab
        #switch
        deps_page = homepage.get_departments_page()# click on deps tab
        #switch
        add_deps_page = deps_page.get_add_new_dep_page() # click on add new dep button
        add_deps_page.get_arabic_name().send_keys(getData["dep_arabic_name"])
        add_deps_page.get_english_name().send_keys(getData["dep_english_name"])
        add_deps_page.get_image_upload().send_keys(getData["image_file"])
        add_deps_page.get_activate_radio_button().click()
        add_deps_page.get_save_button().click()



    @pytest.fixture(params=AddDepsData.test_e2e_data_deps)  # the test case will be executed one time
    def getData(self, request):
        return request.param













