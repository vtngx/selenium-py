from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")
print(driver.title)

search = driver.find_element_by_name("email")
search.send_keys("hoangtumis1997@gmail.com")

search = driver.find_element_by_name("pass")
search.send_keys("Nhonxinh1239@")
search.send_keys(Keys.ENTER)