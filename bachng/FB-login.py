from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Enter Facebook ID or Email:')
fbID = input()
print('Enter password:')
passwd  = input()

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

try:
    driver.get('https://www.facebook.com')
    driver.implicitly_wait(10)

    loginBox = driver.find_element_by_name('email')
    loginBox.send_keys(fbID)

    passWord = driver.find_element_by_name('pass')
    passWord.send_keys(passwd)
    passWord.send_keys(Keys.RETURN)

    print('Login Success')
except:
    print('Login Failed')