import unittest
from selenium import webdriver
from Pages.page import MainPage


class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ultimateqa.com/filling-out-forms/")

    def test_should_fill_form(self):

        main_page = MainPage(self.driver)
        main_page.fill_name()
        main_page.fill_text()
        main_page.submit_button()
        assert main_page.message(), "Form filled out successfully"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()