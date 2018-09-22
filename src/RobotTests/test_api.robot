*** Settings ***
Documentation  Test For API
Library  RequestsLibrary
Library  Collections
Resource  Resources/Variables.robot
Resource  Resources/Keywords_API.robot

*** Test Cases ***
API TEST DEMO
    [Documentation]  adadads
    Create Session      API     ${url}
    ${resp}=	get request  API    /users
    Should Be Equal As Strings	${resp.status_code}	200
    Response Time Should Be Less Than 200ms  ${resp.elapsed.total_seconds()}
    ${JSON}=    Set Variable    ${resp.json()}
    Iteration Should Print Group Companies      ${JSON}