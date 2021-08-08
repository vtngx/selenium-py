import json
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="/Users/quan/Desktop/chromedriver.exe")
driver.get("https://www.facebook.com")

with open("account.json") as a:
    user = json.load(a)
    driver.find_element_by_name("email").send_keys(user["username"])
    driver.find_element_by_name("pass").send_keys(user["password"])

driver.find_element_by_name("login").click()

