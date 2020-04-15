import requests
import csv
from datetime import datetime
from datetime import date
import calendar
from bs4 import BeautifulSoup
import pandas as pd
from itertools import zip_longest


# DAX-Unternehmen einlesen
# ["/wirecard-aktie", "/volkswagen_vz-aktie", "/fresenius-aktie", "/sap-aktie", "/bayer-aktie",
# "/deutsche_b%C3%B6rse-aktie", "/merck_kgaa-aktie", "/fresenius_medical_care-aktie", "/linde_plc-aktie",
# "/allianz-aktie", "/deutsche_post-aktie", "/covestro-aktie", "/henkel_vz-aktie", "/siemens-aktie",
# "/beiersdorf-aktie", "/continental-aktie", "/deutsche_telekom-aktie", "/bmw-aktie", "/vonovia-aktie",
# "/deutsche_bank-aktie", "/daimler-aktie", "/basf-aktie", "/adidas-aktie", "/rwe-aktie", "/munich_re-aktie",
# "/lufthansa-aktie", "/heidelbergcement-aktie", "/infineon-aktie", "/e-on-aktie", "/mtu_aero_engines-aktie"]
def dax_stocks ():
    page = requests.get ("https://www.ariva.de/dax-30")
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="result_table_0")
    dax = []
    for row  in table.find_all("td"):
        if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:
            dax.append(row.find("a")["href"])
            #print(row.find("a")["href"])
            #print(row.get("class"))
            #print(row)
    print(dax)


# Aktienkurse für eine Unternehmen einlesen
# boerse_id ist fix =>  6 = Xetra
# Input Stock: Aktienkennung lt. Ariva.de z.b. /apple-aktie oder /wirecard-aktie
# Input Month: Monatsultimo im Format z.B. 2019-04-30

def stock_prices (stock,month):
    url = "https://www.ariva.de" + stock + "/historische_kurse?boerse_id=6&month=" + month + "&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, "html.parser")
    # page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2020-04-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")

    # read table with monatlichen Kursen
    for result in soup.find_all("tr", class_="arrow0"):
        for col_id, col_content in enumerate(result.find_all("td")):
            if col_id == 0:     # 1.Spalte Datum
                yield "datum", col_content.text.strip()
            elif col_id == 4:   # 5.Spalte Schlusskurs
                yield "price", col_content.text.strip()

# Monatsultimo ermitteln für Zeitraum
# Input z.B. (3, 2015, datetime.now().month, datetime.now().year) bei Aufruf
# Output z.b. Ultimo-Datum z.b. 2016-04-30
def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range(ym_end, ym_start-1, -1):
        y, m = divmod( ym, 12 )
        #yield y,m+1
        #print(date(y,m+1,calendar.monthrange(y,m+1)[1]))
        yield date(y,m+1,calendar.monthrange(y,m+1)[1])


# Erstellung einer Datums-Liste vom aktuellstem bis zum  ältesten Datum im Format jjjj-mm-dd
def date_list (datum_von, datum_bis):
    mydates2  = []
    mydates = pd.date_range(datum_bis, datum_von).tolist()
    for i in range(len(mydates)-1,-1,-1): mydates2.append(mydates[i].strftime('%d.%m.%y'))
    return(mydates2)


"""
stocks = ["/apple-aktie","/wirecard-aktie", "/volkswagen_vz-aktie", "/fresenius-aktie", "/sap-aktie", "/bayer-aktie",
 "/deutsche_b%C3%B6rse-aktie", "/merck_kgaa-aktie", "/fresenius_medical_care-aktie", "/linde_plc-aktie",
 "/allianz-aktie", "/deutsche_post-aktie", "/covestro-aktie", "/henkel_vz-aktie", "/siemens-aktie",
 "/beiersdorf-aktie", "/continental-aktie", "/deutsche_telekom-aktie", "/bmw-aktie", "/vonovia-aktie",
 "/deutsche_bank-aktie", "/daimler-aktie", "/basf-aktie", "/adidas-aktie", "/rwe-aktie", "/munich_re-aktie",
 "/lufthansa-aktie", "/heidelbergcement-aktie", "/infineon-aktie", "/e-on-aktie", "/mtu_aero_engines-aktie",
 "/thyssenkrupp-aktie","/commerzbank-aktie","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
"""
stocks = ["/apple-aktie","/wirecard-aktie"]

start_year = 2020
start_month = 3
output = []
datelist = ["Datum"]
datelist.extend(date_list(date.today(), date(start_year, start_month,1)))
output.append(datelist)


# für jeden Aktientiel aus der Liste Ermittlung einer Zeile mit den Datümern und eine Zeile mit Schlusskursen
for stock in stocks:
    title_row = [stock]
    stock_row = [stock]
    for i in month_year_iter(start_month, start_year, datetime.now().month, datetime.now().year):
        for j in stock_prices(stock,str(i)):
            if j[0] == "datum":
                title_row.append(j[1])
#                print (j[1])
            elif j[0] == "price": stock_row.append(j[1])
            elif j[0] == "blank":
                stock_row.append(j[1])
                title_row.append(j[1])
    output.append(title_row)
    output.append(stock_row)


# Datum-Spalten vereinheitlichen
for i in range(1, len(output[0])-1):
    for j in range(1,len(output)-1):
        if j%2 == 1:
            if output[j][i] != output[0][i]:
                output[j].insert(i,"")
                output[j+1].insert (i, "")
        else: continue
# Check ob die letzte Spalte bei den Aktientiteln leer ist - sonst fehlt eine Spalte am Ende bei den Aktientiteln
for i in range(1,len(output)-1):
    if i%2 == 1 and len(output[0]) != len(output[i]):
        output[i].insert (len(output[i]), "")
        output[i + 1].insert (len(output[i+1]), "")

# Leere Spalten löschen
# kein Kurse für eine Aktie an diesem Tag
pos_del = []
for i in range(1, len(output[0])):
    empty=True
    for j in range (1, len (output) - 1):
        if output[j][i] != "":
            empty=False
            break
    if empty == True: pos_del.append(i)
pos_del.reverse()
for k in pos_del:
    for m in range (len(output)):
        del output[m][k]


# Transponieren der Tabelle und Ausgabe als CSV-File
result = output
#result = [list(filter(None,i)) for i in zip_longest(*output)]


# Ausgabe der Liste als CSV-File
with open ("prices_dax.csv","w",newline="") as fp:
    a = csv.writer(fp,delimiter=",")
    a.writerows(result)
