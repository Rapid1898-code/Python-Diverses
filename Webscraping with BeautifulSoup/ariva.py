import requests
import csv
from bs4 import BeautifulSoup

page = requests.get ("https://www.ariva.de/dax-30")
soup = BeautifulSoup (page.content, "html.parser")
table  = soup.find(id="result_table_0")
for row  in table.find_all("td"):
    try:
        if row.get("class") == ['ellipsis', 'nobr', 'new', 'padding-right-5']:
            print(row.text)
            print(row.find("a")["href"])


        #print(row.get("class"))
        #print(row)
    except: continue





"""
page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2020-04-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")
soup = BeautifulSoup (page.content, "html.parser")

# read table with monatlichen Kursen
for result in soup.find_all("tr", class_="arrow0"):
    for row in result.find_all("td"):
        if row.get("class") == None \
                or row.get("class") == ['font-size-14', 'right', 'colwin']\
                or row.get("class") == ['font-size-14', 'right', 'colloss']:
                   print (row.text.strip())
"""


