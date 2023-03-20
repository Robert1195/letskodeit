from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):

    base_URL = "https://letskodeit.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(4)

    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.base_URL)
        self.lp.login("space.ship199511@gmail.com", "Robert")
        result = self.lp.verify_login_successful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.base_URL)
        self.lp.login("invalidemail@gmail.com", "invalid_password")
        result = self.lp.verify_login_failed()
        assert result == True


if __name__ == '__main__':
    unittest.main(verbosity=2)
