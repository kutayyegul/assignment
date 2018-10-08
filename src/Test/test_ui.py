import unittest
from selenium import webdriver
from Pages.page import MainPage
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestUI(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=options.to_capabilities())

        self.driver.get("https://www.ultimateqa.com/filling-out-forms/")

    def test_should_fill_form_with_captcha(self):

        main_page = MainPage(self.driver)
        main_page.is_opened()
        main_page.fill_name()
        main_page.fill_text()
        main_page.passCaptcha()
        main_page.submit_button()
        assert main_page.message(), "Success"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
