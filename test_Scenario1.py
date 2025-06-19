from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import pytest
import logging


# Initialize the WebDriver
def test_Scenario1():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)  
    
# Initialize the WebDriver

    driver = webdriver.Chrome()


# Open the website
    driver.get("https://practice-react.sdetunicorns.com/")
    driver.maximize_window()
    print(driver.title)
    logger.info("Practice with React | SDET Unicorns Test Site")
    assert "Practice with React | SDET Unicorns Test Site"
    
  
  
    try:

    # 1. Wait for the User Profile button to appear and be clickable
    # 1. Click on User Profile button

    

        user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )

    # adding additional time 
        driver.implicitly_wait(10)
        user_profile_button.click()
    

        print("User Profile button found and clicked!")
        logger.info("User Profile button found and clicked!")
        assert True
        time.sleep(1)
    # 2. Click on 'Register' button

        register_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[2]/a"))   
    )

        driver.implicitly_wait(10)
        time.sleep(1)
        register_button.click()
        print("Register button clicked!")
        logger.info("Register button clicked!")
        assert True
   

   # 3. Fill all mandatory field

        username_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
        username_field.send_keys("Asmaa_Hamisa_00002")
        print("Username filled!")
        logger.info("Username filled!")
        assert True

    
        email_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
        email_field.send_keys("asmaahamisl0002@gmail.com")
        print("Email filled")
        logger.info("Email filled")
        assert True

        password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
        password_field.send_keys("Password123454")
        print("Password filled!")
        logger.info("Password filled!")
        assert True

    # Wait for the dropdown to be present
        gender_dropdown = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "gender"))
    )
  # Create a Select object
        select = Select(gender_dropdown)

  # Select an option by visible text
        select.select_by_visible_text("Female")

        print("Gender selected!")
        logger.info("Gender selected!")
        assert True
       
    # Submit the registration form


        submit_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/form/button")
        driver.implicitly_wait(10)
        submit_button.click()

        print("Registration form submitted!")
        logger.info("Registration form submitted!")
        assert True

    # 4. Validate that user profile contains button logout

        user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )   

        driver.implicitly_wait(10)
        user_profile_button.click()

        print("User Profile button found and clicked again")
        logger.info("User Profile button found and clicked again")
        assert True

        logout_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[2]"))
    )
        Validation = "Validated"
        if logout_button:
            Validation = "Logout button is present. Validation successful!"
            print(Validation)
            logger.info("Logout button is present. Validation successful!")
            assert True
        else:
            Validation = "Logout button not found. Validation failed."
            print(Validation)
            logger.info("Logout button not found. Validation failed.")
            assert True
    

  
    except TimeoutException:
        print("Error: Element took too long to load.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
   


    finally:

      time.sleep(2)
      driver.quit()
    return Validation
# Calling the function for execution
test_Scenario1()