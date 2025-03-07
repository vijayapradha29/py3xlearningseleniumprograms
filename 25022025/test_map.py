from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import pytest
import allure
from allure_commons.types import AttachmentType
import time

@pytest.mark.svgelements

def test_svg_elements():
    driver=webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(10)
    states=driver.find_element(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[local-name()='g']/*[name()='g']/*[local-name()='path' and @aria-label='Tripura  ']")
    states.click()

    #or

    # states_lists=driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[local-name()='g']/*[name()='g']/*[local-name()='path']")
    # for states in states_lists:
    #     if "Tripura" in states.get_attribute("aria-label"):
    #         states.click()
    #         break

    #or
    # states=driver.find_element(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[local-name()='g']/*[name()='g']/*[local-name()='path' and normalize-space(@aria-label='Tripura')]")
    # states.click()
    time.sleep(20)