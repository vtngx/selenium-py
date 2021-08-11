from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Enter Email :')
fbId = input()
print('Enter Password: ')
pwd = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
try:
	driver.get('https://www.facebook.com/')


	loginBox = driver.find_element_by_id('email')
	loginBox.send_keys(fbId)
	loginBox.send_keys(Keys.RETURN)

	passWordBox = driver.find_element_by_name('password')
	passWordBox.send_keys(pwd)
	passWordBox.send_keys(Keys.RETURN)

	print('Login Successful')
except:
	print('Login Failed')