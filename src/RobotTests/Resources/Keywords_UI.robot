*** Settings ***
Documentation    Suite description
Library  Selenium2Library
Resource  Variables.robot

*** Keywords ***
Open URL in Chrome Browser
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed   0.1 seconds
    Title Should Be     Filling Out Forms - Ultimate QA

Input User Name on Form
    [Arguments]    ${NAME_FIELD}    ${NAME}
    Input Text  ${NAME_FIELD}   ${NAME}

Input Message on Form
    [Arguments]    ${TEXT_FIELD}    ${TEXT}
    Input Text  ${TEXT_FIELD}   ${TEXT}


Pass Captcha
    ${TEXT}=  Get Text    ${CAPTCHA}
    ${Result}=  Evaluate  ${TEXT}
    Input Text   ${CAPTCHA_FIELD}    ${Result}