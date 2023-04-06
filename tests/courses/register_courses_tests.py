from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data


@pytest.mark.usefixtures("oneTimeSetUp")
@ddt
class InvalidCardNumberTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)
    @data(*get_csv_data("testdata.csv"))
    @unpack
    def test_invalid_buy(self, course_name, card_number, exp_num, cvv_num):
        """
        Invalid card number E2E test
        """
        self.rp.buy_course(name=course_name, full_course_name=course_name, num=card_number, exp=exp_num, cvv=cvv_num)
        result = self.rp.verify_buy_failed()
        self.ts.mark(result, "Wrong card number verification")
        result_2 = self.rp.verify_if_buy_btn_is_disabled()
        self.ts.markFinal("test_invalid_buy", result_2, "Invalid card number test, buy button is disabled")
        self.rp.click_all_courses_lick()

