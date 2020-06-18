import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("testpython").sheet1  # Open the spreadhseet
#sheet = client.open("entries").sheet1  # Open the spreadhseet
#sheet = client.open("stocksheet").sheet1  # Open the spreadhseet
sheet_data = sheet.get_all_records()  # Get a list of all records
#print(data,"\n")
#pprint(data)

#print(sheet_data[0])
#sheet_data[0]["Entry"] = 50
#print(sheet_data[0])
#sheet.batch_update(sheet_data)

idx="9"
cell_list = sheet.range("A" + idx + ":" + "C" + idx)
new_values = [1,2,3]
for i, val in enumerate(new_values): cell_list[i].value = val
sheet.update_cells(cell_list)
