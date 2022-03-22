import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import os


os.system('adb shell input keyevent 26')
time.sleep(1)
os.system('adb shell input swipe 700 2000 690 1000')  #显示
time.sleep(0.2)
os.system('adb shell input tap 340 1700')
os.system('adb shell input tap 710 1450')
os.system('adb shell input tap 717 1919')
os.system('adb shell input tap 720 1700')
os.system('adb shell input tap 343 1921')
os.system('adb shell input tap 348 1450')

# os.system('adb shell input keyevent 26')