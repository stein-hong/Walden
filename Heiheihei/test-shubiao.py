import time
import os
import urllib.request
import selenium
import base64
from selenium import webdriver
import pyautogui


driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
driver.set_window_size(100, 10000)
driver.get('https://www.drr69.com/meinv/11653.html')
pyautogui.FAILSAFE=True
pyautogui.moveTo(400, 400, duration=0.25)
for s in range(20):
    pyautogui.scroll(-600)
    time.sleep(0.5)
for j in range(20):
    pyautogui.scroll(1600)
    time.sleep(0.5)
# driver.quit()
