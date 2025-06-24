from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import WebDriverException
from decimal import Decimal
import os
import pytest




import logging
import re
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  

def test_3Bonus():
# Initialize the WebDriver
   driver = webdriver.Chrome()
   driver.set_page_load_timeout(15)
   driver.implicitly_wait(5)

   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)  


# Open the website
   driver.get("https://practice-react.sdetunicorns.com/")
   driver.maximize_window()
   print(driver.title)
   logger.info("Practice with React | SDET Unicorns Test Site")
   cart_item_texts = []
   
   try:
# Step 1: Click on "Login" button in the header
       user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )

    # adding additional time 
       driver.implicitly_wait(300)
       user_profile_button.click()


       login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[1]/a"))
    )

       login_button.click()
       print("Login in button in Header is clicked")
       logger.info("Login in button in Header is clicked")
    
    # Step 2: Fill in the email and password in the login form
       email_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
       email_field.send_keys("asmaahamisa6@gmail.com")
       print("Email filled!")

       password_field = driver.find_element(By.ID, "password")
       password_field.send_keys("Password12345")

       print("Email and password are filled")
       logger.info("Email and password are filled")
    

    # Submit the login form
       login_submit_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/form/button")
       login_submit_button.click()

  
       time.sleep(1)

    # Step 3: Validate that the account is open (check for "Logout" button)
    #Click first on user profile button
    
       user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )

    # adding additional time 
       driver.implicitly_wait(300)
       user_profile_button.click()
    
       print("User Profile button found and clicked!")

       logout_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[2]"))
    )
       if logout_button:

           print("Login successful!")
           logger.info("loggin passed successfully")

    #####################################################################      
    
   # Step 1: Click on the cart icon/button to open the cart
       cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[3]/a/i"))  
    )
       cart_button.click()
       print("Cart button clicked to open the cart.")
       logger.info("Cart button clicked to open the cart.")


        # Use a generalized XPath pattern to locate multiple items within the cart
       cart_items = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='root']/div[2]/div/div/div/div[1]/button/h3"))
    )

    # Loop through all items and print their text (or perform any action)
       for index, item in enumerate(cart_items, start=1):
          item_text = item.text
          cart_item_texts.append(item_text)
          print(f"Item {index}: {item.text}")
          logger.info(f"Item {index}: {item.text}")


   except TimeoutException:
       print("Error: Element took too long to load.")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")

   finally:

      time.sleep(2)
      driver.quit()
      return cart_item_texts

# Call the function and store the returned list
cart_items_list = test_3Bonus()
cart_items_list_formatted = [re.search(r"ORDER:\s(\w+)", item).group(1) for item in cart_items_list]

#print("List of cart items:", cart_items_list)

#print (cart_items_list_formatted)
#logger.info(f"List of cart items: {cart_items_list}")


base_url = "https://practice-react.sdetunicorns.com/api/test/"
endpoint = "order"
url = base_url + endpoint
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzE5Y2YxODk4NjE4OGQ0ZGNlNTAyMzAiLCJpYXQiOjE3MzAxNDY0NjN9.ArNzzXDtaajGujlJKHSJkCUu7VHkI-aiDJsW579tnbM"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
API_Get_Orders_Req = requests.get(url, headers=headers)
API_Get_Orders_Res = API_Get_Orders_Req.json()
print("\n")
#print(API_Get_Orders_Res)
print("\n")
ORDER_ID = [list(item.values())[0] for item in API_Get_Orders_Res if item]  # Check if item is not empty


#print(ORDER_ID)


cart_items_list_formatted = [i.lower() for a,i in enumerate(cart_items_list_formatted)]
ORDER_ID = [i.lower() for a,i in enumerate(ORDER_ID)]
comparison_results = [item1 == item2 for item1, item2 in zip(cart_items_list_formatted, ORDER_ID)]

Mismatch = 0
for i, (item1, item2, is_match) in enumerate(zip(cart_items_list_formatted, ORDER_ID, comparison_results), start=1):
    if is_match:
        #print(f"Element {i}: '{item1}' == '{item2}' (Match)")
        pass
    else:
        print(f"Element {i}: '{item1}' != '{item2}' (Mismatch)")
        Mismatch = 1

if Mismatch ==1:
    print(" API order does not return as expected order ID in UI ")
    logger.info(" API order return as expected order ID in UI : Validation Successfully done")

else:
    print(" API order return as expected order ID in UI : Validation Successfully done")
    logger.info(" API order return as expected order ID in UI : Validation Successfully done")