import selenium
import pyautogui
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
driver.get('https://www.runoob.com/mysql/mysql-tutorial.html')
sleep(3)
driver.quit()