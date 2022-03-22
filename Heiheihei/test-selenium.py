import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver=webdriver.Firefox()
urllist=[]
for i in range(1,5):
    if i==1:
        url='http://www.netbian.com/mei/index.htm'
    else:
        url='http://www.netbian.com/mei/index_'+str(i)+'.htm'
        # print(url)
        driver.get(url)
        imglist=driver.find_elements_by_xpath('//div[@id="main"]/div[3]/ul/li/a/img')
        for img in imglist:
            i_img=img.get_attribute("src")
            # print(i_img)
            urllist.append(i_img)
# print(urllist)
x=1
for item in urllist:
    urllib.request.urlretrieve(item,'C:\\Users\\STEIN\\Desktop\\meizi\\'+'%s.jpg'%x)
    x=x+1
    print('已完成：'+str(x-1)+'张')