import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import random
import subprocess
import time

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

# Ausgabe der Liste als XLS-File inkl. Prüfung ob Datei geöffnet ist
# Input stock: Name der Aktie
# Input content: Inhalt in Listenform
# Input filenmae: Name des XLSX-File
# Input append: 1=>anhängen von neuen Worksheets, 0=>überschreiben des XLS
def save_xls(stock, content, filename, append):
    #check ob append ausgewählt - aber file nicht vorhanden - dann Wechsel über Überschreibmodus 0
    try:
        book = load_workbook (filename)
    except:
        append = 0
    while True:
        try:
            if append == 0:
                writer = pd.ExcelWriter(filename, engine = 'openpyxl', options={'strings_to_numbers': True})
            else:
                book = load_workbook (filename)
                writer = pd.ExcelWriter(filename, engine = 'openpyxl', options={'strings_to_numbers': True})
                writer.book = book
            pd.DataFrame(content).to_excel (writer, sheet_name=stock, header=False, index=False)
            writer.save ()
            writer.close ()
            break
        except:
            input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")

# VPN-Switch bei NordVPN mit x Sekunden Verzögerung
# Output: Rückgabe des zufällig gewählten Landes
def vpn_switch(sek):
    countries = ["Argentina", "Australia", "Austria", "Belgium", "Canada", "Germany", "Israel", "Italy",
                 "Norway", "Poland", "Portugal", "Romania", "Serbia", "Switzerland", "United Kingdom"]
    rand_country = random.randrange(len(countries)-1)
    subprocess.call (["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c", "-g", countries[rand_country]])
    print ("VPN Switch to",countries[rand_country],"...")
    time.sleep(sek)  #Verzögerung von x Sekunden
    print ("Connected to",countries[rand_country],"...")
    return(countries[rand_country])

# Unternehmen eines bestimmten Index werden eingelesen
# Output: Dict in der Form Kürzel von Ariva.de + Name des Titels (z.b '/apple-aktie': 'Apple')
def read_index(index_name):
    page = requests.get ("https://www.ariva.de/"+index_name)
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="result_table_0")
    index_stocks = {}
    for row  in table.find_all("td"):
        if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:
            index_stocks[row.find("a")["href"]] = row.text.strip()
    #Dict sortieren nach Value
    index_stocks = {k: v for k, v in sorted(index_stocks.items(), key=lambda item: item[1])}
    return(index_stocks)

# Kennzahlen für das Unternehmen lt. Parameter lesen
# Input Stock: Aktienkennung lt. Ariva.de z.b. /apple-aktie oder /wirecard-aktie
def read_bilanz(stock):
    output_temp = []
    output_gesamt = []
    seite = 0
    jahre_titelleiste = []

    while True:
        link = "https://www.ariva.de" + stock + "/bilanz-guv?page=" + str(seite) + "#stammdaten"
        page = requests.get (link)
        soup = BeautifulSoup (page.content, "html.parser")
        #Kennzahlen auslesen
        table = soup.find_all ("div", class_="column twothirds table")
        for i in table:
            for j in i.find_all ("tr"):
                #print (j.prettify(),"\n")
                row = []
                for k in j.find_all("td"):
                    #print (k.prettify (), "\n")
                    row.append(k.text.strip())
                output_temp.append(row)
        #Bereinigung und Formatierung
        for i in range(len(output_temp)-1,0,-1):
            #Quartalswerte entfernen
            if "Quartal" in output_temp[i][0]: del output_temp[i]
            #Leerzeilen entfernen + Überschriften Aktive/Passiva
            empty = True
            for j in range(1, len(output_temp[0])-1):
                if output_temp[i][j] != "": empty = False
            if empty == True: del output_temp[i]
            #Doppelte Jahreszahlen entfernen
            if i != 0 and output_temp[i] == output_temp[0]: del output_temp[i]
            #Formate und Texte anpassen

            """
            text_dic = {'Umsatz': 'Revenue in M', 'Bruttoergebnis vom Umsatz': 'Gross Profit in M ', 'Operatives Ergebnis (EBIT)': 'EBIT in M',
                        'Finanzergebnis':'Financial Result in M','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val',
                        }
            """

        #Eckdaten Kennzahlen ermitteln und links oben im Sheet speichern
        if seite == 0:
            table = soup.find_all ("h3", class_="arhead undef")
            for i in table:
                if "Bilanz" in i.text and "Geschäftsjahresende" in i.text:
                    output_temp[0][0] = "Bilanz in Mio. " + i.text.strip()[18:22] + " per " + i.text.strip()[-7:-1]

        #Einfügen weiterer Jahreswerte
        if output_temp[0][1:7] == jahre_titelleiste:
            break
        else:
            jahre_titelleiste = output_temp[0][1:7]
            seite +=6
            if output_gesamt == []:
                output_gesamt = output_temp
            else:
                for i in range(len(output_temp[0])-1,1,-1):
                    if output_temp[0][i] in output_gesamt[0][1:len(output_gesamt[0])-1]: continue
                    else:
                        pos_insert = i
                        break
                for i in range(pos_insert,0,-1):
                    for j in range (len(output_gesamt)):
                        output_gesamt[j].insert(1, output_temp[j][i])
                        if j > 0 and output_gesamt[j][0] != output_temp[j][0]:
                            print("FEHLER !!! Beschriftung unterschiedlich in Output-Gesamt und Output-Temp in Zeile: ",j)
            output_temp = []

    #Leerspalten bereinigen (wo nur "-" enthalten ist
    #Tausender-Punkte entfernen
    for i in range (len(output_gesamt[0])-1,0,-1):
        #Check ob Spalte nur aus Blank oder "-" besteht
        empty=True
        for j in range(len(output_gesamt)):
            if j != 0 and  output_gesamt[j][i] not in ["-",""]: empty=False
            #Tausenderpunkte entfernen
            output_gesamt[j][i] = output_gesamt[j][i].replace (".", "")
            #Umwandlung von Zahlen mit M im Text für Millionen
            if output_gesamt[j][i].find("M") != -1:
                output_gesamt[j][i] = output_gesamt[j][i].replace (",", ".")
                output_gesamt[j][i] = output_gesamt[j][i].replace("M", "").strip()
                output_gesamt[j][i] = round(float(output_gesamt[j][i])*1000000,0)
            #Umwandlung auf float (nur mit "." und nicht mit "," möglich - daher Umwandlung
            try:
                output_gesamt[j][i] = output_gesamt[j][i].replace (",", ".")
                output_gesamt[j][i] = float (output_gesamt[j][i])
            except:
                continue
        if empty==True:
            for j in range (len(output_gesamt)):
                del output_gesamt[j][i]
    return output_gesamt

stocks_dic = {'/apple-aktie': 'Apple', '/infineon-aktie': 'Infineon'}
#stocks_dic = {'/apple-aktie': 'Apple'}

#Input-Parameter
#Input - Angabe welcher Index gelesen werden soll (z.B. DAX-30) - bei Angabe von 0 wird individuell lt. stocks_dic eingelesen
#Input - sek: Anzahl der Sekunden der Verzögerung bei VPN-Switch
index=0
sek=30
vpn_land = vpn_switch (sek)
if index != 0:
    stocks_dic = read_index(index)
for stock in stocks_dic:
    print("Verarbeitung ",stock," with VPN ",vpn_land)
    output = read_bilanz(stock)
    save_xls(stocks_dic.get(stock), output, "Ariva_Data.xlsx" , 1)




