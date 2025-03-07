# <input class="Pke_EE"
# type="text"
# title="Search for Products, Brands and More"
# name="q"
# autocomplete="off"
# placeholder="Search for Products, Brands and More"
# value=""
# fdprocessedid="qvsma">


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
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    search_bar_element=driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
    search_bar_element.send_keys("AC")

    # search_button_element=driver.find_element(By.XPATH,"//*[local-name()='svg']/*[local-name()='path' and @stroke='#717478']")
    # search_button_element.click()
    search_button_lists=driver.find_elements(By.XPATH,"//*[local-name()='svg']")
    search_button_lists[0].click()

