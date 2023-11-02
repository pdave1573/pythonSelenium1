import pytest
from selenium import webdriver

def getDriver():
    setup()

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(20)
    print("Driver Set up done")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Pranav",
        "Project Name": "pythonSelenium",
        "Module Name": "facebook",
    }

# It is hook for delete/Modify Environment info to HTML Report
#@pytest.mark.optionalhook
#def pytest_metadata(metadata):
#    metadata.pop("JAVA_HOME", None)
#    metadata.pop("Plugins", None)