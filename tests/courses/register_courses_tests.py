from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.status import Status
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class InvalidCardNumberTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterCoursesPage(self.driver)
        self.ts = Status(self.driver)

    def test_invalid(self):
        self.rp.click_all_courses_lick()
        self.rp.enter_course_name("Javascript")
        self.rp.select_course_to_enroll("JavaScript for beginners")
        self.rp.click_enroll_btn()
        self.rp.scroll_page()
        self.rp.enter_card_num(num="5111 1111 1111 1118")
        self.rp.enter_card_exp(exp="01 / 25")
