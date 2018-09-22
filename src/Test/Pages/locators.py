from selenium.webdriver.common.by import By


class MainPageLocators(object):
    Name_Field = (By.CSS_SELECTOR, '.et_pb_contact_field_0 #et_pb_contact_name_1.input')
    Text_Field = (By.CSS_SELECTOR, ".et_pb_contact_field_1 .input")
    Submit_Button = (By.CSS_SELECTOR, "#et_pb_contact_form_0 .et_pb_contact_submit.et_pb_button")
    success = (By.CSS_SELECTOR, "#et_pb_contact_form_0 .et-pb-contact-message")