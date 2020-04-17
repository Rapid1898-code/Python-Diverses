import requests
import csv
import re
from bs4 import BeautifulSoup

# Ausgabe der Liste als CSV-File inkl. Prüfung ob Datei geöffnet ist
# Input content: ist eine Matrix Liste [[][]]
# Input filenmae: Name des CSVs-File
def csv_write(content,filename):
    while True:
        try:
            with open (filename,"w",newline="") as fp:
                a = csv.writer(fp,delimiter=",")
                a.writerows(content)
                break
        except:
            input ("Datei kann nicht geöffent werden - bitte schließen und <Enter> drücken!")

page = requests.get ("https://www.ariva.de/apple-aktie/bilanz-guv#stammdaten")
soup = BeautifulSoup (page.content, "html.parser")
table = soup.find_all ("div", class_="column twothirds table")
output = []
for i in table:
#    for j in i.find_all("tr", id=re.compile("^((?!Quartal).)*$")):
    for j in i.find_all ("tr"):
        print (j.prettify ())
        row = []
        for k in j.find_all("td"):
            row.append(k.text.strip())
        output.append(row)
#print(output)
#csv_write(output,"ariva_data.csv")



