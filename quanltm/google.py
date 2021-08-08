from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/Users/quan/Desktop/chromedriver.exe")
driver.get("http://www.gmail.com/")

driver.find_element_by_id("identifierId").send_keys("-------@fpt.edu.vn")


driver.find_element_by_class_name('VfPpkd-vQzf8d').click()
time.sleep(3)

driver.find_element_by_class_name('whsOnd').send_keys("-----")

driver.find_element_by_class_name("VfPpkd-vQzf8d").click()


