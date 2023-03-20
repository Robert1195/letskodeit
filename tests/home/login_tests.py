from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import time


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        base_URL = "https://letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(3)

        lp = LoginPage(driver)
        lp.login("space.ship199511@gmail.com", "Robert")

        result = lp.verify_login_successful()
        assert result == True


if __name__ == '__main__':
    unittest.main(verbosity=2)
