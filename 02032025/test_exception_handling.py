from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.common.keys import Keys
from allure_commons.types import AttachmentType
import allure
import pytest
import time

def test_vwo_login_16():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    try:
        element=driver.find_element(By.ID,"this_id_doesn't_exist")
    except NoSuchElementException:
        print("Element Not Found")

    print("End of the Program")


    time.sleep(5)