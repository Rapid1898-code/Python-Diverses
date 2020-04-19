import xlrd     # Einlesen von Excel-Sheet
import requests
import csv
import datetime
import calendar
from bs4 import BeautifulSoup
import pandas as pd
from itertools import zip_longest
import timeit
import time
import random
import subprocess
import json


# DAX-Unternehmen einlesen
# DAX30 Unternehmen + Ex-Unternehmen
def dax_stocks ():
    page = requests.get ("https://www.ariva.de/dax-30")
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="result_table_0")
    dax = {}
    for row  in table.find_all("td"):
        if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:
            dax[row.find("a")["href"]] = row.text.strip()
            #print(row.find("a")["href"])
            #print(row.get("class"))
            #print(row)
    print(dax)


def vpn_switch():
    countries = ["Argentina", "Australia", "Austria", "Belgium", "Canada", "Germany", "Israel", "Italy",
                 "Norway", "Poland", "Portugal", "Romania", "Serbia", "Switzerland", "United Kingdom"]
    rand_country = random.randrange(len(countries)-1)
    subprocess.call (["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c", "-g", countries[rand_country]])
    time.sleep(30)  #Verzögerung von x Sekunden
    print ("Connected to ", countries[rand_country],"...")


# Aktienkurse für eine Unternehmen einlesen
# boerse_id ist fix =>  6 = Xetra
# Input Stock: Aktienkennung lt. Ariva.de z.b. /apple-aktie oder /wirecard-aktie
# Input Month: Monatsultimo im Format z.B. 2019-04-30
def stock_prices (stock,month):
    # read table with monatlichen Kursen
    url = "https://www.ariva.de" + stock + "/historische_kurse?boerse_id=6&month=" + month + "&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, "html.parser")
    # Check ob Zugriff auf die IP-Adresse gesperrt ist
    # wenn ja wird "abbruch" zurückgegeben und dadurch die weitere Verarbeitung gestoppt
    if "Kein Zugriff" in soup.text:
        print("Abbruch!!!")
        yield "abbruch", soup.text.strip()
    for result in soup.find_all("tr", class_="arrow0"):
        for col_id, col_content in enumerate(result.find_all("td")):
            # wenn Ausgabejahr nicht mit dem gesuchten Jahr zusammenpasst => break
            if col_id == 0 and (datetime.datetime.strptime(col_content.text.strip(), "%d.%m.%y").year !=
                                datetime.datetime.strptime(month, "%Y-%m-%d").year or
                                datetime.datetime.strptime (col_content.text.strip (), "%d.%m.%y").month !=
                                datetime.datetime.strptime (month, "%Y-%m-%d").month):
                break
            # Datum des Kurse bzw. Schlusskurs auslesen
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
        #print(datetime.date(y,m+1,calendar.monthrange(y,m+1)[1]))
        yield datetime.date(y,m+1,calendar.monthrange(y,m+1)[1])


# Erstellung einer Datums-Liste vom aktuellstem bis zum  ältesten Datum im Format jjjj-mm-dd
def date_list (datum_von, datum_bis):
    mydates2  = []
    mydates = pd.date_range(datum_bis, datum_von).tolist()
    for i in range(len(mydates)-1,-1,-1): mydates2.append(mydates[i].strftime('%d.%m.%y'))
    return(mydates2)


# Ausgabe der Liste als CSV-File
def csv_write(result, filename):
    while True:
        try:
            with open (filename,"w",newline="") as fp:
                a = csv.writer(fp,delimiter=",")
                a.writerows(result)
                break
        except:
            print("Datei ", filename, " kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")
            input()
    fp.close()


# Einlesen eines Ergebnis-XLS um die Datümer zusätzlich abzugleichen
# Durchgängiges Datum muss noch vorne ergänzt werden
def read_XLS():
    workbook = xlrd.open_workbook ("DAX Price2.xlsx")
    sheet = workbook.sheet_by_index (0)
    liste = []
    for row in range (sheet.nrows):
        zeile=[]
        for col in range(sheet.ncols):
            if sheet.cell(row,col).ctype == 3:
                zeile.append(datetime(*xlrd.xldate_as_tuple(sheet.cell(row,col).value,0)).strftime("%d.%m.%Y"))
            else:
                zeile.append(sheet.cell(row,col).value)
        liste.append(zeile)
    #print(liste)

    result = [list(filter(None,i)) for i in zip_longest(*liste)]
    print(result)
    csv_write(result, "testout.csv")


