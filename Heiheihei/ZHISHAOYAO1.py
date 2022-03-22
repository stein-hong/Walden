# 修改版-1
import time
import os
import shutil
import urllib.request
import selenium
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def main():
    baseurl="https://www.2eabf188a3bf.com"
    # findurl="https://www.69bhq.com/meinv/list-兔宝宝"
    findurl = "https://www.69bhq.com/tupian/list-清纯唯美"
    dirpath,URLLIST=FindUrl(baseurl, findurl)
    paths=SetPath(dirpath,URLLIST)
    allimg=GetUrl(URLLIST,baseurl,paths)

    x=0
    for items in allimg:
        a = 0
        for item in items:
            urllib.request.urlretrieve(item, paths[x] +'\\'+ '%s.jpg' % a)
            a=a+1
        x=x+1


def FindUrl(baseurl,findurl):
    dirpath=[]
    URLLIST = []
    for i in range(1,2):
        URL=findurl+"-"+str(i)+".html"
        print(URL)
        dirpath.append(URL)
    for page in dirpath:
        s = Service('D:\python\webdriver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.set_window_size(100, 6000)
        driver.get(page)
        driver.execute_script("window.scrollBy(0,3000)")  # 模拟浏览器下拉操作
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,4500)")
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,6000)")
        time.sleep(1)
        urllist=driver.find_elements_by_xpath('//div[@id="tpl-img-content"]/li/a[1]')
        for url in urllist:
            i_url=url.get_attribute("href")
            URLLIST.append(i_url)
            # print(i_url)
        driver.quit()
    return (dirpath,URLLIST)


def GetUrl(URLLIST,baseurl,paths):
    # print(URLLIST[1])
    pathnum=0
    allimg = []
    for url in URLLIST:
        s = Service('D:\python\webdriver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        panduan=driver.find_elements_by_xpath('//ul[@class="scroll-content"]/li/a')
        if panduan is None:
            shutil.rmtree(paths[pathnum])
            pathnum=pathnum+1
            driver.quit()
            continue
        else:
            pathnum=pathnum+1
            imglist=[]
            driver.set_window_size(100, 10000)
            driver.get(url)

            pyautogui.FAILSAFE = True        #浏览器下拉
            pyautogui.moveTo(400, 400, duration=0.25)

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


            imgs=driver.find_elements_by_xpath('//div[@class="content"]/img')
            for item in imgs:
                i_img=item.get_attribute("src")
                imglist.append(i_img)
            allimg.append(imglist)
            driver.quit()
        # print(allimg[0][2])
    return allimg


def SetPath(dirpath,URLLIST):
    paths=[]
    # dirs = []
    # for url in URLLIST:
    for url in dirpath:
        print(url)
        s = Service('D:\python\webdriver\chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.set_window_size(100, 10000)
        driver.get(url)
        driver.execute_script("window.scrollBy(0,3000)")  # 模拟浏览器下拉操作
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,7000)")
        time.sleep(1)

        # Name=driver.find_elements_by_xpath('//div[@class="content"]/img')
        # name=Name[0].get_attribute("title")
        elements = driver.find_elements_by_xpath('//div[@id="tpl-img-content"]/li/a[2]/h3')
        for element in elements:
            dir = element.get_attribute('title')
            # dirs.append(dir)
            path="D:\\M\\"+str(dir)
            paths.append(path)
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
            else:
                print("路径已存在")
        driver.quit()
    return paths


if __name__ == "__main__":                # 程序执行时调用函数main
    main()
    print("爬取完毕!")