from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginTests:

    def test_valid_login(self):
        base_URL = "https://letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_URL)
        driver.implicitly_wait(3)

        login_link = driver.find_element(By.LINK_TEXT, "Sign Up or Log In")
        login_link.click()

        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys("space.ship199511@gmail.com")

        password_field = driver.find_element(By.ID, "login-password")
        password_field.send_keys("Robert")

        login_btn = driver.find_element(By.ID, "login")
        login_btn.click()

        user_icon = driver.find_element(By.XPATH, "//span[text()='My Account']")
        if user_icon is not None:
            print("Login successful")
        else:
            print("Login Failed")

        time.sleep(3)


chro = LoginTests()
chro.test_valid_login()
