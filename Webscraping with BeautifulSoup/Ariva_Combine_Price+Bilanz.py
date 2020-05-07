import xlrd
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Border, Side
import pandas as pd

# read input-excel-sheets
filename = "Prices_Apple.xlsx"
wb_price = load_workbook(filename)
sh_price  = wb_price.active
stock = wb_price.sheetnames[0]
wb_data = load_workbook("Data_Apple.xlsx")
sh_data = wb_data.active

# read price xls in list
price_list = []
for row in sh_price.iter_rows():
    zeile = []
    for cell in row:
        if cell.value is None: zeile.append("")
        else: zeile.append(cell.value)
    price_list.append(zeile)

# read data xls in list
data_list = []
for row in sh_data.iter_rows():
    zeile = []
    for cell in row:
        if cell.value is None: zeile.append("")
        else: zeile.append(cell.value)
    data_list.append(zeile)

# find necessary rows
row_title = row_shares = 0
for i in range(len(data_list)-1):
    if "Bilanz in Mio." in data_list[i][0]: row_title = data_list[i]
    if "Aktien im Umlauf"  in data_list[i][0]: row_shares= data_list[i]

# calculate marketcap per day with daily price and yearly outstanding shares
tmp_year=0
tmp_shares=0
for i in range (1,len(price_list)):
    if price_list[i][0] == "": continue
    if datetime.strptime(price_list[i][0],"%d.%m.%Y") != tmp_year:
        for j in range(2,len(row_title)):
            if datetime.strptime(price_list[i][0],"%d.%m.%Y").year-1 == int(row_title[j]):
                tmp_year = int(row_title[j])
                tmp_shares = row_shares[j]
                break
    price_list[i][2] = round(price_list[i][1] * tmp_shares / 1000,2)
    price_list[i][1] = round(price_list[i][1],2)

# Überschrift ergänzen
if price_list[1][0] != "" and price_list[2][0] != "":
    price_list.insert(1,["","Price","MarketCap"])
    price_list.insert(2,["","Kurs","MarktKap"])

#  save XLSX
writer = pd.ExcelWriter (filename, engine='openpyxl', options={'strings_to_numbers': True})
wb_price.remove(sh_price)
writer.book = wb_price
pd.DataFrame (price_list).to_excel (writer, sheet_name=stock, header=False, index=False)
writer.book._sheets.sort(key=lambda x: x.title)

# Formatierung XLSX
column_widths = []
ws = writer.sheets[stock]
for row in price_list:
    for i, cell in enumerate (row):
        if len (column_widths) > i:
            if len (str (cell)) > column_widths[i]:
                column_widths[i] = len (str (cell))
        else:
            column_widths += [len (str (cell))]
for i, column_width in enumerate (column_widths):
    ws.column_dimensions[get_column_letter (i + 1)].width = column_width + 2

    bold = Font (bold=True)
    bg_yellow = PatternFill (fill_type="solid", start_color='fbfce1', end_color='fbfce1')
    bg_grey = PatternFill (fill_type="solid", start_color='babab6', end_color='babab6')
    bg_green = PatternFill (fill_type="solid", start_color='c7ffcd', end_color='fffbc7')
    frame_all = Border (left=Side (style='thin'), right=Side (style='thin'), top=Side (style='thin'),bottom=Side (style='thin'))
    frame_upanddown = Border (top=Side (style='thin'), bottom=Side (style='thin'))
    for cell in ws["A:A"]:
        cell.font = bold
        cell.fill = bg_green
        cell.border = frame_all
    for cell in ws["1:1"]:
        cell.font = bold
        cell.fill = bg_green
        cell.border = frame_all
    freeze = ws["B2"]
    ws.freeze_panes = freeze



while True:
    try:
        writer.save ()
        writer.close ()
        break
    except Exception as e:
        print ("Error: ", e)
        input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")
