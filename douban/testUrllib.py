import urllib.request


#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))        #中文解码utf-8


#获取一个post请求
# import urllib.parse   #解析器
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))



#get请求
# response=urllib.request.urlopen("http://httpbin.org/get")
# print(response.read().decode("utf-8"))




#伪装浏览器
# url="http://httpbin.org/post"
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")     #封装
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))




#伪装浏览器进入豆瓣
url="http://www.douban.com"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
req=urllib.request.Request(url=url,headers=headers)       #封装成req方便下述访问
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
