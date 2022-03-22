import time
import os
import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox()
urllist=[]
namelists=[]
url='https://www.quanjing.com/image/'
# print(url)
driver.get(url)
namelist=driver.find_elements_by_xpath('//div[@id="divImgHolder"]/ul/li/span[2]')
i=0
paths=[]
for name in namelist:
    if i<20:
        i_name=name.text
        # print(i_name)
        i=i+1
        namelists.append(i_name)
        paths.append("C:\\Users\\STEIN\\Desktop\\quanjingwang\\" + str(i_name))
    else:
        break
for path in paths:
    os.makedirs(path)
print(namelists)
driver.close()
driver.quit()
time.sleep(3)

# findbutton=driver.find_elements_by_xpath('//span[@class="enter"]')
# print(findbutton[1].text)
for j in range(0,1):
    driver.get(url)
    findbutton = driver.find_elements_by_xpath('//span[@class="enter"]')
    findbutton[j].click()
    time.sleep(2)
    # imgUrl()
    # driver.back()
    # time.sleep(3)

# def imgUrl():
    imgurls=[]
    imglist=driver.find_elements_by_xpath('//ul[@id="gallery-list"]/li/a/img')
    for k in range(2):
        imgurls.append(imglist[k].get_attribute("src"))
    # print(imgurls)
    a=0
    for img in imgurls:
        urllib.request.urlretrieve(img,"C:\\Users\\STEIN\\Desktop\\quanjingwang\\成年\\"+'%s.jpg'%a)
        a+1
driver.close()
driver.quit()
# driver.close()
# driver.quit()
# urllist.append(i_img)
# print(urllist)
# x=1
# for item in urllist:
#     urllib.request.urlretrieve(item,'C:\\Users\\STEIN\\Desktop\\meizi\\'+'%s.jpg'%x)
#     x=x+1
#     print('已完成：'+str(x-1)+'张')
