import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support.ui import Select
import time

@pytest.mark.select

def test_herokuapp_select():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_element=driver.find_element(By.CSS_SELECTOR,"select[id='dropdown']")
    select=Select(select_element)
    select.select_by_visible_text("Option 2")
    time.sleep(5)
