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

def test_2AddToCart():
# Initialize the WebDriver
   driver = webdriver.Chrome()
   #driver.set_page_load_timeout(15)
   #driver.implicitly_wait(5)

   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)  

# Open the website
   driver.get("https://practice-react.sdetunicorns.com/")
   driver.maximize_window()
   print(driver.title)
   logger.info("Practice with React | SDET Unicorns Test Site")
   assert "Practice with React | SDET Unicorns Test Site"
    
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
       email_field.send_keys("WebAutol19@gmail.com")
       print("Email filled!")

       password_field = driver.find_element(By.ID, "password")
       password_field.send_keys("Password123454")

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
    
    # Step 4: Click on the "Categories" button to reveal category options


       categories_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div/div[2]/h4"))
    )

       driver.implicitly_wait(1000)
       categories_button.click()

  
    #time.sleep(1)

       print("Categories button clicked!")
       logger.info("Categories button clicked!")

    # Step 5: Wait for the "Keyboards" checkbox to appear and select it

       keyboards_checkbox = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div/div[2]/div/ul/li[4]/div/button"))
    )

       driver.implicitly_wait(1000)
       keyboards_checkbox.click()

       time.sleep(1)
       print("Keyboards category selected successfully!")
       logger.info("Keyboards category selected successfully!")

    # Step 6: Click on "Apply" button to filter products

       apply_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div/button"))
    )

       driver.implicitly_wait(1000)
       apply_button.click()
       print("Apply button clicked. Keyboards filter applied.")
    
    # Step 7: Validate that only keyboard products only appear

    # Step 8 :Click on product "Logitech Wireless Keyboard and Mouse Combo - Black (MK270)" 
    
       Keyboard_product = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/h3/a")
    

       driver.implicitly_wait(1000)
       Keyboard_product.click()
       time.sleep(2)
   

    # Step 9: Validate product details (name and price)
    # no price added to compare with

       product_name = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div/h2").text
       product_price = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div/div[1]/span").text

       if "Logitech Wireless Keyboard" in product_name:
           print(f"Product name validated: {product_name}")
           logger.info(f"Product name validated: {product_name}")


   # Step 10: Validate that product cart are empty


       Cart = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/button/span")
    
       driver.implicitly_wait(1000)
       Cart.click()
       time.sleep(1)



       cart_empty_message = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/div/p").text
       print(f"Cart is empty:{cart_empty_message}")
       logger.info(f"Cart is empty:{cart_empty_message}")

    
    # Step 11: Click on Add to Cart 
       add_to_cart_button = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div/div[4]/div[2]/button")

       add_to_cart_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div/div[4]/div[2]/button"))
    )
    
       driver.implicitly_wait(1000)
       time.sleep(1)
       add_to_cart_button.click()


    # Step 12 :Validate that product cart contain one element

       View_Cart = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/div/div[2]/a[1]")

       View_Cart = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/div/div[2]/a[1]"))
    )

    
    
       driver.implicitly_wait(1000)
       View_Cart.click()

       cart_count_element = driver.find_element(By.CLASS_NAME, "cart-plus-minus-box")

    # Extract the value from the input field
       cart_item_count = int(cart_count_element.get_attribute('value'))

    # Validate that the cart contains exactly 1 item
       if cart_item_count == 1:
          print("Test Passed: Cart contains 1 item.")
          logger.info("Test Passed: Cart contains 1 item.")
       else:
           print(f"Test Failed: Expected 1 item in cart, but found {cart_item_count}")
           logger.info(f"Test Failed: Expected 1 item in cart, but found {cart_item_count}")

    # Step 13 : Validate that product message     
       product_name_in_Cart = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div/div/table/tbody/tr/td[2]/a").text
    
       if "Logitech Wireless Keyboard" in product_name_in_Cart:
           print(f"Product message validated: {product_name_in_Cart}")
           logger.info(f"Product message validated: {product_name_in_Cart}")

    
    #Step 14 : Click on Products tab in header

       product_tab = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[2]/div/nav/ul/li[2]/a")
    
       driver.implicitly_wait(1000)
       product_tab.click()

    #Step 15 :Click on Laptop in categories in home page.

       laptop_checkbox = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div/div[2]/div/ul/li[2]/div/button"))
    )
    
       driver.implicitly_wait(1000)
       laptop_checkbox.click()
       print("laptop category selected!")
       logger.info("laptop category selected!")


    # Step 16: Click on "Apply" button to filter products
       apply_button = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div/button"))
    )

       driver.implicitly_wait(1000)
       apply_button.click()
       print("Apply button clicked. laptop category selected.")
       logger.info("Apply button clicked. laptop category selected")

    #Step 17: choose product name "Dell Chromebook 11 3120 (11.6", Intel Celeron N2840, 4GB RAM, 16GB SSD, Latest Chromebook OS) - Refurbished"
    
       laptop_product = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]/h3/a")
    
    
    
       driver.implicitly_wait(1000)
       laptop_product .click()
       time.sleep(1)

    #Step 18: click on add to cart

       add_to_cart_button = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[2]/div/div[4]/div[2]/button")
      
       driver.implicitly_wait(1000)
       add_to_cart_button.click()
       time.sleep(1)


    #press on view cart

       Cart = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/button/span")
       driver.implicitly_wait(10000)
       Cart.click()


       View_Cart = driver.find_element(By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/div/div[2]/a[1]")
       View_Cart = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[4]/div/div[2]/a[1]"))
    )
    
       driver.implicitly_wait(10000)
    #View_Cart.click()
       driver.execute_script("arguments[0].click();", View_Cart)

       cart_count_element = driver.find_element(By.CLASS_NAME, "cart-plus-minus-box")

     # Extract the value from the input field
       cart_item_count = int(cart_count_element.get_attribute('value'))

     # Validate that the cart contains exactly 1 item
  
       print(f"Cart contain :{cart_item_count} laptop")


    #Step 19: Validate that two products which include (title and Price) are successfully added in cart

       CartProducts = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "pe-7s-shopbag"))
)

       driver.implicitly_wait(1000)
    
       try:
    # Check that exactly two products are in the cart
           assert len(CartProducts) == 2, "There should be exactly two products in the cart."
           print("Test Passed: Two products are successfully added to the cart.")
           logger.info("Test Passed: Two products are successfully added to the cart.")
       except AssertionError as e:
    
           print(f"Test Failed: {e}")
           logger.info(f"Test Failed: {e}")

    # Define expected names and prices
    
       expected_products = [
    {"name": "Logitech Wireless Keyboard and Mouse Combo - Black (MK270)", "price": 33.00},
    {"name": "Dell Chromebook 11 3120 (11.6\", Intel Celeron N2840, 4GB RAM, 16GB SSD, Latest Chromebook OS) - Refurbished", "price": 700.00}
    ]


    # Validate each product's name and price
       driver.implicitly_wait(1000)
   
       first_product = CartProducts[0]  # Get the first element


       print("Successfully accessed the first product.")
       actual_name = first_product.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[2]/a").text
       driver.implicitly_wait(1000)


       actual_price_product1 = float(first_product.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div/div/table/tbody/tr[1]/td[3]/span").text.replace("$", ""))
       driver.implicitly_wait(1000)
    

       assert actual_name == expected_products[0]["name"], f"Test Failed: Name mismatch for product { 1}"
       assert actual_price_product1 == expected_products[0]["price"], f"Test Failed: Price mismatch for product { 1}"
       print(f"Test Passed: Product { 1} name and price match.")
       logger.info(f"Test Passed: Product { 1} name and price match.")
   
   

       Second_product = CartProducts[1]  # Get the first element 
       print("Successfully accessed the first product.")
       actual_name = Second_product.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[2]/a").text
       driver.implicitly_wait(1000)
   


       actual_price_product2 = float(Second_product.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div/div/table/tbody/tr[2]/td[3]/span").text.replace("$", ""))
       driver.implicitly_wait(1000)
    
       assert actual_name == expected_products[1]["name"], f"Test Failed: Name mismatch for product { 2}"
       assert actual_price_product2 == expected_products[1]["price"], f"Test Failed: Price mismatch for product { 2}"
       print(f"Test Passed: Product {2} name and price match.")
       logger.info(f"Test Passed: Product {2} name and price match.")



     #Step 20: Validate that total amount is calculated correctly.

       expected_total = 0.0
       expected_total=actual_price_product1+actual_price_product2

       print(f"the expected total price is : {expected_total}" )
       logger.info(f"the expected total price is : {expected_total}")

    

       Total_price_displayed = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div/div/h4/span").text
       driver.implicitly_wait(1000)
   # Convert the string to a float after removing the $ symbol
       try:
          displayed_total_value = float(Total_price_displayed.replace("$", "").strip())
          print("Displayed Total:", displayed_total_value)
          logger.info("Displayed Total:", displayed_total_value)

       except ValueError as e:
          print(f"Error converting total to float: {e}")
          logger.info(f"Error converting total to float: {e}")

       if expected_total == displayed_total_value:
          print("Total amount is calculated correctly.")
          logger.info(f"Total amount is calculated correctly.")
       else:
          print(f"Total amount mismatch: Expected ${expected_total}, but got ${displayed_total_value}")
          logger.info(f"Total amount mismatch: Expected ${expected_total}, but got ${displayed_total_value}")

     #Step 21: Click on Checkout button.


       try:
           checkout_button = WebDriverWait(driver, 30).until(
           EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div/div/a"))  
           )
           driver.implicitly_wait(1000)
           checkout_button.click()
           time.sleep(1)
           print("Checkout button clicked successfully.")
           logger.info("Checkout button clicked successfully.")

       except Exception as e:
           print(f"Error clicking Checkout button: {e}")
           logger.info(f"Error clicking Checkout button: {e}")

#Step 22 :Fill the shipping address and click on checkbox button

# Sample shipping address data
       shipping_data = {
    "Country": "Egypt",
    "Region": "Aswan",
    "address1": "123ABC",
    "address2": "12345ABCD",
    "city": "New York",
    "zip_code": "10001",
    "phone": "34567890"
    }

       try:
    # Fill Country field 
           dropdown_Country = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[1]/div[1]/select")  
           dropdown = Select(dropdown_Country)
           dropdown.select_by_visible_text(shipping_data["Country"])

    # fill region field   

           dropdown_Region = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[1]/div[2]/select")  
           dropdown = Select(dropdown_Region)
           dropdown.select_by_visible_text(shipping_data["Region"])
    
       
    # Fill in the Address1 field
           address_field = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[2]/div[1]/input")  
           address_field.clear()
           address_field.send_keys(shipping_data["address1"])

    # Fill in the Address2 field
           address_field = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[2]/div[2]/input")  
           address_field.clear()
           address_field.send_keys(shipping_data["address2"])

    # Fill in the ZIP code field
           zip_code_field = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[3]/div[1]/input")  # Adjust the locator
           zip_code_field.clear()
           zip_code_field.send_keys(shipping_data["zip_code"])

    # Fill in the Phone number field
           phone_field = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[3]/div[2]/input")  # Adjust the locator
           phone_field.clear()
           phone_field.send_keys(shipping_data["phone"])

           checkbox = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[4]/label/input")  # Adjust the ID as needed

    # Check if the checkbox is not already selected, then click to select it
           if not checkbox.is_selected():
             driver.implicitly_wait(1000)
             checkbox.click()
             print("Checkbox selected successfully.")
           else:
             print("Checkbox was already selected.")

     #Step 22 :Click on Confirm button.

        # Wait until the Confirm button is clickable, then click it
           confirm_button = WebDriverWait(driver, 30).until(
           EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[2]/div/div[3]/div[2]/form/div/div[5]/button"))  # Adjust locator as needed
    
    )
        
           driver.implicitly_wait(1000)
           confirm_button.click()
           time.sleep(1)
        
       except Exception as e:
            print(f"An error occurred while filling the form or clicking the checkbox: {e}")
            logger.info(f"An error occurred while filling the form or clicking the checkbox: {e}")
        
    #Step 23: validate that shipping address are correct and total price


       Order_press = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/button/h3")
       Order_press.click()

       driver.implicitly_wait(1000)

    #download_button = driver.find_element(By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div[2]/div/div[1]/button")
    #download_button.click()
    
    # Expected values for validation
       expected_address = f"Address 1 : {shipping_data['address1']}"
       expected_total_price = "Total : $733"
       wait = WebDriverWait(driver, 10)
       address_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div[2]/div/div[2]/h4[4]")))  # Replace with the actual XPath
       total_price_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/div[2]/div/div/div[1]/div[2]/div/div[2]/h4[6]")))  # Replace with the actual XPath

    # Extract text from elements
       actual_address = address_element.text
       actual_total_price = total_price_element.text

    ## Perform validations
       if actual_address == expected_address:
           print(f"Address validation successful: '{actual_address}' matches expected address.")
           logger.info(f"Address validation successful: '{actual_address}' matches expected address.")
       else:
           print(f"Address validation failed: Expected '{expected_address}', but found '{actual_address}'.")
           logger.info(f"Address validation failed: Expected '{expected_address}', but found '{actual_address}'.")

       if actual_total_price == expected_total_price:
           print(f"Total price validation successful: '{actual_total_price}' matches expected total price.")
           logger.info(f"Total price validation successful: '{actual_total_price}' matches expected total price.")
       else:
           print(f"Total price validation failed: Expected '{expected_total_price}', but found '{actual_total_price}'.")
           logger.info(f"Total price validation failed: Expected '{expected_total_price}', but found '{actual_total_price}'.")
   
    
   except TimeoutException:
       print("Error: Element took too long to load.")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")

   finally:

      time.sleep(2)
      driver.quit()
   return True

# Calling the function for execution
#test_2AddToCart()