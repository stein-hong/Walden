#urllib代理
# import urllib.request
#
# url='http://myip.kkcha.com'
# proxies={
#     'http':'http://171.214.214.185:8118',
#     'https':'163.125.223.14:8118'
# }
# pro_support=urllib.request.ProxyHandler(proxies)
# opener=urllib.request.build_opener(pro_support)
# urllib.request.install_opener(opener)
# response=urllib.request.urlopen(url)



#requests代理设置
# import requests
#
# url='http://myip.kkcha.com'
# proxies={
#     'http':'http://171.214.214.185:8118'
# }
# response=requests.get(url,proxies=proxies)
# print(response.text)



#selenium代理
# from selenium import webdriver
#
# chromeoptions=webdriver.ChromeOptions()
# chromeoptions.add_argument("--proxy-server=http://171.233.252:555")
# driver=webdriver.Chrome(chrome_options=chromeoptions)
# driver.get("https://www.baidu.com")
# print(driver.page_source)
# driver.quit()



#ip随机切换
import random

iplist=['xxx.xxx.xxx:xxx','xxx.xxx.xxx:xxx']
proxies={'http':random.choice(iplist)}
