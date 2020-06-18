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
pprint(col)

cell = sheet.cell(1,2).value  # Get the value of a specific cell
pprint(cell)

sheet.update_cell(2,2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet
print(numRows)
print(len(data))

# sheet.delete_rows(4)

insertRow = [10, "NEW","NEW"]
#sheet.append_row(insertRow)
sheet.insert_row(insertRow,2)

