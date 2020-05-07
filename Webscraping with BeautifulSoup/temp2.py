from openpyxl import load_workbook
import pandas as pd

# read XLSX
workbook = load_workbook("TEST.xlsx")
sheet = workbook["SHEET_A"]


# change to list
l=[]
for row in sheet:
    temp_row = []
    for cell in row:
        temp_row.append(cell.value)
    l.append(temp_row)

# manipulate list
l[1][1] = 1

# write back to XLSX
writer = pd.ExcelWriter ("TEST.xlsx", engine='openpyxl')
workbook.remove(sheet)
writer.book = workbook
pd.DataFrame (l).to_excel (writer, sheet_name="SHEET_A", header=False, index=False)
writer.book._sheets.sort(key=lambda x: x.title)
writer.save()
writer.close()