# DAX30 Unternehmen + Ex-Unternehmen
"""
stocks_dic = {'/apple-aktie': 'Apple', '/infineon-aktie': 'Infineon', '/volkswagen_vz-aktie': 'Volkswagen Vz', '/continental-aktie': 'Continental',
'/bmw-aktie': 'BMW St', '/heidelbergcement-aktie': 'HeidelbergCement', '/mtu_aero_engines-aktie': 'MTU Aero Engines', '/covestro-aktie': 'Covestro',
'/siemens-aktie': 'Siemens', '/daimler-aktie': 'Daimler', '/munich_re-aktie': 'Munich Re', '/basf-aktie': 'BASF', '/deutsche_bank-aktie': 'Dt. Bank',
'/deutsche_post-aktie': 'Dt. Post', '/adidas-aktie': 'adidas', '/allianz-aktie': 'Allianz', '/sap-aktie': 'SAP', '/deutsche_telekom-aktie': 'Dt. Telekom',
'/linde_plc-aktie': 'Linde PLC', '/bayer-aktie': 'Bayer', '/henkel_vz-aktie': 'Henkel Vz', '/lufthansa-aktie': 'Lufthansa', '/beiersdorf-aktie': 'Beiersdorf',
'/merck_kgaa-aktie': 'Merck KGaA', '/fresenius_medical_care-aktie': 'Fresenius Medical Care', '/deutsche_b%C3%B6rse-aktie': 'Dt. Börse', '/fresenius-aktie': 'Fresenius',
'/wirecard-aktie': 'Wirecard', '/rwe-aktie': 'RWE St', '/e-on-aktie': 'E.ON', '/vonovia-aktie': 'Vonovia', '/thyssenkrupp-akti': 'ThyssenKrupp',
'/commerzbank-aktie': 'Commerzbank', '/prosiebensat-1_media-aktie': 'ProSiebenSat-1 Media', '/uniper-aktie': 'Uniper', '/k-s-6-aktie': 'KS6',
 '/lanxess-aktie': 'Lanxess', '/osram_licht-aktie': 'Osram Licht', '/ceconomy_st-aktie': 'Ceconomy St', '/man-aktie': 'MAN', '/salzgitter-aktie': 'Salzgitter'
 , '/hannover_rück-aktie': 'Hannover Rück', '/tui-aktie': 'TUI', '/mlp-aktie': 'MLP'}
"""

stocks_dic = {'/apple-aktie': 'Apple', '/infineon-aktie': 'Infineon'}


#stocks = ["/prosiebensat-1_media-aktie","/linde_plc-aktie"]
#stocks = ["/apple-aktie","/wirecard-aktie", "/rwe-aktie", "/heidelbergcement-aktie","/volkswagen_vz-aktie"]
#stocks = ["/apple-aktie"]

#stocks = ["/volkswagen_vz-aktie", "/fresenius-aktie", "/sap-aktie", "/bayer-aktie",
# "/deutsche_b%C3%B6rse-aktie", "/merck_kgaa-aktie", "/fresenius_medical_care-aktie", "/linde_plc-aktie",
# "/allianz-aktie", "/deutsche_post-aktie", "/covestro-aktie", "/henkel_vz-aktie", "/siemens-aktie",
# "/beiersdorf-aktie", "/continental-aktie", "/deutsche_telekom-aktie", "/bmw-aktie", "/vonovia-aktie",
# "/deutsche_bank-aktie", "/daimler-aktie", "/basf-aktie", "/adidas-aktie", "/munich_re-aktie",
# "/lufthansa-aktie", "/infineon-aktie", "/e-on-aktie", "/mtu_aero_engines-aktie",
# "/thyssenkrupp-aktie","/commerzbank-aktie","/prosiebensat-1_media-aktie","/linde_plc-aktie","/uniper-aktie",
# "/k-s-6-aktie","/lanxess-aktie","/osram_licht-aktie","/ceconomy_st-aktie","/man-aktie","/salzgitter-aktie",
# "/hannover_rück-aktie","/infineon-aktie","/tui-aktie","/lanxess-aktie","/mlp-aktie","/daimler-aktie"]
#

start_gesamt = timeit.default_timer()
start_year = 2020
start_month = 4
end_year = 0
end_month = 0
if end_year == 0:
    end_year = datetime.datetime.now().year
    end_month = datetime.datetime.now().month
