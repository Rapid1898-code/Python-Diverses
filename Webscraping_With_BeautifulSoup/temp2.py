import xlwings as xw
wb = xw.Book ("Test.xlsx")
ws_db = wb.sheets["Tabelle1"]
idx = 2
cell_list = ws_db.range ("A" + str(idx) + ":" + "C" + str(idx)).value
print(cell_list)
print(cell_list[1])
print(type(cell_list))
print(type(cell_list[1]))

cell_list = ["","",""]
ws_db.range ("A" + str (idx) + ":" + "C" + str (idx)).value = cell_list


