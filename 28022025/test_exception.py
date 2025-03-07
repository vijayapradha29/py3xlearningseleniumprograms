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


def test_practice():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    # exception_element=driver.find_element(By.XPATH,"//div[@jsname='RNNXgb']/div[1]/div[2]/textarea[@name='q']")
    try:
        exception_element = driver.find_element(By.NAME, "pramod")
        exception_element.send_keys("the testing academy")
    except NoSuchElementException as nse:
        print(f"No Such Element Found check Locators:{nse}")
    time.sleep(10)