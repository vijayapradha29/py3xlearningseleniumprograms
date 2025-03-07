from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, TimeoutException

import time



def test_spicejet():


    driver = webdriver.Chrome()

    driver.get("https://www.spicejet.com/")

    driver.maximize_window()



    time.sleep(5)



    ignore_list = (ElementNotVisibleException, ElementNotSelectableException)



    try:

        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-testid='search-source-code']")))



        from_city = driver.find_element(By.XPATH, "//*[@data-testid='search-source-code']")



        action = ActionChains(driver)

        action.move_to_element(from_city).click().perform()



        print("Clicked on the 'From' city input field successfully.")

    except TimeoutException:

        print("Timed out waiting for the element to be visible.")

    except Exception as e:

        print(f"An error occurred: {str(e)}")

    finally:

        time.sleep(5)

        driver.quit()



# Run the test

# test_spicejet()

