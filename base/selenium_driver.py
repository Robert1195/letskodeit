from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG, where="cmd")

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relativeFileName = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relativeFileName)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.error(f"Locator type is not supported/correct: {locator_type}")
            return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Element found with locator: {locator}, Locator Type: {locator_type}")
        except:
            self.log.error(f"Element not found with locator: {locator}, Locator Type: {locator_type}")
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
         Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info(f"Element found with locator: {locator}, Locator Type: {locator_type}")
        except:
            self.log.error(f"Element not found with locator: {locator}, Locator Type: {locator_type}")
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(f"Clicked on element with locator: {locator}, Locator Type: {locator_type}")
        except:
            self.log.error(f"Cannot clicked on element with locator: {locator}, Locator Type: {locator_type}")
            print_stack()

    def sendKeys(self, data, locator="", locator_type="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info(f"Send keys: '{data}' on element with locator: {locator}, Locator Type: {locator_type}")
        except:
            self.log.error(f"Cannot send keys: '{data}' on element with locator: {locator}, Locator Type: {locator_type}")
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info(f"Element found with locator: {locator}, Locator Type: {locator_type}")
                return True
            else:
                self.log.error(f"Element not found with locator: {locator}, Locator Type: {locator_type}")
                return False
        except:
            self.log.error("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def are_elements_present(self, locator, by_type):
        elements_list = self.driver.find_elements(by_type, locator)
        if len(elements_list) > 0:
            self.log.info("Elements found")
            return True
        else:
            self.log.error("Elements not found")
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10):
        element = None
        self.log.info("************ PO ELEMENT *********")
        try:
            self.log.info("************ PO TRY *********")
            byType = self.get_by_type(locator_type)
            self.log.info(f"************ PO BY TYPE *********", {byType})
            self.log.info("Waiting for maximum :: ", timeout, " :: seconds for element to be visible")
            self.log.info("************ Przed WAIT *********")
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                                ElementNotVisibleException,
                                                                                                ElementNotSelectableException])
            self.log.info("************ PO WAIT *********")
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeard on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def get_title(self):
        title = self.driver.title
        return title

    def web_scroll(self, direction="up"):
        """
        scroll the page up or down
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -500);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 500);")

    def change_iframe(self, locator="", locator_type="xpath"):
        """
        Method to change iframe
        """
        try:
            if locator == "default":
                self.driver.switch_to.default_content()
                self.log.info("iframe changed to default frame")
            else:
                iframe = self.get_element(locator, locator_type)
                self.driver.switch_to.frame(iframe)
                self.log.info(f"iframe changed to frame with locator: {locator}, Locator Type: {locator_type}")
        except:
            self.log.error(f"Cannot changed iframe to iframe with locator: {locator}, Locator Type: {locator_type}")
            print_stack()
