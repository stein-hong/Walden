import time
import os
import urllib.request
import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

findurl = "https://m.imooc.com/wenda/detail/543115"
# driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
s=Service('D:\python\webdriver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.set_window_size(100, 6000)
driver.get(findurl)
# driver.execute_script("window.scrollBy(0,3000)")  # 模拟浏览器下拉操作
# time.sleep(1)
# driver.execute_script("window.scrollBy(0,4500)")
# time.sleep(1)

# 定义一个初始值
temp_height=0
while True:
    # 循环将滚动条下拉
    pyautogui.moveTo(400, 400, duration=0.25)
    pyautogui.scroll(-600)
    # sleep一下让滚动条反应一下
    time.sleep(0.5)
    # 获取当前滚动条距离顶部的距离
    check_height = driver.execute_script(
        "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    # 如果两者相等说明到底了
    if check_height == temp_height:
        break
    temp_height = check_height

temp_height=0
while True:             #浏览器上拉
    # 循环将滚动条上拉
    pyautogui.moveTo(400, 400, duration=0.25)
    pyautogui.scroll(1800)
    # sleep一下让滚动条反应一下
    time.sleep(0.5)
    # 获取当前滚动条距离顶部的距离
    check_height = driver.execute_script(
        "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    # 如果两者相等说明到顶了
    if check_height == temp_height:
        break
    temp_height = check_height