from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
import os

def test_actions():
    load_dotenv()
    driver=webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    # time.sleep(5)
    driver.maximize_window()
    # driver.implicitly_wait(10)
    wait=WebDriverWait(driver=driver,timeout=10).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']"))
    )
    wait.click()
    time.sleep(2)
    # driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()
    wait=WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='CustomModal_10']"))
    )
    wait.click()
    time.sleep(2)
    #Now next we need to locate the element (fromcity)
    wait=WebDriverWait(driver=driver,timeout=10).until(
        EC.visibility_of_element_located((By.XPATH,"//input[@id='fromCity']"))
    )
    # #or (BY.XPATH,"//input[@id='fromCity']")
    fromcity_element=driver.find_element(By.ID,"fromCity")
    action=ActionChains(driver)
    # action.move_to_element(fromcity_element).click().send_keys_to_element(fromcity_element,"Goa").perform()
    action.move_to_element(fromcity_element).click().send_keys_to_element(fromcity_element,os.environ.get("CITY")).perform()
    # action.move_to_element(fromcity_element).click().send_keys("New Delhi").perform()
    # action.move_to_element(fromcity_element).click().send_keys_to_element(fromcity_element,"New Delhi").key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    time.sleep(10)
    action.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
    time.sleep(5)

    #Note: right is context-click
    #1.we can also get city(key value)from external source instead of hardcoding values,for that we use .env
    #2.pip install python-dotenv
    #3.click on folder (py3x)->create new file as .env and enter CITY=Mumbai(can use quotes or  no quotes for value of city)
    #4.then use a small function,
    #from dotenv import load_dotenv
    #5.then call load_dotenv() into def test_actions()in first line
    #6.import os
    #7.in send_keys_to_element,enter(os.environ.get("CITY"))