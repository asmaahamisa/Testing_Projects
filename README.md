
///////Web Automation Project Using Selenium and Python//////


This project automates two important user actions on a web application:

test_1SignUP: Verifying user registration
Test_2AddToCart: Verifying product purchase

**It is built using Selenium WebDriver with Python, and simulates how a real user would interact with the website.

*******test_1SignUP – User Registration*********
This test simulates a user signing up on the website.

🔹 Steps Automated:
1-Click on User Profile
2-Click on Register
3-Fill all mandatory fields (like name, email, password, etc.)
4-Submit the registration form
5-Check that the "Logout" button appears on the profile, meaning the user was registered and logged in successfully

🎥 Video Demonstration:
check this path and click view raw
https://github.com/asmaahamisa/Testing_Projects/blob/main/WebVideos/1-SignUp.mp4

///////////////////////////////////////////////////////////////////

*********test_2AddToCart – Purchase Two Products*********
This test simulates a user buying two products.

🔹 Steps Automated:
1-Click on Login in button in Header
2-Add two products to the cart
3-Proceed to checkout
4-Complete the purchase
5-Confirm that the order summary contains both the added two products

🎥 Video Demonstration:
check this path and click view raw
https://github.com/asmaahamisa/Testing_Projects/blob/main/WebVideos/2-AddToCart.mp4

🛠 Tools and Environment

Tool / Software	Purpose
Visual Studio Code	Code editor used to write and run Python automation scripts
Python	Programming language used to build the test cases
Selenium WebDriver	Library used to automate and control the browser
Google Chrome	Browser used for testing the website

▶️ How to Run the Tests
You can run the automation scripts in two ways:

🔹 Option 1: From VS Code (What I Used) 
Open the project folder in Visual Studio Code
Open the test file (e.g., test_Scenario1.py)

Click the green ▶ Run button at the top-right of the editor window

// if use this way make sure you are adding at the end of the test case the manual call function

The test will execute and open the browser automatically

💡 This is the easiest way to run Python scripts if you're using VS Code.

🔹 Option 2: From the Terminal (Alternative)
If you prefer to run from the terminal:

// by using this way you will generate also the test report 

TestCases/test_1SignUp.py --html=Reports/SignUp_report.html --self-contained-html   
TestCases/test_2AddToCart.py --html=Reports/AddToCart_Report.html --self-contained-html


Author
Name: Asmaa Hamisa
Role: Senior Embedded Software Engineer
Country: Egypt
GitHub: https://github.com/asmaahamisa

**********************************************************************
