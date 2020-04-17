import xlrd
import datetime
from datetime import datetime


workbook = xlrd.open_workbook ("DAX Price2.xlsx")
sheet = workbook.sheet_by_index (0)
liste = []
for row in range (sheet.nrows):
    zeile=[]
    for col in range(sheet.ncols):
        if sheet.cell(row,col).ctype == 3:
            zeile.append(datetime(*xlrd.xldate_as_tuple(sheet.cell(row,col).value,0)).strftime("%d.%m.%Y"))
        else:
            zeile.append(sheet.cell(row,col).value)
    liste.append(zeile)

print(liste)











