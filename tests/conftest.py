import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


# run for every method
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def LoginOneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


# run at the beginning and at the end of the module
@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("space.ship199511@gmail.com", "Robert")

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
