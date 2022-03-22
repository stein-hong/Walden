#-*- codeing = utf-8 -*-

from bs4 import BeautifulSoup
import sqlite3
import re
import sys
import xlwt
import urllib.request,urllib.error

def main():
#基础网址
    baseurl="https://movie.douban.com/top250?start="
    datalist=getData(baseurl)
#保存数据
    savepath="豆瓣电影top250.xls"                  #保存到当前位置
    dbpath = "movie.db"
    saveData(datalist,savepath)
    # saveData2DB(datalist,dbpath)
#    askURL("https://movie.douban.com/top250?start=0")

#影片详情链接的规则
findLink=re.compile(r'<a href="(.*?)">')      #创建正则表达式对象，表示规则（字符串的模式）
#影片图片规则
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)   #re.S让换行符包含在字符中
#片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关内容
findBd = re.compile(r'<p class="">(.*?) </p>',re.S)

 #爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):       #调用获取页面信息函数
        url=baseurl + str(i*25)
        html=askURL(url)        #保存获取网页源码
#2.逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="item"):     #查找符合要求的字符串，形成列表,class是类别，要加下划线
            #print(item)    #测试，查看item信息
            data = []         #保存一部电影的所有信息
            item=str(item)

            #影片详情的链接
            link = re.findall(findLink,item)[0] #re库用正则表达式查找指定的字符串,0表示要第一个
            data.append(link)

            ImgSrc = re.findall(findImgSrc,item)[0]
            data.append(ImgSrc)

            titles = re.findall(findTitle,item) #片名可能只有一个中文名，没有英文名
            if (len(titles))==2:
                ctitle=titles[0]
                data.append(ctitle)               #添加中文名
                otitle=titles[1].replace("/","")   #去掉无关符号
                data.append(otitle)                #添加外国名
            else:
                data.append(titles[0])
                data.append(' ')                  #外国名留空，excel表格占位

            rating = re.findall(findRating,item)[0]   #评分
            data.append(rating)

            judgeNum=re.findall(findJudge,item)[0]     #评价人数
            data.append(judgeNum)

            inq = re.findall(findInq,item)        #添加概述（可能没有）
            if len(inq)!=0:
                inq=inq[0].replace("。","")        #去掉句号
                data.append(inq)
            else:
                data.append(" ")                   #留空
            bd=re.findall(findBd,item)[0]
            bd = re.sub("<br/\s+>?>(\s+)?"," ",bd)   #去掉br换行符
            bd = re.sub('/'," ",bd)                  #换掉/
            data.append(bd.strip())                   #去掉前后空格

            datalist.append(data)                    #把处理好的一部电影信息放入datalist
#    print(datalist)
    return datalist


#得到指定的一个URL网页内容
def askURL(url):
    head = {}
    head["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
              #表示告诉豆瓣我们是浏览器访问
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
 #       print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
           print(e.code)
        if hasattr(e,"reason"):
           print(e.reason)
    return html



def saveData(datalist,savepath):
    print("爬取中......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)       #创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)          #创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])       #列名
    for i in range(0,250):
        print("第%d条"%(i+1))          #行名
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])         #数据

    book.save(savepath)                     #保存表格到指定路径


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movies250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



def init_db(dbpath):
    sql = '''
    create table movies250
    (
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    instroduction text,
    info text
    )
    '''            # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":                # 程序执行时调用函数main
    main()
    #init_db("movietest.db")
    print("爬取完毕!")