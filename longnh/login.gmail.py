from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Enter Email :')
gmailId = input()
print('Enter Password: ')
pwd = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
try:
	driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue='
			   'https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&'
			   'flowName=GlifWebSignIn&flowEntry=ServiceLogin')


	loginBox = driver.find_element_by_id('identifierId')
	loginBox.send_keys(gmailId)
	loginBox.send_keys(Keys.RETURN)

	passWordBox = driver.find_element_by_name('password')
	passWordBox.send_keys(pwd)
	passWordBox.send_keys(Keys.RETURN)

	print('Login Successful')
except:
	print('Login Failed')