from pages.home.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.clear_fields()
        self.lp.login("space.ship199511@gmail.com", "Robert")
        result_1 = self.lp.verify_title()
        self.ts.mark(result_1, "Title Verified")
        result_2 = self.lp.verify_login_successful()
        self.ts.markFinal("test_valid_login", result_2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("invalidemail@gmail.com", "invalid_password")
        result = self.lp.verify_login_failed()
        assert result == True
