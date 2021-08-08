import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

DRIVER = os.getenv('CHROME_DRIVER')
URL = os.getenv('URL_FPT')

driver = webdriver.Chrome(DRIVER)
driver.get(URL)

# get web page title
title = driver.title
print('Title: ', title, '\n')

try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'element-item'))
    )

    links = []
    # print all links from grid elements
    for element in elements:
        # print(element.text)
        hyperlink = element.find_element_by_tag_name('a')
        links.append(hyperlink.text)

    # find and navigate to dai-hoc-fpt
    for l in links:
        link = driver.find_element_by_link_text(l)
        link.click()
        
        title = driver.title
        url = driver.current_url.replace(URL,'') if (URL in driver.current_url) else driver.current_url
        print('Navigated to:', title, 'at', url)
        
        driver.back()
        # driver.forward()

finally:
    time.sleep(5)

    # close tab
    # driver.close()
    
    # close browwser
    driver.quit()