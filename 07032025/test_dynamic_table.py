#dynamic table:https://awesomeqa.com/webtable1.html
#here we have rows->6,columns->7
#here row and column values are not equal.
#then how to handle this?

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import allure
import pytest
import time
from allure_commons.types import AttachmentType

def test_dynamic_table():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()
    #get the table
    table_element=driver.find_element(By.XPATH,"//table[@summary='Sample Table']")
    #here if we know table,we can find tr by find element chaining
    #but be sure that the element tr is present within the table,else it will give u error.
    rows_element=table_element.find_elements(By.TAG_NAME,"tr")
    #or //table[@summary='Sample Table']/tbody/tr
    for rows in rows_element:
        # columns=rows.find_elements(By.TAG_NAME,"td")
        # for elements in columns:
        #     # print(elements.text)
        #and
            header=rows.find_elements(By.TAG_NAME,"th")
            for structure in header:
                print(structure.text)
            #and if "UAE" in elements.text:
                #print("YES")