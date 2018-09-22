from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)


class MainPage(BasePage):

    def fill_name(self, formNumber):
        if formNumber == 1:
            locator = MainPageLocators.Name_Field
        elif formNumber == 2:
            locator = MainPageLocators.Name_Field2
        element = self.driver.find_element(*locator)
        element.send_keys("USER_NAME USER_SURNAME")

    def fill_text(self, formNumber):
        if formNumber == 1:
            locator = MainPageLocators.Text_Field
        elif formNumber == 2:
            locator = MainPageLocators.Text_Field2
        element = self.driver.find_element(*locator)
        element.send_keys("FORM FIELD TO TYPE A MESSAGE FOR USERS")

    def submit_button(self, formNumber):
        if formNumber == 1:
            locator = MainPageLocators.Submit_Button
        elif formNumber == 2:
            locator = MainPageLocators.Submit_Button2
        element = self.driver.find_element(*locator)
        element.click()

    def message(self, formNumber):
        if formNumber == 1:
            locator = MainPageLocators.Success_Message
        elif formNumber == 2:
            locator = MainPageLocators.Success_Message2
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element.text

    def passCaptcha(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.Captcha))
        operation = eval(element.text)
        element2 = self.wait.until(EC.element_to_be_clickable(MainPageLocators.Captcha_Field))
        element2.send_keys(operation)