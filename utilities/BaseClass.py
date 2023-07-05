"""This class hold any reusable functions and all fixtures
 Anything can be used by multiple test cases """
import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")  # Definition of setup method is in conftest
class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # File handler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_presence(self, text):  # Explicit wait for linked text
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             ((By.LINK_TEXT, text)))

    def select_option_by_text(self, locator, text): # for drop down menu
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def implicit_wait(self, seconds):  # Implicit wait
        self.driver.implicitly_wait(seconds)

    def scroll_down(self):
        self.driver.execute_script("""
    var element = document.querySelector('.content');
    element.scrollTop = element.scrollHeight;
    """)





