from selenium.webdriver.common.by import By


class PosPage:

    def __init__(self, driver):
        self.driver = driver  # Set the driver from test case to be local here

    search_bar = (By.XPATH, "//input[@placeholder='برجاء اختيار العميل']")
    calender_tab = (By.XPATH,"//div[@class='font-medium text-base'][contains(text(),'التقويم')]")

    services_tab = (By.XPATH,"//div[@class='font-medium text-base'][contains(text(),'الخدمات')]")
    products_tab = (By.XPATH,"//div[@class='font-medium text-base'][contains(text(),'المنتجات')]")
    newBookings_tab = (By.XPATH,"//div[@class='font-medium text-base'][contains(text(),'الحجوزات الجديدة')]")
    packages_tab = (By.XPATH,"//div[@class='font-medium text-base'][contains(text(),'الباقات')]")

    cart_icon = (By.CSS_SELECTOR,".rounded.rounded-full.bg-red-600.text-white.w-5.h-5.absolute")
    setting_icon = (By.CSS_SELECTOR,".p-2.rounded-lg.bg-white.mr-1.relative.block")

    day_back = (By.XPATH,"//button[@title='Previous اليوم']")
    day_forward = (By.XPATH,"//button[@title='Next اليوم']")

    #booking_slot = (By.XPATH,"//div[@class='fc-event-title' and contains(text(), 'testy') and following-sibling::div[contains(text(), '1 ص')]]")
    def get_search_bar(self):
        return self.driver.find_element(*PosPage.search_bar)

    def get_calender_tab(self):
        return self.driver.find_element(*PosPage.calender_tab)
    def get_services_tab(self):
        return self.driver.find_element(*PosPage.services_tab)
    def get_products_tab(self):
        return self.driver.find_element(*PosPage.products_tab)
    def get_newBookings_tab(self):
        return self.driver.find_element(*PosPage.newBookings_tab)
    def get_packages_tab(self):
        return self.driver.find_element(*PosPage.packages_tab)

    def get_cart_icon(self):
        return self.driver.find_element(*PosPage.cart_icon)
    def get_setting_icon(self):
        return self.driver.find_element(*PosPage.setting_icon)

    def get_day_back(self):
        return self.driver.find_element(*PosPage.day_back)

    def get_day_forward(self):
        return self.driver.find_element(*PosPage.day_forward)

    def get_booking_slot(self):
        return self.driver.find_element(*PosPage.booking_slot)










