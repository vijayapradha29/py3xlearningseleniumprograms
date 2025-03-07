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

def test_heatmap():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/analyze/osa/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()
    main_window_handle=driver.current_window_handle
    print("Before Click "+main_window_handle)

    # < div
    # ng -

    # class ="{'screenshot-thumb__show-msg' : (isHeatmapAvailable || isHeatmapAvailable === false), 'screenshot-thumb__click-msg' : (isHeatmapAvailable === undefined) }" evaluation-product="insights" data-qa="meqeqiwiwe" vwo-upgrade-new="(campaign.type === CampaignTypeEnum.ANALYZE_HEATMAP || campaign.type === CampaignTypeEnum.HEATMAP || campaign.isHeatmapEnabled) ? false : $root.FeatureFlags.HEATMAP_VARIATION_HEATMAPS" class ="ng-binding screenshot-thumb__click-msg" > View Heatmap < / div >
    list_of_elements=driver.find_elements(By.CSS_SELECTOR,"[data-qa='meqeqiwiwe']")
    # // div[ @ data - qa = "meqeqiwiwe"]
    action=ActionChains(driver)
    action.move_to_element(list_of_elements[1]).click().perform()
    time.sleep(15)
    all_handles=driver.window_handles
    for handle in all_handles:
        if handle!=main_window_handle:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.switch_to.frame("heatmap-iframe")

            #how to come out of iframe:
            #driver.switch.to.window(main_window_handle)-switch to parent window

            # < span
            # data - qa = "refoyekife" > Clickmap < / span >
            click_element=driver.find_element(By.XPATH,"//span[@data-qa='refoyekife']")
            click_element.click()
            time.sleep(20)
            driver.quit()

    # iframe:An HTML iframe is used to display a web page within a web page.An iframe, or Inline Frame, is an HTML element represented by the <iframe> tag. It functions as a ‘window’ on your webpage through which visitors can view and interact with another webpage from a different source.
    # Iframes are used for various purposes like:
    #
    # 1.Embedding Multimedia: Easily integrate videos, audio, or animations from platforms like YouTube, etc.
    # 2.Including Maps: Embed maps from services like Google Maps directly into your site.
    # 3.Loading Forms and Widgets: Incorporate forms or widgets from other sources without writing complex code.