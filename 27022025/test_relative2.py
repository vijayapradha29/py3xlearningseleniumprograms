from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with


@pytest.mark.relative1
def test_relative_locator1():
    driver = webdriver.Chrome()
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")
    driver.maximize_window()
    search_element=driver.find_element(By.XPATH,"//input[@type='search']")
    search_element.send_keys("india")
    svg_element_list=driver.find_elements(By.XPATH,"//*[local-name()='svg']")
    svg_element_list[0].click()
    time.sleep(10)
    bhiwandi_element=driver.find_element(By.XPATH,"//p[text()='New Delhi']")
    print(bhiwandi_element.text)
    left_element=driver.find_element(locate_with(By.XPATH,"//p[text()='1']").to_left_of(bhiwandi_element))
    print(left_element.text)
    right_element=driver.find_element(locate_with(By.XPATH,"//span[text()='194']").to_right_of(bhiwandi_element))
    print(right_element.text)
    print(f"The Element to the Left of {bhiwandi_element.text} is:{left_element.text} and The Element to the Right of {bhiwandi_element.text} is:{right_element.text}")
    time.sleep(10)