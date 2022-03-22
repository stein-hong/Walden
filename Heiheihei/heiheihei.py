import re
import urllib
import urllib.request
from bs4 import BeautifulSoup


def main():
    url='http://www.netbian.com/mei/'
    datalist=getdata(url)
    save(datalist)

#正则
findp=re.compile('<img alt=.*src="(.*?)"/>')
findp1=re.compile('<img alt=".*" src="(.*?)"/>')


def getdata(url):
    datalist=[]
    html=Askurl(url)
    soup=BeautifulSoup(html,'html.parser')
    item=str(soup.find_all('div',class_="list"))
    # print(str(item))
    print(item)
    find=re.findall(findp1,item)
    for Find in find:
        print(Find)
        datalist.append(Find)
    # print(datalist)
    return datalist


def Askurl(url):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read().decode('GBK')
    # print(html)
    return html

def save(datalist):
    x=1
    for data in datalist:
        urllib.request.urlretrieve(data,'C:\\Users\\STEIN\\Desktop\\meizi\\'+'%s.jpg'%x)
        x=x+1

if __name__==main():
    main()
    print('爬取中')