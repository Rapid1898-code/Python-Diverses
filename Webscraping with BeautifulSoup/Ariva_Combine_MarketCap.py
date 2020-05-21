from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import NamedStyle, Font, PatternFill, Border, Side
import pandas as pd

fn_price = "dax-30_Stock_Prices_EUR for free.xlsx"
wb_price = load_workbook(fn_price)
erg_list = []
for sh_price in wb_price:
    erg_row_date = erg_row_price = [sh_price.title]
    if sh_price.title in ["INDEX","HowTo"]: continue
    for row_cells in sh_price.iter_rows(min_col=1, max_col=2):
        if row_cells[0].value not in [None,"Date","Datum"]:
            erg_row_date.insert (1, row_cells[1].value)
            erg_row_date.insert (1, datetime.strptime(row_cells[0].value, "%d.%m.%Y"))
    erg_list.append(erg_row_date)
    erg_list.append (erg_row_price)
#Datums-Headline erstellen
erg_date = ["Datum"]
for i in erg_list:
    for j_idx, j_cont in enumerate(i):
        if j_idx%2 == 1 and j_cont not in erg_date: erg_date.append(j_cont)
erg_date.sort()
print(erg_date)

