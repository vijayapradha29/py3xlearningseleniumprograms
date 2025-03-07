from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with

@pytest.mark.relative1

def test_relative_locator1():
    driver=webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    newdelhi_element=driver.find_element(By.XPATH,"//p[text()='New Delhi']")
    left_element=driver.find_element(locate_with(By.XPATH,"//p[text()='23']").to_left_of(newdelhi_element))
    print(left_element.text)
    right_element=driver.find_element(locate_with(By.XPATH,"//span[text()='184']").to_right_of(newdelhi_element))
    print(right_element.text)
    print(f"The Element to the Left of New Delhi is:{left_element.text} and The Element to the Right of New Delhi is:{right_element.text}")