from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
import allure
import pytest
import time


def test_google_20():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    try:
        wait=WebDriverWait(driver=driver,timeout=10).until(
            EC.element_to_be_clickable((By.ID,"submit"))
        )
    except TimeoutException as timeout:
        print(f"The Exception Occured is",{timeout})
        print("Timeout Exception Occured!!,10 seconds passed")