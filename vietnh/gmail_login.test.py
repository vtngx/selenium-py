import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

DRIVER = os.getenv('CHROME_DRIVER')
URL = os.getenv('URL_GMAIL')
EMAIL = os.getenv('EMAIL_GG')
PASSWORD = os.getenv('PASSWORD_GG')

driver = webdriver.Chrome(DRIVER)
driver.get(URL)

try:
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'identifier'))
    )
    email_input.send_keys(EMAIL)
    email_input.send_keys(Keys.RETURN)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

except: 
    driver.close()
