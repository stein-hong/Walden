import re

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# 1.Tag,标签及其内容；默认拿到第一个内容


# print(bs.title.string)
#2.NavigableString, 只获取标签里的内容


# print(bs.a.attrs)
#3.拿到一个标签里的所以属性，以键值对显示


# print(type(bs))
#BeautifulSoup 表示整个文档


# print(bs.a.string)
#.comment,输出内容不包含注释符号


##############

#文档遍历
# print(bs.head.contents)
#print(bs.head.contents[1])


#文档搜索
#1.find all(),某一个标签
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# for i in t_list:
#     print(t_list[1])


#正则表达式搜索：使用search,标签里有“a”就匹配
# import re
# t_list=bs.find_all(re.compile("a"))
# print(t_list)


#传入一个函数，根据函数要求搜索
def name_is_exist(tag):
    return tag.has_attr("value")
t_list=bs.find_all(name_is_exist)
for item in t_list:
    print(item)                #一条条输出更好看


#2.kwards   参数
# t_list=bs.find_all(class_=True)
# for item in t_list:
#     print(item)


#3.text参数
#t_list=bs.find_all(text="hao123")
#或者：
#t_list=bs.find_all(text=["hao123","地图","贴吧"])
# t_list=bs.find_all(text=re.compile("\d"))             #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)


#4.limit参数
# t_list=bs.find_all("a",limit=3)  #只获取三条
# for item in t_list:
#     print(item)


#CSS选择器
#t_list=bs.select("title")   #通过标签查找
#t_list=bs.select(".mnav")     #通过类名查找
#t_list=bs.select("#u1")      #通过id查找
#t_list=bs.select("a[class]")   #通过属性查找
#t_list=bs.select("head>title")  #通过子标签查找
# for item in t_list:
#     print(item)