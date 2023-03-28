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

    def test_invalid(self):
        self.rp.click_all_courses_lick()