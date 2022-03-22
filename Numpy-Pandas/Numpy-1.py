import numpy as np
import matplotlib

#https://www.runoob.com/numpy/numpy-string-functions.html     #教程
#数组
# a=numpy.array([1,2,3],dtype=complex)
# b=numpy.array([[1,2],[3,4]])
# print(a)
# print(b)


#维度
# a = np.arange(24)
# print (a.ndim)             # a 现只有一个维度
# # 现在调整其大小
# b = a.reshape(2,4,3)  # b 现在拥有三个维度
# print(b.ndim)
# print (b)


#shape调整
# a=np.array([[1,2,3],[4,5,6]])
# print(a.shape)
# a.shape=(3,2)
# print(a)

#创建空数组，元素值为随机值
# x=np.empty([3,3],dtype=int)#2,3为数组维度
# print(x)
# y=np.zeros([2,3],dtype=complex)#创建0数组
# print(y)

#动态数组建立，通过已有数组建立新数组
# s=b'Hello World'      #python默认str为Unicode类型，要加b
# a=np.frombuffer(s,dtype='S1',count=-1,offset=0)     #buffer可以是任意对象,count为切片读取数据量，offset为起始位置
# print(a)

#迭代建立数组
# list=range(24)
# it=iter(list)
# x=np.fromiter(it,dtype=complex)
# print(x)

# #数值范围创建数组
# # np.arange(start,stop,step,dtype)
# x=np.arange(1,12,2,dtype=int)
# print(x)
# # y=np.linspace(start,stop,num,dtype)  #等差数列

#切片索引
# x=np.arange(12)
# s=slice(2,11,3)
# print(x[s])
# y=x[1:12:2]
# print(y)
# z=x[3:]
# print(z)
# w=[[1,2,3],[4,4,5],[4,5,6]]
# r=w[1:]       #多维数组同样适用
# print(r)

#迭代数组
# a = np.arange(6).reshape(2,3)
# print ('原始数组是：')
# print (a)
# print ('\n')
# print ('迭代输出元素：')
# for x in np.nditer(a):     #nditer迭代
#     print (x, end=", " )
# print('\n')
# print(a.T)     #a的转置

#字符串函数
