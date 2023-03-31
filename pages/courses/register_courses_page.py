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
    _course = "//div[@class='zen-course-list']//h4[contains(text(),'{0}')]"  # by xpath
    _all_courses = "div[class='zen-course-list']"  # by css
    _enroll_button = "//button[text()='Enroll in Course']"
    _cc_num = "input[placeholder='Card Number']"  # by css
    _cc_exp = "input[placeholder='MM / RR']"  # by css
    _cc_cvv = "input[placeholder='Security CodeR']"  # by css
    _buy_btn = "button[class*='sp-buy btn']"  # by css
    _enroll_error_message = "//span[text()='Numer karty jest niepoprawny.']"  # by xpath
    _iframe_num = "//iframe[@title='Bezpieczne pole wprowadzania numeru karty']" # by xpath
    _iframe_exp = "//iframe[@title='Bezpieczne pole wprowadzania terminu ważności']" # by xpath
    _iframe_cvc = "//iframe[@title='Bezpieczne pole wprowadzania CVC']" # by xpath

    def click_all_courses_lick(self):
        self.element_click(self._all_courser_link, "xpath")

    def enter_course_name(self, name):
        self.sendKeys(name, self._search_box, "css")

    def select_course_to_enroll(self, full_course_name):
        _course_locator = self._course.format(full_course_name)
        self.element_click(_course_locator, "xpath")

    def click_enroll_btn(self):
        self.element_click(self._enroll_button, "xpath")

    def scroll_page(self):
        self.web_scroll(direction="down")
    def enter_card_num(self, num):
        self.change_iframe(self._iframe_num, "xpath")
        self.sendKeys(num, self._cc_num, "css")
        self.driver.switch_to.default_content()

    def enter_card_exp(self, exp):
        time.sleep(2)
        self.change_iframe(self._iframe_exp, "xpath")
        self.sendKeys(exp, self._cc_exp, "css")
        time.sleep(2)
    def enter_card_cvv(self, cvv):
        self.sendKeys(cvv, self._cc_cvv, "css")
    def click_by_btn(self):
        self.element_click(self._buy_btn, "css")
    def enter_credit_card_info(self, num, exp, cvv):
        pass










