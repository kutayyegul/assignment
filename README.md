# Python Automation and Robot Framework

This project consist of 2 seperate automation types. One of them, python binding selenium,
other one is Robot Framework. Both automation suites tests UI and API cases.

Selenium Bindings test suites are under Test Folder. Robot Framework
Suites are under RobotTests Folder.

###### Requirements 

There are few modules need to be installed before running the tests.
You can install this modules via below commands.

* `pip install selenium`
* `pip install requests`
* `pip install robotframework`
* `pip install robotframework-requests`
* `pip install robotframework-selenium2library`


###### Project 

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


###### Suites

**UI TEST**

For the UI suites, Both form is tested in Robot Framework. For Selenium Python side, I choose to
remove the case for standard form and the form with captcha case is remained. 

In both framework, there is a title verification after the URL loaded. Then name fields and 
message fields are filled. For the captcha case, Captcha operation is calculated by `eval`
function then result is filled the captcha area. After that, form is submitted and checking 
for success message on the page.

`Test URL : https://www.ultimateqa.com/filling-out-forms/`

**API TEST**

For the API suites, All cases are tested in both framework and also Postman Test.
This tests are check for response code and expect a response duration less than 200ms.
Then, checking for company names which are contains Group in the response body json.

`https://jsonplaceholder.typicode.com/users`

![Postman Test Results](https://github.com/kutayyegul/assignment/blob/master/postman.png)

This Postman tests can be found at `PostmanTest.js` file under src folder.

###### Running Tests

To be able to run the tests. Requirements need to be installed correctly.

For python selenium suites. There are two option to run the test. 

1. Running via terminal command line.
    * Open terminal and navigate the folder that contain test_ui.py and test_api.py files.
    * Type `python -m unittest test_ui.py` or `python -m unittest test_api.py`
    or `python -m unittest discover`
2. Running `load.py` file 

For Robot suites

1. Open terminal and navigate the folder that contain test_ui.robot and test_api.robot files.
2. Type `pybot test_ui.robot` or `pybot test_api.robot`

