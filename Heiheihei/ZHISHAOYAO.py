import time
import os
import urllib.request
import selenium
import pyautogui
from selenium import webdriver


def main():
    baseurl="https://www.2eabf188a3bf.com"
    findurl="https://www.73c96f2ca5d4.com/meinv/list-兔宝宝"

    URLLIST=FindUrl(baseurl, findurl)
    paths=SetPath(URLLIST)
    allimg=GetUrl(URLLIST,baseurl)

    x=0
    for items in allimg:
        a = 0
        for item in items:
            urllib.request.urlretrieve(item, paths[x] +'\\'+ '%s.jpg' % a)
            a=a+1
        x=x+1


def FindUrl(baseurl,findurl):
    URLLIST = []
    for i in range(1,2):
        URL=findurl+"-"+str(i)+".html"
        driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
        driver.set_window_size(100, 6000)
        # opt=ChromeOptions()              #无界面测试
        # opt.headless=True
        driver.get(URL)
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
    return URLLIST


def GetUrl(URLLIST,baseurl):
    # print(URLLIST[1])
    allimg = []
    for url in URLLIST:
        imglist=[]
        driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
        driver.set_window_size(100, 10000)
        driver.get(url)

        pyautogui.FAILSAFE = True        #浏览器下拉
        pyautogui.moveTo(400, 400, duration=0.25)
        for s in range(150):
            pyautogui.scroll(-600)
            time.sleep(0.5)
        for j in range(50):
            pyautogui.scroll(1600)
            time.sleep(0.5)

        imgs=driver.find_elements_by_xpath('//div[@class="content"]/img')
        for item in imgs:
            i_img=item.get_attribute("src")
            imglist.append(i_img)
        allimg.append(imglist)
        driver.quit()
    # print(allimg[0][2])
    return allimg


def SetPath(URLLIST):
    paths=[]
    for url in URLLIST:
        driver = webdriver.Chrome(executable_path='D:\python\webdriver\chromedriver.exe')
        driver.set_window_size(100, 10000)
        driver.get(url)
        driver.execute_script("window.scrollBy(0,3000)")  # 模拟浏览器下拉操作
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,7000)")
        time.sleep(1)

        Name=driver.find_elements_by_xpath('//div[@class="content"]/img')
        name=Name[0].get_attribute("title")
        path="D:\\M\\"+str(name)
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