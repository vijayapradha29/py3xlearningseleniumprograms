from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with

@pytest.mark.relativelocators

def test_relative_locators():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    yoe_element=driver.find_element(By.XPATH,"//span[text()='Years of Experience']")
    radion_button3=driver.find_element(locate_with(By.ID,"exp-2").to_right_of(yoe_element))
    radion_button3.click()
    time.sleep(5)