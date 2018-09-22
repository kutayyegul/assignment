*** Keywords ***
Iteration Should Print Group Companies      [Arguments]    ${JSON}
    :FOR    ${ELEMENT}    IN    @{JSON}
        \    ${COMPANY}=    Set Variable     ${ELEMENT["company"]["name"]}
        \    Run Keyword If     "Group" in $COMPANY   log  ${COMPANY}


Response Time Should Be Less Than 200ms  [Arguments]  ${TIME}
    Should Be True  ${TIME} <=0.200