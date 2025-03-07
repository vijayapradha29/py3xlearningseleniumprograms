#how to handle windows:
#windows means tabs
#https://the-internet.herokuapp.com/windows
#when you click on "Click Here" button->it opens another tab or windows
#now we have to windows or tabs

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

def test_windows():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    #to get parent window use,driver.current_window_handle

    parent_window=driver.current_window_handle
    print(parent_window)
    click_element=driver.find_element(By.XPATH,"//a[text()='Click Here']")
    #or(BY.LINK_TEXT,'Click Here')
    click_element.click()

    window_handles=driver.window_handles
    print(window_handles)

    #we will get 2 windows with unique 16 digit number
    #we can switch to second window also

    # for handle in window_handles:
    #     driver.switch_to.window(handle)
    #     if "New Window" in driver.page_source:#here we are verifying the text that displayed in the child window as "New Window"
    #         print("Test case :Passed!!")
    #         break
    #or you also switch window by
    driver.switch_to.window(window_handles[1])

    time.sleep(5)