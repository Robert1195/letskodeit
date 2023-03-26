from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl
import time


class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG, where="cmd")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    _login_xpath = "//a[text()='Sign In']"
    _email_field = "email"
    _password_field = "login-password"
    _login_btn = "login"
    _user_icon_xpath = "//span[text()='My Account']"
    _invalid_login_message_xpath = "//span[contains(text(),'Your username or password is invalid. Please try again.')]"
    _base_URL = "https://letskodeit.com/"

    # def get_login_link(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)

    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)

    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)

    # def get_login_btn(self):
    #     return self.driver.find_element(By.ID, self._login_btn)

    def click_login_link(self):
        self.element_click(self._login_xpath, locator_type="xpath")
    def enter_email(self, email):
        self.sendKeys(email, self._email_field)
    def enter_password(self, password):
        self.sendKeys(password, self._password_field)
    def click_login_btn(self):
        self.element_click(self._login_btn)
    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        time.sleep(1)
        self.click_login_btn()

    def verify_login_successful(self):
        result = self.is_element_present(self._user_icon_xpath, "xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self._invalid_login_message_xpath, "xpath")
        return result
