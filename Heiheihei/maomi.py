import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import


def main():
    url='https://www.86cfh.com/meinv/11655.html'
    datalist=getdata(url)
    # save(datalist)

#正则
findp=re.compile('<img alt=.*src="(.*?)"/>')
findp1=re.compile('<img alt=".*" src="(.*?)"/>')


def getdata(url):
    datalist=[]
    html=Askurl(url)
    soup=BeautifulSoup(html,'html.parser')
    item=str(soup.find_all('div',class_="content"))
    # print(str(item))
    print(item)
    find=re.findall(findp,item)
    for Find in find:
        # print(Find)
        datalist.append(Find)
    # print(datalist)
    return datalist


def Askurl(url):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
    # headers["Accept"] ="*/*"
    # headers["Accept-Encoding"] = "gzip, deflate"
    # headers["Accept-Language"] = "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
    # headers["Cache-Control"] = "max-age=0"
    # headers["Connection"] = "keep-alive"
    # headers["Cookie"] = "Hm_lvt_fe1ee127952183484aed5afc8a4cf0fd=1640424706; Hm_lpvt_fe1ee127952183484aed5afc8a4cf0fd=1640426543; _ga=GA1.2.346560733.1640424709; _gid=GA1.2.1953254209.1640424709"
    # headers["If-Modified-Since"] = "Sat, 11 Dec 2021 05:30:47 GMT"
    # headers["If-None-Match"] = "61b43787-df0"
    # headers["Referer"] = "http://mmgih7.com/"

    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    print(html)
    return html

def save(datalist):
    x=1
    for data in datalist:
        urllib.request.urlretrieve(data,'C:\\Users\\STEIN\\Desktop\\meizi\\'+'%s.jpg'%x)
        x=x+1

if __name__==main():
    main()
    print('爬取中')