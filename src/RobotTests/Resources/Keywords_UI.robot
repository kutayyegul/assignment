*** Settings ***
Documentation    Suite description
Library  Selenium2Library
Resource  Variables.robot

*** Keywords ***
Open URL in Browser
    [Arguments]    ${BROWSER}
    Open Browser    ${LOGIN URL}    ${BROWSER}

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