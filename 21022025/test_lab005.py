from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_pageload():
    chrome_options=Options()
    chrome_options.add_argument("--page-load-strategy=none")
    driver=webdriver.Chrome()
    chrome_options.add_extension("C:/Users/Dhivya/Desktop/AdBlock.crx")
    driver.get("https://app.vwo.com")

