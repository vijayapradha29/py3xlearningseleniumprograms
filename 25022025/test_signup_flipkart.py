from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

@pytest.mark.search

def test_search_flipkart():
    driver=webdriver.Chrome()
    driver.get("https://www.flipkart.com/mobiles-accessories/signup~brand/pr?sid=tyy")
    driver.maximize_window()
    # ignore_list=[ElementNotVisibleException,ElementNotSelectableException]
    # WebDriverWait(driver=driver,poll_frequency=1,timeout=10,ignored_exceptions=ignore_list).until(
    #     EC.visibility_of_element_located((By.XPATH,"//a[starts-with(text(),'New')]"))
    # )
    # print(driver.current_url)
    login_element=driver.find_element(By.XPATH,"//a[text()='Login']")
    login_element.click()
    sign_element=driver.find_element(By.XPATH,"//a[contains(text(),'New')]")
    print(driver.current_url)
