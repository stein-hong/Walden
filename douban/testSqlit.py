import sqlite3

# 1.连接数据库
# conn = sqlite3.connect("test1.db")     # 打开或者创建，如果没有test.db,将会默认创建一个
#
# print("Opened database successful")


# 2.创建数据表
# conn = sqlite3.connect("test1.db")     # 打开或者创建，如果没有test.db,将会默认创建一个
# print("成功打开数据库")
# c = conn.cursor()            # 获取游标
# sql = '''
#     create table company
#          (id int primary key not null,
#          name text not null,
#          age int not null,
#          address char(50),
#          salary real);
# '''
# c.execute(sql)                  # 执行
# conn.commit()               # 提交
# conn.close()             # 关闭
# print("成功建表")


# 3.插入数据
# conn = sqlite3.connect("test1.db")     # 打开或者创建，如果没有test.db,将会默认创建一个
# print("成功打开数据库")
# c = conn.cursor()            # 获取游标
# sql1 = '''
#     insert into company(id,name,age,address,salary)     # 插入数据
#     values(1,'张三',32,"成都",8000)
# '''
# sql2 = '''
#     insert into company(id,name,age,address,salary)
#     values(2,'李四',34,"北京",9000)
# '''
# c.execute(sql1)                  # 执行
# c.execute(sql2)
# conn.commit()               # 提交
# conn.close()             # 关闭
# print("插入数据完毕")


# 4.查询数据
conn = sqlite3.connect("test1.db")     # 打开或者创建，如果没有test.db,将会默认创建一个
print("成功打开数据库")
c = conn.cursor()            # 获取游标
sql = "select id,name,address,salary from company"
cursor = c.execute(sql)                  # 执行
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address=",row[2])
    print("salary=",row[3],"\n")
conn.close()             # 关闭
print("查询数据完毕")