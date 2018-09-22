from selenium.webdriver.common.by import By


class MainPageLocators(object):

    # FORM 1 SELECTORS
    Name_Field = (By.CSS_SELECTOR, '.et_pb_contact_field_0 #et_pb_contact_name_1.input')
    Text_Field = (By.CSS_SELECTOR, ".et_pb_contact_field_1 .input")
    Submit_Button = (By.CSS_SELECTOR, "#et_pb_contact_form_0 .et_pb_contact_submit.et_pb_button")
    Success_Message = (By.CSS_SELECTOR, "#et_pb_contact_form_0 .et-pb-contact-message")

    # FORM 2 SELECTORS
    Captcha = (By.CSS_SELECTOR, ".et_pb_contact_captcha_question")
    Captcha_Field = (By.CSS_SELECTOR, ".input.et_pb_contact_captcha")
    Name_Field2 = (By.CSS_SELECTOR, ".et_pb_contact_field_2 #et_pb_contact_name_1")
    Text_Field2= (By.CSS_SELECTOR, ".et_pb_contact_field_3 .et_pb_contact_message.input")
    Submit_Button2= (By.CSS_SELECTOR, "#et_pb_contact_form_1 .et_pb_contact_submit.et_pb_button")
    Success_Message2 = (By.CSS_SELECTOR, "#et_pb_contact_form_1 .et-pb-contact-message")