from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Enter your Email")
account = input()
print("Enter your password")
password = input()

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.gmail.com/")
print(driver.title)

search = driver.find_element_by_name("identifier")
search.send_keys(account)
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    main.send_keys(password)
    main.send_keys(Keys.RETURN)
except:
    driver.quit()


