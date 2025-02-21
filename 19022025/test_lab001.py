# import selenium

from selenium import webdriver
import pytest


def test_sample():
    driver=webdriver.Chrome()
    driver.get("https://www.thetestingacademy.com")
    assert driver.current_url=="https://thetestingacademy.com/"