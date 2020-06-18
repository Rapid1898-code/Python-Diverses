import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("testpython").sheet1  # Open the spreadhseet
data = sheet.get_all_records()  # Get a list of all records
print(data,"\n")
pprint(data)

row = sheet.row_values(3)  # Get a specific row
pprint(row)

col = sheet.col_values(3)  # Get a specific column
print("Col: ",col)

cell = sheet.cell(1,2).value  # Get the value of a specific cell
pprint(cell)

sheet.update_cell(2,2, "CHANGED")  # Update one cell

sheet.update_cell(3,3,"UPDATE")

numRows = sheet.row_count  # Get the number of rows in the sheet
# sheet.delete_rows(4)

insertRow = [10, "NEW","NEW"]
#sheet.append_row(insertRow)
sheet.insert_row(insertRow,2)
sheet.sort((1, 'asc'), (2, 'des'), range='A2:G20')
print(sheet.cell (2, 3).value)
print(len(sheet.get_all_records()))
