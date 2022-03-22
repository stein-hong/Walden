import selenium
from selenium import webdriver
import os


bro=webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
bro.get("https://www.baidu.com/")

# chromedriver='D:\python\webdriver\chromedriver.exe'
# os.environ["webdriver.chrome.driver"]=chromedriver
# browser=webdriver.Chrome(chromedriver)
# browser.get('https://www.baidu.com/')



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s = Service(r'D:\python\webdriver\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get('https://www.baidu.com')
# driver.close()


#Firfox
# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.get('http://www.baidu.com/')


# from selenium import webdriver
# driver=webdriver.PhantomJS(executable_path="D:\\python\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
# driver.get("http://www.baidu.com/")
# data=driver.title
# driver.save_screenshot('baidu.jpg')
# print(data)