from locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)


class MainPage(BasePage):

    def fill_name(self):
        element = self.driver.find_element(*MainPageLocators.Name_Field)
        element.send_keys("osman")

    def fill_text(self):
        element = self.driver.find_element(*MainPageLocators.Text_Field)
        element.send_keys("osmancan 2222")

    def submit_button(self):
        element = self.driver.find_element(*MainPageLocators.Submit_Button)
        element.click()

    def message(self):
        #element = self.driver.find_element(*MainPageLocators.success)
        element = self.wait.until(EC.element_to_be_clickable(MainPageLocators.success))
        return element.text


if __name__ == "__main__":
    import sys