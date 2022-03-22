import xlwt
from xlwt import Workbook

book=xlwt.Workbook(encoding='utf-8')
sheet=book.add_sheet('菜鸟')
col=('A','B','C','D','E','F')
for i in range(0,6):
    sheet.write(0,i+1,col[i])
for j in range(0,6):
    sheet.write(j+1,0,'第{}条'.format(j+1))
data=[['a','b','c','d','e','f'],['0','1','2','3','4','5']]
for i in range(0,2):
    for j in range(0,6):
        sheet.write(i+1,j+1,data[i][j])
book.save('C:\\Users\\STEIN\\Desktop\\1\\菜鸟.xls')