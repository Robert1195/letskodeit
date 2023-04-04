from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp")
class InvalidCardNumberTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    def test_invalid_buy(self):
        """
        Invalid card number E2E test
        """
        self.rp.buy_course(name="Javascript", full_course_name="JavaScript for beginners", num="5111 1111 1111 1118", exp="01 / 25", cvv="1111")
        result = self.rp.verify_buy_failed()
        self.ts.mark(result, "Wrong card number verification")
        result_2 = self.rp.verify_if_buy_btn_is_disabled()
        self.ts.markFinal("test_invalid_buy", result_2, "Invalid card number test, buy button is disabled")

