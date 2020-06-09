import xlwings as xw

wb = xw.Book('Example.xlsx')
sht1 = wb.sheets['Tabelle1']
sht1.range('E2').value = 45


