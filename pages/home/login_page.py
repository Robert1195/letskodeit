from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        login_link = self.driver.find_element(By.LINK_TEXT, "Sign Up or Log In")
        login_link.click()

        email_field = self.driver.find_element(By.ID, "email")
        email_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "login-password")
        password_field.send_keys("Robert")

        login_btn = self.driver.find_element(By.ID, "login")
        login_btn.click()
