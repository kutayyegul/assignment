import unittest
from selenium import webdriver
from Pages.page import MainPage
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class TestUI(unittest.TestCase):

    def setUp(self):
        operating_system = platform.system()
        if operating_system == "Darwin":
            path = "./Drivers/chromedriver"
        elif operating_system == "Windows":
            path = "./Drivers/chromedriver.exe"
        else:
            path = "./Drivers/chromedriverLinux"

        self.driver = webdriver.Chrome(executable_path=path)
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
