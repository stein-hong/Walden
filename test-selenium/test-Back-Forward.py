import selenium
from selenium import webdriver
import time

bro=webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
bro.get("https://www.baidu.com/")
time.sleep(2)
bro.get("http://news.baidu.com")
time.sleep(1)
bro.back()
time.sleep(1)
bro.forward()


bro.refresh()      #刷新页面
bro.quit()