import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# This is a session-level fixture for the driver.
# The driver object is initialized as None, and is updated in the setup fixture.
# Then it is accessible in other fixtures or tests via the driver fixture.
@pytest.fixture(scope="session")
def driver():
    driver_obj = {'driver': None}
    yield driver_obj
    # After all tests are done, close the driver if it exists
    #if driver_obj['driver'] is not None:
     #   driver_obj['driver'].close()

@pytest.fixture(scope="class")
def setup(request, driver):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("D:/Python_Automation_Udemy/ChromeDriver/chromedriver.exe")
        driver['driver'] = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("D:/Python_Automation_Udemy/FirefoxDriver/geckodriver.exe")
        driver['driver'] = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = Service("D:/Python_Automation_Udemy/IEDriver/msedgedriver.exe")
        driver['driver'] = webdriver.Edge(service=service_obj)

    driver['driver'].get("https://staging.cg.sa/") # open new window
    driver['driver'].maximize_window()

    # we will add login part here to be shared between all test cases
    driver['driver'].find_element(By.XPATH,
        '//input[@placeholder = "البريد الالكتروني"]').send_keys("test2@admin.com") # enter email

    driver['driver'].find_element(By.XPATH,
        '//input[@placeholder = \"كلمة المرور\"]').send_keys(
        "123456")  # enter password

    driver['driver'].find_element(By.XPATH,('//*[text() = \"تسجيل الدخول\"]')).click() # click login


    request.cls.driver = driver['driver'] #This allows you to use the driver within your test methods

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item._request.getfixturevalue('driver') # Get the driver from the fixture
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(driver['driver'], file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style=' \
                       '"width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)
