import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory


# run for every method
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


# run at the beginning and at the end of the module
@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

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
