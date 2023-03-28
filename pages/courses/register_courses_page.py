import logging
import utilities.custom_logger as cl
import time
from base.basepage import BasePage
from selenium import webdriver


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG, where="file")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    _all_courser_link = "//a[text()='ALL COURSES']"  # by xpath
    _search_box = "input[id='search']"  # by css
    _course = f"//div[@class='zen-course-list']//h4[contains(text(),'{0}')]"  # by xpath
    _all_courses = "div[class='zen-course-list']"  # by css
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "cardnumber"  # by name
    _cc_exp = "exp-date"  # by name
    _cc_cvv = "cvc"  # by name
    _submit_enroll = "button[class*='sp-buy btn']"  # by css
    _enroll_error_message = "//span[text()='Numer karty jest niepoprawny.']"  # by xpath

    def click_all_courses_lick(self):
        self.element_click(locator=self._all_courser_link, locator_type="xpath")


