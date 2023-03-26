from pages.home.login_page import LoginPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.clear_fields()
        self.lp.login("space.ship199511@gmail.com", "Robert")
        result = self.lp.verify_login_successful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("invalidemail@gmail.com", "invalid_password")
        result = self.lp.verify_login_failed()
        assert result == True
