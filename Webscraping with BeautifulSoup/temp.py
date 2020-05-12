from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import NamedStyle, Font, PatternFill, Border, Side
import pandas as pd

name_xlsx = "Test.xlsx"
wb =  load_workbook(name_xlsx)
wb._sheets.sort(key=lambda x: x.title)
if "INDEX" in wb.sheetnames: del wb["INDEX"]
wb.create_sheet("INDEX",0)
ws_idx = wb["INDEX"]
link_idx =  name_xlsx + "#" + "INDEX" + "!A1"
for i, ws in enumerate(wb):
    if ws.title == "INDEX": continue
    link = name_xlsx + "#" + ws.title + "!A1"
    ws_idx.cell (row=i+1, column=1).value = '=HYPERLINK("{}", "{}")'.format (link, ws.title)
    wb[ws.title].cell (row=1, column=6).value = '=HYPERLINK("{}", "{}")'.format (link_idx, "Back to INDEX")

while True:
    try:
        wb.save (name_xlsx)
        wb.close ()
        break
    except Exception as e:
        print ("Error: ", e)
        input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")









