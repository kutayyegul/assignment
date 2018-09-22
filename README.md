# Python Automation and Robot Framework

###### Requirements 

There are few modules need to be installed before running the tests.
You can install this modules via below commands.

* `pip install selenium`
* `pip install requests`
* `pip install robotframework`
* `pip install robotframework-requests`
* `pip install robotframework-selenium2library`

This project consist of 2 seperate automation types. One of them, python binding selenium,
other one is Robot Framework. Both automation suites tests UI and API cases.

Selenium Bindings test suites are under Test Folder. Robot Framework
Suites are under RobotTests Folder.

Each Framework is testing some simple cases on UI. These are ;

1. Navigating to site URL
2. Filling in one of the two forms
3. Clicking the submit button
4. Checking for the successful message

This test suites are **`test_ui.py`** and **`test_ui.robot`**

And also there are some simple cases on API;

1. Do a GET request to the /users endpoint
2. Validate the response code to be 200
3. Validate the response time to be less than 200ms
4. Iterate over all elements of the json response body
and print out all company names ending with “ Group”

This test suites are **`test_api.py`** and **`test_api.robot`**