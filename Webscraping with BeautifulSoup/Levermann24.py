import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook

indizes = ["dax","mdax","dow-jones"]
erg = []

for index in indizes:
    tmp_l = []
    url = "https://levermann24.com/" + index + "/"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="index_table")
    for row  in table.find_all("td"):
        tmp_l.append(row.text.strip().upper().replace("*","").replace("VZ.",".").replace(".",""))
    for i in range(0, len(tmp_l), 17):
        tmp_entry = [tmp_l[i]]
        for j in tmp_l[i+2:i+16]: tmp_entry.append(j)
        erg.append(tmp_entry)
erg.sort()

fn = "Lever24.xlsx"
writer = pd.ExcelWriter (fn, engine='openpyxl',options={'strings_to_numbers': True})
pd.DataFrame (erg).to_excel (writer, sheet_name="Score",header=False, index=False)
writer.save()
writer.close()





