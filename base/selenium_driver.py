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

    def wait_for_element(self, locator, locator_type="id", timeout=10, polFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=polFrequency, ignored_exceptions=[NoSuchElementException,
                                                                                                ElementNotVisibleException,
                                                                                                ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeard on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        scroll the page up or down
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -600);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 600);")

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

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def SwitchFrameByIndex(self, locator, locator_type="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locator_type="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.is_element_present(locator, locator_type)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.driver.switch_to.default_content()
            return result
        except:
            print("iFrame index not found")
            return result

    def clearField(self, locator="", locatorType="id"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def getElementAttributeValue(self, attribute, element=None, locator="", locator_type="xpath"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locator_type="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.get_element(locator, locator_type=locator_type)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def get_title(self):
        return self.driver.title
