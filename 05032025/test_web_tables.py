# # Web tables:
# Web Tables are used to organize similar types of content on the web page, Web tables are groups of elements that are logically stored in a row and column format. Web table has various HTML tags like., table, th, tr, td. Let’s understand these tags a bit more:
#
# <table> – It defines a table
# <th> – It defines a header cell
# <tr> – It defines a row in a table.
# <td>- It defines a cell in a table. the <td> tag always lies inside the <tr> tag.
#thead->it can be optional
from itertools import dropwhile

#in table,we have rows and cells not columns(any individual column that we choose is cell)
#horizontal are rows and vertical are cells
#< tbody > — Defines a container for rows and columns


#how to handle?
#eg:https://awesomeqa.com/webtable.html
# 1.Find the table
# //table[@id="customer"]

# Types of web tables

# 1.Static:The fixed data in these tables stays constant throughout. They are referred to as Static Web Tables due to the static nature of their content.

# 2.Dynamic:These tables have data that changes over time, and hence the number of rows and columns might also change depending upon the data shifts. Due to the dynamic nature of their content, they are called Dynamic web tables.


# problem statement:how to get all the elements from the table:


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



def test_web_table():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    #first of all find how many rows and columns the table has
    #total no of rows://table[@id='customers']/tbody/tr
    #select any row.for ex:i have selected 2nd row so,
    #total no.of columns://table[@id='customers']/tbody/tr[2]/td
    #this is the static table

    row_elements=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    rows=len(row_elements)
    print(rows)
    column_element=driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    columns=len(column_element)
    print(columns)
    time.sleep(5)

    #to get all the values
    #to get the particular element out from the table only the numbers in tr and numbers in td changes rest remains same
    #//table[@id='customers']/tbody/tr[
    # 2->changes from 2 to 7,because 1 is header
    # ]/td[
    # 1->changes from 1 to 3
    # ]

    first_part="//table[@id='customers']/tbody/tr["
    second_part="]/td["
    third_part="]"
    for i in range(2,rows+1):#rows->take values from given and stops at the specified end value so we ae giving end value as row+1,#here if suppose we 2 to rows(rows prints 7 as value) so it will take only from 2 to 6 so we gave 2 to row+1
        for j in range(1,columns+1):
            dynamic_elements=f"{first_part}{i}{second_part}{j}{third_part}"
            data=driver.find_element(By.XPATH,dynamic_elements).text
            # print(data.text)
            if "Helen Bennett" in data:
                path=f"{dynamic_elements}/following-sibling::td"
                path_text=driver.find_element(By.XPATH,path)
                print(path_text.text)
    driver.quit()

    #3.Find Helen Bennett Country:
    #in web tables use xpath axes
    