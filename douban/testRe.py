#正则表达式：字幅串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象
# pat=re.compile("AA")  #此处AA是正则表达式，用来去验证其他字符串
# #
# # #与
# m=pat.search("ABCAASAAA")   #一定要有AA才能匹配，只匹配第一个符合的
# #没有模式对象
# m=re.search("asd","Aasd")   #前面的字符串是规则，后面的是对象
# print(m)


# print(re.findall("a","SAAaKKaL"))    #前面是规则，后面被校验

#print(re.findall("[A-Z,a-z,\d]","SAAaK231KaL"))   #一个个摘出

#print(re.findall("[A-Z]+","SAAaKDKaL"))



#sub
#print(re.sub("a","A","abcdsxcd"))    #在第三个中找到a用A替换

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题，例如：
a=r"\aabd-\'"
print(a)
