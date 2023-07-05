from selenium.webdriver.common.by import By
from pageObjects.BookingsPage import BookingsPage
from pageObjects.PosPage import PosPage
from pageObjects.EmployeesPage import EmpolyeesPage
from pageObjects.DepartmentsPage import DepartmentsPage



class HomePage:

    def __init__(self, driver):
        self.driver = driver

    booking_tab = (By.XPATH, "//div[@class='side-menu__title'][contains(text(),'استعراض الحجوزات')]")
    bookingList_subTab = (By.XPATH,"//div[@class='side-menu__title'][contains(text(),'قائمة الحجوزات')]")
    bookingList_button = (By.CLASS_NAME, "text-3xl")
    pos_tab = (By.XPATH,"//div[@class='side-menu__title'][contains(text(),'الحجوزات / نقاط البيع')]")

    employees_main_tab =(By.XPATH,"/html[1]/body[1]/div[4]/nav[1]/ul[1]/li[4]/a[1]/div[2]") #abs xpath
    employees_sub_tab = (By.XPATH,"//html[1]/body[1]/div[4]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/div[2]")   #abs xpath

    branch_tab = (By.XPATH,"/html[1]/body[1]/div[4]/nav[1]/ul[1]/li[5]/a[1]/div[2]")
    departments_tab = (By.XPATH,"//body[1]/div[4]/nav[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]")

    def get_booking_tab(self):
        return self.driver.find_element(*HomePage.booking_tab)

    def booking_index(self):  # Navigation to next page(booking index page)
        self.driver.find_element(*HomePage.bookingList_subTab).click()
        bookings_page = BookingsPage(self.driver)
        return bookings_page

    def pos_page(self): #navigatin to POS page from home page
        self.driver.find_element(*HomePage.pos_tab).click()
        pos_page = PosPage(self.driver)
        return pos_page

    def get_employees_main_tab(self):
        return self.driver.find_element(*HomePage.employees_main_tab)

    def get_employees_page(self):  # navigation to employees page from home page
        self.driver.find_element(*HomePage.employees_sub_tab).click()
        employees_page = EmpolyeesPage(self.driver)
        return employees_page


    # navigation to deps page from home page
    # add locator of deps tab with click action
    def get_departments_page(self):
        self.driver.find_element(*HomePage.departments_tab).click()
        deps_page = DepartmentsPage(self.driver)
        return deps_page

    def get_booking_list_but(self):
        return self.driver.find_element(*HomePage.bookingList_button)

    def get_pos_tab(self):
        return self.driver.find_element(*HomePage.pos_tab)


    def get_branch_tab(self):
        return self.driver.find_element(*HomePage.branch_tab)







