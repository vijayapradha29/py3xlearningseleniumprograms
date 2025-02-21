from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_extension():
    chrome_options=Options()
    chrome_options.add_extension("C:/Users/Dhivya/Desktop/AdBlock.crx")
    driver=webdriver.Chrome(chrome_options)
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    time.sleep(10)