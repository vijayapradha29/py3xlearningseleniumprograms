
from selenium import webdriver

def test_open_vwologin():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    page=driver.page_source
    print(page)