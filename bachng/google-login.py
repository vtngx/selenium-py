from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Enter the gmail ID:')
gmailId = input()
print('Enter pasword:')
passwd = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
try:
	driver.get('http://www.gmail.com/')
	driver.implicitly_wait(15)

	loginBox = driver.find_element_by_id('identifierId')
	loginBox.send_keys(gmailId)
	loginBox.send_keys(Keys.RETURN)

	passWordBox = driver.find_element_by_name('password')
	passWordBox.send_keys(passwd)
	passWordBox.send_keys(Keys.RETURN)

	print('Login Successful!!')
except:
	print('Login Failed')
