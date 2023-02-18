import pytest
from selenium import webdriver
import time
driver = None

#chrome driver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser): # this method to let pytest identify varaible in runtime from cmd
    # we want this to choose browser type at runtime -> Ex: py.test --browser_name Firefox
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class") # mean execute it once in the scope of the class not every methods in the class - if remove scope = class it will be in the scope of every method
def setup(request): # invoke the browser
    global driver # make driver variable is global for setup and _capture_screenshot methods
    browser_name = request.config.getoption("browser_name") # here we get the brower name you entered in cmd
    if browser_name == "chrome":
        service_obj = Service("D:\Python_Automation_Udemy\ChromeDriver\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("D:\Python_Automation_Udemy\FirefoxDriver\geckodriver.exe")
        driver = webdriver.Firefox(service = service_obj)
    elif browser_name == "IE":
        service_obj = Service("D:\Python_Automation_Udemy\IEDriver\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/") # we can paramatrizartion here same as when choose browser name like in pytest_addoption method
    driver.maximize_window()
    request.cls.driver = driver # here we pass this local driver to the class in test_e2e file
    yield
    driver.close()


# whenever a test case fail control will be directed to next method
# we use this to get a screenshot into the report whenever a test case fail
# below code is like edit the html report format to have screenshot in it
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
