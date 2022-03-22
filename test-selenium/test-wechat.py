import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

driver=webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
driver.get("https://www.baidu.com/")
# driver=webdriver.Firefox()
# driver.get('https://www.baidu.com/')
baidu=driver.find_element_by_id('kw')
baidu.send_keys('北京理工大学')
baidu.send_keys(Keys.RETURN)
time.sleep(2)
school=driver.find_element_by_xpath('//h3[@class="t"]/a[1]')
# school_text=school.text
# print(school_text)
ActionChains(driver).move_to_element(school).click().perform()
# school.click()
time.sleep(2)
while 1:
    start=time.perf_counter()
    try:
        driver.find_element_by_xpath('/html/body/footer/div[1]/ul[1]/li[1]/a/h3')
        print('定位成功')
        end=time.perf_counter()
    except:
        print('定位失败')
print('定位时间：'+str(end-start))
# zhihui=driver.find_element_by_xpath('//div[@class="top_rt"]/a[3]')   #'/html/body/header/div[1]/div/div[2]/a[3]'
# ActionChains(driver).move_to_element(zhihui).click().perform()
time.sleep(5)
