from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import allure
import pytest
import time
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
import os
from selenium.common.exceptions import *


def test_spicejet():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    driver.maximize_window()

    time.sleep(5)

    # try:
    ignore_list = (ElementNotVisibleException, ElementNotSelectableException)
    wait = WebDriverWait(driver=driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located(
                (By.XPATH, "//*/div[@data-testid='search-source-code']"))
        )
    from_city = driver.find_element(By.XPATH,
                                        "//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2] [@data-testid='search-source-code']")
    action = ActionChains(driver)
    action.move_to_element(from_city).click().perform()

    # except Exception:
    #     print("Exception")

time.sleep(5)
