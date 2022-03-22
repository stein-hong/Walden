#获取cookies并保存到文件中

import http.cookiejar
import urllib.request

url='http://tieba.baidu.com'
filename='cookie.txt'

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open(url)

f=open(filename,'a')
for item in cookie:
    f.write(item.name+"="+item.value+'\n')
f.close()