output = []
#Datumszeile erstellen für den gesamten Zeitraum pro Tag
datelist = ["Kürzel","Datum"]
datelist.extend(date_list(datetime.date.today(), datetime.date(start_year, start_month,1)))
output.append(datelist)

#Temp-Daten aus vorherigen Läufen einlesen...
try:
    with open("tempdata.txt") as f:
        for line in f:
            line = line.replace ("'", '"')
            output.append (json.loads (line.strip()))
except: pass

abbruch = False
print("Aktienkurse lesen...")
# für jeden Aktientiel aus der Liste Ermittlung einer Zeile mit den Datümern und eine Zeile mit Schlusskursen
start_readstocks = timeit.default_timer()
for stock in stocks_dic:
    if abbruch == True: break
    #check if stock ist bereits im Tempfile vorhanden
    skip = False
    for i in range(len(output)-1):
        if output[i][0] == stock:
            print(stock, " bereits in tempdata.txt vorhanden... daher skip...")
            skip = True
            break
    if skip == True:
        continue
    #switch der vpn-verbindung
    vpn_switch()
    start_stock = timeit.default_timer()
    title_row = [stock,stocks_dic.get(stock)]
    stock_row = [stock,stocks_dic.get(stock)]
    year = datetime.datetime.now().year
    if year <= end_year: print(stock + " " + str(year))
    for i in month_year_iter(start_month, start_year, end_month, end_year):
        if abbruch == True: break
        #Ausgabe zur Fortschrittskontrolle des Programms
        if i.year != year:
            year -= 1
            if year <= end_year: print(stock + " " + str(year))
        for j in stock_prices(stock,str(i)):
            if j[0] =="abbruch":
                abbruch = True
                break
            if j[0] == "datum":
                title_row.append(j[1])
            elif j[0] == "price": stock_row.append(j[1])
            elif j[0] == "blank":
                stock_row.append(j[1])
                title_row.append(j[1])
    output.append(title_row)
    output.append(stock_row)

    # Ausgabe der Zeilen in Temp-Textfile...
    print(title_row)
    print(stock_row)
    with open('tempdata.txt', 'a') as file:
        file.write("%s\n" %title_row)
        file.write ("%s\n" %stock_row)

    stop_stock = timeit.default_timer ()
    print("Laufzeit Aktie ",stock," : ",round((stop_stock-start_stock)/60,2),"min")
stop_readstocks = timeit.default_timer()

# csv_write([list(filter(None,i)) for i in zip_longest(*output)], "prices_dax_unordered.csv")
csv_write(list(zip_longest(*output)), "prices_dax_unordered.csv")

start_spaltenaufbereitung = timeit.default_timer()
print("Spalten bereinigen...")
# Datum-Spalten vereinheitlichen
for i in range(2, len(output[0])-1):
    for j in range(1,len(output)-1):
        if j%2 == 1:
            if i == len(output[j]):
                output[j].insert (i, "")
                output[j + 1].insert (i, "")
            elif output[j][i] != output[0][i]:
                output[j].insert(i,"")
                output[j+1].insert (i, "")
        else: continue
# Check ob die letzte Spalte bei den Aktientiteln leer ist - sonst fehlt eine Spalte am Ende bei den Aktientiteln
for i in range(2,len(output)-1):
    if i%2 == 1 and len(output[0]) != len(output[i]):
        output[i].insert (len(output[i]), "")
        output[i + 1].insert (len(output[i+1]), "")

# Leere Spalten löschen
# kein Kurse für eine Aktie an diesem Tag
pos_del = []

for i in range(2, len(output[0])):
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

print("Transponieren und Ausgeben...")
# Transponieren der Tabelle und Ausgabe als CSV-File
# result = output       #Output mit Datümern auf Spaltenebene - funktioniert nur bis zu einer gewissen Größe...

#result = [list(filter(None,i)) for i in zip_longest(*output)]
result = list(zip_longest(*output))

csv_write(result, "prices_dax_withdates.csv")

stop_spaltenaufbereitung = timeit.default_timer()
stop_gesamt = timeit.default_timer()
print("Gesamtlaufzeit: ", round((stop_gesamt-start_gesamt)/60,2), "min")
print("Aktienkurse Gesamt: ", round((stop_readstocks-start_readstocks)/60,2), "min")
print("Spaltenaufbereiung: ", round((stop_spaltenaufbereitung-start_spaltenaufbereitung)/60,2), "min")

