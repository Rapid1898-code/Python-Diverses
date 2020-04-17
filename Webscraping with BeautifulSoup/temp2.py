import xlrd
import datetime
import csv
from datetime import datetime
from itertools import zip_longest

# Ausgabe der Liste als CSV-File
def csv_write(result, filename):
    while True:
        try:
            with open (filename,"w",newline="") as fp:
                a = csv.writer(fp,delimiter=",")
                a.writerows(result)
                break
        except:
            input ("Datei kann nicht geöffent werden - bitte schließen und <Enter> drücken!")
    fp.close()

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
#print(liste)

result = [list(filter(None,i)) for i in zip_longest(*liste)]
print(result)
csv_write(result, "testout.csv")










