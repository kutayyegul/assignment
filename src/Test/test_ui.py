import unittest
from selenium import webdriver
from Pages.page import MainPage
import platform
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time



class TestUI(unittest.TestCase):

    def setUp(self):
        operating_system = platform.system()
        if operating_system == "Darwin":
            path = "./Drivers/chromedriver"
        elif operating_system == "Windows":
            path = "./Drivers/chromedriver.exe"
        else:
            path = "./Drivers/chromedriverLinux"

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")


        ##self.driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
        time.sleep(5)
        self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME, command_executor='http://167.99.209.91:4444/wd/hub')
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
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
