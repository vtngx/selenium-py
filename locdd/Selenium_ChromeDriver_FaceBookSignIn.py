from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Enter your Email")
account = input()
print("Enter your password")
password = input()

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")
print(driver.title)

search = driver.find_element_by_name("email")
search.send_keys(account)

search = driver.find_element_by_name("pass")
search.send_keys(password)
search.send_keys(Keys.ENTER)