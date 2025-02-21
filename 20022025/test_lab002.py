from selenium import webdriver
import time

def test_vwologin():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    session_id=driver.session_id
    print(session_id)
    title=driver.title
    print(title)
    assert title=="Login - VWO"