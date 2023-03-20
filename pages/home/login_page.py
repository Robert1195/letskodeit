from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    _login_link = "Sign Up or Log In"
    _email_field = "email"
    _password_field = "login-password"
    _login_btn = "login"

    def get_login_link(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def get_email_field(self):
        return self.driver.find_element(By.ID, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self._password_field)

    def get_login_btn(self):
        return self.driver.find_element(By.ID, self._login_btn)

    def click_login_link(self):
        self.get_login_link().click()

    def enter_email(self, email):
        self.get_email_field().send_keys(email)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def click_login_btn(self):
        self.get_login_btn().click()

    def login(self, email, password):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()
