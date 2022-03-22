import pandas

#一维构建
#数组构建
# mat=pandas.Series([1,2,3],index=[2,4,6],dtype=int)
# print(mat)
#
# #键值构建
# fat={'a':'first','b':'second'}
# Fat=pandas.Series(fat)
# print(Fat)


#二维构建
# a=[['A','a'],['B','b'],['C','c']]
# cl=pandas.DataFrame(a,columns=['大写','小写'],index=['A1','B2','C3'])
# print(cl)


#打开csv文件
# df=pandas.read_csv('nba.csv')
# print(df.to_string())
# # print(df)       #只输出前后五行
# print(df.head(6).to_string())    #指定头部输出行数
# print(df.tail(7))    #指定尾部输出行数
# print(df.info())       #输出表格信息

#保存为csv
# name=['A','B','C']
# age=['23','33','12']
# adress=['bei','nan','xi']
# dic={'name':name,'age':age,'adress':adress}
# col=pandas.DataFrame(dic)
# col.to_csv('test.csv')


#数据清洗
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)  '''axis=0遇空值去掉整行，axis=1遇空值去掉整列；
#  how='all',how=’any‘,'thresh'为空值数门槛值，sbset为检查的列'''

# df=pandas.read_csv('property-data.csv')
# print(df['NUM_BEDROOMS'])  #输出指定列
# print (df['NUM_BEDROOMS'].isnull())  #判断空值


# new_df=df.dropna(axis=0,subset=['NUM_BEDROOMS'])     #删除空值
# print(new_df)

dic={'1':'2','a':'b'}
print(dic)