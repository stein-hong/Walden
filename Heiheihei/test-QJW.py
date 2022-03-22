import time
import os
import urllib
import selenium
from selenium import webdriver


def main():

    url = 'https://www.quanjing.com/image/'
    # paths=GetName(url)                                    #需要参数
    # print(paths)
    imgurls=FindButton(url)
    # ImgSave(imgurls)

def GetName(url):
    driver = webdriver.Firefox()
    driver.get(url)
    namelist = driver.find_elements_by_xpath('//div[@id="divImgHolder"]/ul/li/span[2]')
    i = 0
    paths = []
    namelists=[]
    for name in namelist:
        if i < 20:
            i_name = name.text
            # print(i_name)
            i = i + 1
            namelists.append(i_name)
            paths.append("C:\\Users\\STEIN\\Desktop\\quanjingwang\\" + str(i_name))
        else:
            break
    for path in paths:
        isExist=os.path.exists(path)
        if not isExist:
            os.makedirs(path)
        else:
            print("路径已存在")
            break
    driver.close()
    driver.quit()
    time.sleep(2)
    # print(paths)
    return paths


def FindButton(url):
    paths = GetName(url)
    driver = webdriver.Firefox()
    driver.get(url)
    for j in range(1, 3):
        findbutton = driver.find_elements_by_xpath('//span[@class="enter"]')
        findbutton[j].click()
        time.sleep(1)

        imgurls = []
        imglist = driver.find_elements_by_xpath('//ul[@id="gallery-list"]/li/a/img')
        # print(imglist)
        for k in range(2):
            imgurls.append(imglist[k].get_attribute("src"))
        # print(imgurls)
        ImgSave(imgurls,paths,j)
        # print(str(j))
        driver.back()
        time.sleep(2)
    driver.close()
    driver.quit()

def ImgSave(imgurls,paths,j):
    a = 0
    for img in imgurls:
        urllib.request.urlretrieve(img, paths[j] +'\\'+ '%s.jpg'%a)
        a=a + 1


if __name__ == "__main__":                # 程序执行时调用函数main
    main()
    print("爬取完毕!")