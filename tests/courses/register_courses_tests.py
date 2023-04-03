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
        print("********************************")
        print(result)
        print("********************************")
        self.ts.markFinal("test_invalid_buy", result, "Wrong card number verification message")

