#coding:utf-8
import xlwt
book = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = book.add_sheet("demo",cell_overwrite_ok=False)
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'SimSun' # 指定“宋体”
style.font = font

def save(x,y,s):
    sheet.write(x,y,s)
    book.save('demo.xls')

