import pytest
from selenium import webdriver


# run for every method
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


# run at the beginning and at the end of the module
@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    if browser == "chrome":
        base_URL = "https://letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(4)
        print("Running tests on Chrome")
    else:
        base_URL = "https://letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(4)
        print("Running tests in Firefox")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running conftest demo one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--env", help="Type of environment")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")
