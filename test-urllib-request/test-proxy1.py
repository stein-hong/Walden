import urllib.request

url='http://www.baidu.com'
headers='请求头'
pro_handler=urllib.request.ProxyHandler({'代理1','代理2'})
opener=urllib.request.build_opener(pro_handler)
urllib.request.install_opener(opener)                     #创建全局opener对象

request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
print(response.read().decode('utf-8'))