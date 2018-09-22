*** Settings ***
Documentation  Demo Test for Robot Framework
Library  Selenium2Library
Resource  Resources/Variables.robot
Resource  Resources/Keywords_UI.robot

*** Test Cases ***
User Must Fill The Form 1 Successfully
    [Documentation]  This is demo test case

    Open URL in Browser     ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed   0.1 seconds
    Input User Name on Form     ${NAME_FIELD}     TEXT_NAME
    Input Message on Form  ${TEXT_FIELD}   TEST_TEXT
    Click Button  ${SUBMIT_BUTTON}
    Wait Until Page Contains    Form filled out successfully
    Close Browser

User Must Fill The Form 2 Successfully
    [Documentation]  This is demo test case

       Open Browser    ${LOGIN URL}    ${BROWSER}
       Maximize Browser Window
       Set Selenium Speed   0.1 seconds
       Input User Name on Form  ${NAME_FIELD2}    TEST_NAME
       Input Message on Form  ${TEXT_FIELD2}   TEST_TEXT
       PASS CAPTCHA
       Click Button  ${SUBMIT_BUTTON2}
       Wait Until Page Contains    Success
       Close Browser