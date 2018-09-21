*** Settings ***
Documentation  Test For API
Library  RequestsLibrary
Library  Collections

*** Variables ***
${URL}  https://jsonplaceholder.typicode.com

*** Test Cases ***
API TEST DEMO
    [Documentation]  adadads
    Create Session      API     ${url}
    ${resp}=	get request  API    /users
    Should Be Equal As Strings	${resp.status_code}	200
    Should Be True  ${resp.elapsed.total_seconds()} <=200
    ${JSON}=    Set Variable    ${resp.json()}
    :FOR    ${ELEMENT}    IN    @{JSON}
    \    ${COMPANY}=    Set Variable     ${ELEMENT["company"]["name"]}
    \    Run Keyword If     "Group" in $COMPANY   log  ${COMPANY}
