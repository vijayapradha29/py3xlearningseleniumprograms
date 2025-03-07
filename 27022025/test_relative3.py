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
    list_of_states=driver.find_elements(By.XPATH,"//main/div[@data-page='aqi-live-cities-ranking']/div[2]/div[1]/div[2]/div[2]/a/div/p")
    print("\nRank"+"|"+"City"+"|"+"AQI")
    for state in list_of_states:
    #     if state.text.__contains__("China"):
    #         s1=driver.find_element(locate_with(By.TAG_NAME,"p").to_left_of(state)).text
    # # # #     print(s1
    #         s2=driver.find_element(locate_with(By.TAG_NAME,"span").to_right_of(state)).text
    # #     # print(state.text+ "|" + s1+ "|" + s2)
    #         print(s1+ "|"+state.text + "|" + s2)
        if state.text.__contains__("Tianjin, China"):
            s3=driver.find_element(locate_with(By.XPATH,"//main/div[@data-page='aqi-live-cities-ranking']/div[2]/div[1]/div[2]/div[2]/a/div/p").above(state)).text
            # print(s3)\
            s11=driver.find_element(locate_with(By.TAG_NAME,"span"))
            s12=driver.find_element(locate_with(By.TAG_NAME,"p"))
            s13=locate_with(By.TAG_NAME,"p").to_left_of({By.XPATH:"//main/div[@data-page='aqi-live-cities-ranking']/div[2]/div[1]/div[2]/div[2]/a/div/p"}).text
            # print(s13)
            time.sleep(10)
            # s4=driver.find_element(locate_with(By.XPATH,"//main/div[@data-page='aqi-live-cities-ranking']/div[2]/div[1]/div[2]/div[2]/a/div/p").below(state)).text
            # print(s3+"|"+state.text+"|"+s4)
            # print(s3+"|"+s13)
    # bhiwandi_element=driver.find_element(By.XPATH,"//p[text()='New Delhi']")
    # print(bhiwandi_element.text)
    # left_element=driver.find_element(locate_with(By.XPATH,"//p[text()='1']").to_left_of(bhiwandi_element))
    # print(left_element.text)
    # right_element=driver.find_element(locate_with(By.XPATH,"//span[text()='194']").to_right_of(bhiwandi_element))
    # print(right_element.text)
    # print(f"The Element to the Left of {bhiwandi_element.text} is:{left_element.text} and The Element to the Right of {bhiwandi_element.text} is:{right_element.text}")
    # time.sleep(10)