#乘法口诀表
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")       #创建workbook对象
worksheet = workbook.add_sheet("sheet1")          #创建工作表
i=1
while i<=9:
    j=1
    while j<=9 and j<=i:
        data=i*j
        worksheet.write(i-1, j-1, '{}x{}={}'.format(j,i,data))
        j=j+1
    i=i+1

#worksheet.write(0,0,"hello")                     #写入数据，第一个参数为“行”，第二个为“列”，第三个是写入内容
workbook.save('student.xls')                     #保存表格

#或者循环写为：
# for i in range(0,9):
#     for j in range(0,i+1):
#         worksheet.write(i+1, j+1,"%d*%d = %d"%(i+1,j+1,(i+1)*(j+1)))