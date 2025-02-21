from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_vwologin():
    chrome_options=Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension',False)
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_argument("--window-size=1980x1080")
    # chrome_options.add_argument("--window-size=920x680")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-infobar")
    driver=webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(10)
