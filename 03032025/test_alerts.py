from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
import pytest
import allure
import time

def test_alert():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    jsalert_element=driver.find_element(By.XPATH,"//button[contains(text(),'JS Alert')]")
    jsalert_element.click()
    wait=WebDriverWait(driver=driver,timeout=5).until(
        EC.alert_is_present()
    )
    alert=Alert(driver)
    alert.accept()
    result=driver.find_element(By.ID,"result").text
    assert result=="You successfully clicked an alert"


def test_confirm_alert():
    options=webdriver.ChromeOptions()
    options.page_load_strategy='normal'
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_confirm_element=driver.find_element(By.XPATH,"//button[contains(text(),'JS Confirm')]")
    js_confirm_element.click()
    wait=WebDriverWait(driver=driver,timeout=5).until(
        EC.alert_is_present()
    )
    alert=Alert(driver)
    alert.accept()
    result=driver.find_element(By.ID,"result").text
    assert result=="You clicked: Ok"

def test_prompt_alerrt():
    options=webdriver.ChromeOptions()
    options.page_load_strategy='normal'
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_prompt_element=driver.find_element(By.XPATH,"//button[contains(text(),'JS Prompt')]")
    js_prompt_element.click()
    wait=WebDriverWait(driver=driver,timeout=5).until(
        EC.alert_is_present()
    )
    alert=Alert(driver)
    alert.send_keys("vijaya")
    alert.accept()
    result=driver.find_element(By.ID,"result").text
    assert result=="You entered: vijaya"

def test_checkbox():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes_element=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    checkboxes_element[0].click()