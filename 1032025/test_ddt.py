import openpyxl
from openpyxl.utils import rows_from_range
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
import allure
import pytest
import time
import os
from allure_commons.types import AttachmentType


def user_credentials_from_excel(file_path):
    credentials=[]
    workbook=openpyxl.load_workbook(file_path)
    sheet=workbook.active
    for row in sheet.iter_rows(min_row=2,values_only=True):
        username,password=row
        credentials.append({
            "username":username,
            "password":password
        })
    return credentials



file_path=os.getcwd()+"/testdata.xlsx"

@pytest.mark.parametrize("user_cred",user_credentials_from_excel(file_path))
def test_vwo_login(user_cred):
    username=user_cred["username"]
    password=user_cred["password"]
    vwo_login(username=username,password=password)
    # print(username,password)
def vwo_login(username,password):
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    username_input=driver.find_element(By.XPATH,"//input[@id='login-username']")
    username_input.send_keys(username)

    password_input=driver.find_element(By.CSS_SELECTOR,"[name='password']")
    password_input.send_keys(password)

    sign_in_button=driver.find_element(By.ID,"js-login-btn")
    sign_in_button.click()

    time.sleep(10)

    # assert driver.current_url=="https://app.vwo.com/#/dashboard"
    # time.sleep(5)
    result=driver.current_url
    print(result)


    if result!="https://app.vwo.com/#/dashboard":
        # ignore_list=(ElementNotVisibleException,ElementNotSelectableException)
        # wait=WebDriverWait(driver=driver,timeout=10,poll_frequency=1,ignored_exceptions=ignore_list)
        # wait.until(
        #     EC.visibility_of_element_located((By.ID,"js-notification-box-msg"))
        # )
        error_msg_element=driver.find_element(By.ID,"js-notification-box-msg")
        assert driver.current_url=="https://app.vwo.com/#/login"

    else:
        # ignore_list=(ElementNotVisibleException,ElementNotVisibleException)
        # wait=WebDriverWait(driver=driver,timeout=10,poll_frequency=1,ignored_exceptions=ignore_list)
        # wait.until(
        #     EC.visibility_of_element_located((By.XPATH,"//span[@data-qa='lufexuloga']"))
        # )
        dashboard_element=driver.find_element(By.XPATH,"//span[@data-qa='lufexuloga']")
        assert driver.current_url=="https://app.vwo.com/#/dashboard"

    time.sleep(10)