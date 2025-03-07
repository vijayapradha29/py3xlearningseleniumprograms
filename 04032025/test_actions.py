from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType

def test_actions():
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    # time.sleep(5)
    driver.maximize_window()
    wait=WebDriverWait(driver=driver,timeout=10).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']"))
    )
    wait.click()
    # driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
    time.sleep(2)
    #Now next we need to locate the element (fromcity)

    fromcity_element=driver.find_element(By.XPATH,"//input[@id='fromCity']")
    #or (BY.XPATH,"//input[@id='fromCity']")
    action=ActionChains(driver)
    action.move_to_element(fromcity_element).click().send_keys_to_element(fromcity_element,"Mumbai").perform()
    # action.move_to_element(fromcity_element).click().send_keys("New Delhi").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    time.sleep(10)