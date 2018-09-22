import unittest
from selenium import webdriver
from Pages.page import MainPage


class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.ultimateqa.com/filling-out-forms/")

    def test_should_fill_form(self):

        main_page = MainPage(self.driver)
        main_page.fill_name(1)
        main_page.fill_text(1)
        main_page.submit_button(1)
        assert main_page.message(1), "Form filled out successfully"

    def test_should_fill_form_2(self):

        main_page = MainPage(self.driver)
        main_page.fill_name(2)
        main_page.fill_text(2)
        main_page.passCaptcha()
        main_page.submit_button(2)
        assert main_page.message(2), "Success"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()