import time
import os
import urllib.request
import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

baseurl="https://www.2eabf188a3bf.com"
# findurl="https://www.69bhq.com/meinv/list-兔宝宝.html"
# findurl="https://www.69bhq.com/tupian/186334.html"
findurl = "https://www.69bhq.com/tupian/list-清纯唯美.html"

s = Service('D:\python\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get(findurl)
pyautogui.scroll(-1800)
time.sleep(0.5)
pyautogui.scroll(-3000)
time.sleep(0.5)
pyautogui.scroll(-7000)
time.sleep(0.5)
elements=driver.find_elements_by_xpath('//div[@id="tpl-img-content"]/li/a[2]/h3')
dirs=[]
for element in elements:
    dir=element.get_attribute('title')
    dirs.append(dir)