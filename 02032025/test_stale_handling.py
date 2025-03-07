from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
import allure
import pytest
import time


def test_google_18():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    try:
        text_area=driver.find_element(By.NAME,"q")
        driver.refresh()
        text_area.send_keys("the testing academy")

    except StaleElementReferenceException as see:
        print(see)

    time.sleep(5)