from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.common.exceptions import *


def test_exception():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    try:
        textarea=driver.find_element(By.NAME,"q")
        driver.refresh()
        textarea=driver.find_element(By.NAME,"q")
        textarea.send_keys("the testing academy")
    except StaleElementReferenceException as see:
        print(see)

    time.sleep(10)
    driver.quit()