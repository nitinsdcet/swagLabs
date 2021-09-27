import pytest
from selenium import webdriver
# import allure


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("launching chrome browser......")
        driver = webdriver.Chrome(executable_path="C:/Nitin/Drivers/chromedriver_win32/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox driver")
    else:
        driver = webdriver.Ie
    return driver


def pytest_addoption(parser):   # this will get value from CLI/hook
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):    # this will return browser value to set up method
    return request.config.getoption("--browser")

# ########Pytest HTML Report ########
# It is hook to delete/modify environment info to HTML Report


def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag Labs'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Nitin'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)







