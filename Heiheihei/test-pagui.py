import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import xlwt

pattern1=re.compile('<a href="(.*?)" target="_blank">')
pattern2=re.compile('<a href=".*?" target="_blank" title=".*?">(.*?)</a>')
pattern3=re.compile('(.*?)</dd>')
pattern4=re.compile('<li><a class="score" href=".*"><strong>(.*?)</strong>')

baseurl='https://you.ctrip.com/sight/beijing1/s0-p'
datalist=[]
for i in range(1,10):
    url=baseurl+str(i)+'.html#sightname'
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    # print(html)
    soup=BeautifulSoup(html,'html.parser')
    sights=soup.find_all('div',class_='list_mod2')
    # print(sights[1])
    for sight in sights:
        data=[]
        item=str(sight)
        href=re.findall(pattern1,item)[0]
        data.append(href)
        # print(href)

        name=re.findall(pattern2,item)[0]
        data.append(name)
        # print(name)

        address=re.findall(pattern3,item)[0]
        data.append(address.replace(' ',''))
        # print(address)

        score=re.findall(pattern4,item)
        if len(score)!=0:
            data.append(score[0])
        else:
            data.append(' ')
        # print(score)

        datalist.append(data)
    # print(datalist)
workbook=xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet('1')
sheethead=['网址','景点名称','地址','评分']
for i in range(0,4):
    worksheet.write(0,i,sheethead[i])

for i in range(0,len(datalist)):
    for j in range(0,4):
        worksheet.write(i+1,j,datalist[i][j])
    i=i+1
workbook.save('11.xls')
