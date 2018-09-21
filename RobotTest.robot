
*** Settings ***
Documentation  Demo Test for Robot Framework
Library  Selenium2Library

*** Variables ***
${LOGIN URL}        https://www.ultimateqa.com/filling-out-forms/
${BROWSER}        Chrome
${NAME_FIELD}    css=.et_pb_contact_field_0 #et_pb_contact_name_1.input
${TEXT_FIELD}   css=.et_pb_contact_field_1 .input
${SUBMIT_BUTTON}    css=#et_pb_contact_form_0 .et_pb_contact_submit.et_pb_button

*** Test Cases ***
User Must Sign in to check out
    [Documentation]  This is demo test case
    [Tags]  Smoke
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait  10 seconds
    set selenium speed   0.5 seconds
    Input Text  ${NAME_FIELD}    TEST_NAME
    Input Text  ${TEXT_FIELD}   TEST_TEXT
    Click Button  ${SUBMIT_BUTTON}
    Wait Until Page Contains    Form filled out successfully
    Close Browser
