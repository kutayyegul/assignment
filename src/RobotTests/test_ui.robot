*** Settings ***
Documentation  Test to verify that form submit succeed correctly when a user
...            enter user name and a message into the form and then submit that
...            message. For the second case, User need to validate a captcha
...            operation before submitting message.

Library  Selenium2Library
Resource  Resources/Variables.robot
Resource  Resources/Keywords_UI.robot

Test Setup  Open URL in Chrome Browser
Test Teardown  Close Browser

*** Test Cases ***
User Should Fill The Form 1 Successfully
    Input User Name on Form     ${NAME_FIELD}     TEXT_NAME
    Input Message on Form  ${TEXT_FIELD}   TEST_TEXT
    Click Button  ${SUBMIT_BUTTON}
    Wait Until Page Contains    Form filled out successfully


User Should Fill The Form 2 Successfully
    Input User Name on Form  ${NAME_FIELD2}    TEST_NAME
    Input Message on Form  ${TEXT_FIELD2}   TEST_TEXT
    Pass Captcha
    Click Button  ${SUBMIT_BUTTON2}
    Wait Until Page Contains    Success
