import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

DRIVER = os.getenv('CHROME_DRIVER')
URL = os.getenv('URL_FB')
EMAIL = os.getenv('EMAIL_FB')
PASSWORD = os.getenv('PASSWORD_FB')

driver = webdriver.Chrome(DRIVER)
driver.get(URL)

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    email_input.send_keys(EMAIL)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass'))
    )
    password_input.send_keys(PASSWORD)
    
    # password_input.send_keys(Keys.RETURN)
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'login'))
    )
    login_button.click()
except:
    driver.close()