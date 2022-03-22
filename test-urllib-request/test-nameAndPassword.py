import urllib.request

url='http://tieba.baidu.com'
user='斯坦洪'
password='428571aaaylhxde'
pwdmgr=urllib.request.HTTPPasswordMgrWithDefaultRealm()    #实例化账号密码管理对象
pwdmgr.add_password(None,url,user,password)                #添加账号密码
auth_hander=urllib.request.HTTPBasicAuthHandler(pwdmgr)          #得到handler
opener=urllib.request.build_opener(auth_hander)            #获取opener对象
response=opener.open(url)
print(response.read().decode('utf-8'))