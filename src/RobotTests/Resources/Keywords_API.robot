*** Settings ***
Library  RequestsLibrary
Library  Collections
Resource     Variables.robot


*** Keywords ***
Create a Session for API
    Create Session      API     ${URL}
    ${resp}=	get request  API    /users
    Set Global Variable    ${resp}

Response Should Return 200 Code
    Should Be Equal As Strings	${resp.status_code}	200


Response Time Should Be Less Than 200ms
    Should Be True  ${resp.elapsed.total_seconds()} <=0.200

Iteration Should Print Group Companies
    ${JSON}=    Set Variable    ${resp.json()}
    :FOR    ${ELEMENT}    IN    @{JSON}
        \    ${COMPANY}=    Set Variable     ${ELEMENT["company"]["name"]}
        \    Run Keyword If     "Group" in $COMPANY   log  ${COMPANY}