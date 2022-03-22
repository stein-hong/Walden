from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
driver.get("http://mail.163.com/")

elem_user=driver.find_element_by_name("email")
elem_user.send_keys('18811368698')
elem_password=driver.find_element_by_name("password")
elem_password.send_keys("42aaa")
elem_password.send_keys(Keys.RETURN)

time.sleep(3)
driver.close()
driver.quit()
