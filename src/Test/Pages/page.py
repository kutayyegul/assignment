from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)


class MainPage(BasePage):

    def is_opened(self):
        title = self.driver.title
        assert title, "Filling Out Forms - Ultimate QA"

    def fill_name(self):
        element = self.driver.find_element(*MainPageLocators.Name_Field2)
        element.send_keys("USER_NAME USER_SURNAME")

    def fill_text(self):
        element = self.driver.find_element(*MainPageLocators.Text_Field2)
        element.send_keys("FORM FIELD TO TYPE A MESSAGE FOR USERS")

    def submit_button(self):
        element = self.driver.find_element(*MainPageLocators.Submit_Button2)
        element.click()

    def message(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.Success_Message2))
        return element.text

    def passCaptcha(self):
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.Captcha))
        operation = eval(element.text)
        element2 = self.wait.until(EC.element_to_be_clickable(MainPageLocators.Captcha_Field))
        element2.send_keys(operation)