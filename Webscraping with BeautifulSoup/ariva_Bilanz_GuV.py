import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font, PatternFill, Border, Side
import random
import subprocess
import time
import re
import sys

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
        except Exception as e:
            print ("Error: ", e)
            input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")

# Ausgabe der Liste als XLS-File inkl. Prüfung ob Datei geöffnet ist
# Input stock: Name der Aktie
# Input content: Inhalt in Listenform
# Input filenmae: Name des XLSX-File
# Input append: 1=>anhängen von neuen Worksheets, 0=>überschreiben des XLS
def save_xls(stock, content, filename, append):
    #check ob append ausgewählt - aber wenn file nicht vorhanden - dann Wechsel über Überschreibmodus 0
    try:
        book = load_workbook (filename)
    except:
        append = 0
    while True:
        try:
            if append == 0:
                writer = pd.ExcelWriter(filename, engine = 'openpyxl', options={'strings_to_numbers': True})
            elif append == 1:
                book = load_workbook (filename)
                writer = pd.ExcelWriter(filename, engine = 'openpyxl', options={'strings_to_numbers': True})
                writer.book = book
            pd.DataFrame(content).to_excel (writer, sheet_name=stock, header=False, index=False)
            break
        except Exception as e:
            print ("Error: ", e)
            input ("Datei kann nicht geöffnet werden - bitte schließen und <Enter> drücken!")

    # Automatische Anpassung der Spalten nach best fit
    column_widths = []
    ws = writer.sheets[stock]
    # Ermittlung des längsten Wertes pro Spalte
    for row in content:
        for i, cell in enumerate (row):
            if len (column_widths) > i:
                if len (str (cell)) > column_widths[i]:
                    column_widths[i] = len (str (cell))
            else:
                column_widths += [len (str (cell))]
    for i, column_width in enumerate (column_widths):
        # Spalte 2 mit langem Profil fix mit Breite 17 - restliche Spaten immer mit maximalen Wert pro Spalte
        if i == 1: ws.column_dimensions[get_column_letter (i + 1)].width = 17
        else: ws.column_dimensions[get_column_letter (i + 1)].width = column_width+2

    # Formatierung des Excel-Sheets
    bold = Font(bold=True)
    bg_yellow = PatternFill(fill_type="solid", start_color='fbfce1',end_color='fbfce1')
    bg_grey = PatternFill (fill_type="solid", start_color='babab6', end_color='babab6')
    fr = Border (left=Side (style='thin'),right=Side (style='thin'), top=Side (style='thin'), bottom=Side (style='thin'))

    # Formatierung Titelleiste Jahre
    for i,cont in enumerate (content):
        if cont == []: continue     # Leerzeile überspringen...
        if cont[0].find("Bilanz in ") != -1:
            row = i+1
            break

    for cell in ws["A:A"]:
        cell.font = bold
        cell.fill = bg_yellow
        cell.border = fr
    for cell in ws["1:1"]:
        cell.font = bold
        cell.fill = bg_yellow
        cell.border = fr
    for cell in ws["A1:A2"]: cell[0].fill = bg_yellow
    """    
    ws["C1"].font = bold
    ws["C1"].fill = bg_yellow
    ws["C1"].border = fr
    ws["E1"].font = bold
    ws["E1"].fill = bg_yellow
    ws["E1"].border = fr
    ws["G1"].font = bold
    ws["G1"].fill = bg_yellow
    ws["G1"].border = fr
    """
    for cell in ws[f"{row}:{row}"]:
        cell.font = bold
        cell.fill = bg_yellow
        cell.border = fr
    for cell in ws[f"{row-1}:{row-1}"]:
        cell.fill = bg_grey

    writer.save ()
    writer.close ()

# VPN-Switch bei NordVPN mit x Sekunden Verzögerung
# Output: Rückgabe des zufällig gewählten Landes
def vpn_switch(sek):
    countries = ["Austria", "Belgium", "Canada", "Germany", "Israel", "Italy","Bosnia and Herzogovina",
                 "Norway", "Poland", "Portugal", "Romania", "Serbia", "Switzerland", "United Kingdom",
                 "Bulgaria","Croatia","Denmark","Estonia","Finland","France","Gerogia","Greece","Hong Kong",
                 "Hungary","Iceland","India","Latvia","Netherlands"]
    rand_country = random.randrange(len(countries)-1)
    subprocess.call (["C:/Program Files (x86)/NordVPN/NordVPN.exe", "-c", "-g", countries[rand_country]])
    print ("VPN Switch to",countries[rand_country],"...")
    for i in range (sek, 0, -1):
        sys.stdout.write (str (i) + ' ')
        sys.stdout.flush ()
        time.sleep (1)
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

# Stammdaten für das Unternehmen lt. Parameter lesen
# Input Stock: Aktienkennung lt. Ariva.de z.b. /apple-aktie oder /wirecard-aktie
def read_stamm(stock):
    output = []
    link = "https://www.ariva.de" + stock + "/bilanz-guv?page=" + "0" + "#stammdaten"
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")

    # Stammdaten auslesen
    output.append(["STAMMDATEN",""])
    table = soup.find_all ("div", class_="column half")
    for i in table:
        for j in i.find_all ("tr"):
            row = []
            for k in j.find_all ("td"):
                if k.text.strip() == "": row.append ("-")
                else: row.append (k.text.strip())
            output.append (row)

    # Kontakte auslesen
    output[0].extend(["KONTAKT",""])
    table = soup.find_all ("div", class_="column half last")
    nr = 1
    for i in table:
        for j in i.find_all ("tr"):
            # Adresse wird unten vor der Zeile Management eingefügt, weil sie zu groß ist
            next_one_adress = False
            for k in j.find_all ("td"):
                if next_one_adress == True:
                    next_one_adress = False
                    if k.text.strip() == "": next_one_adress_row.append("-")
                    else: next_one_adress_row.append(k.text.strip())
                    continue
                if k.text.strip() == "Adresse":
                    next_one_adress = True
                    next_one_adress_row = ["Adresse"]
                    nr -= 1
                    continue
                if k.text.strip() == "": output[nr].append ("-")
                else: output[nr].append (k.text.strip())
            nr += 1

    # Termine auslesen
    table = soup.find_all ("div", class_="termine abstand new")
    nr = 1
    # Termine - Überschrift auslesen
    for i in table:
        cont = i.find("h3", class_="arhead undef").text.strip().upper()
        output[0].extend([cont,""])
    # Termine Inhalt auslesen
    for i in table:
        for j in i.find_all ("tr"):
            for k in j.find_all ("td"):
                #Prüfung ob Tag.Monat damit Jahr ergänzt wird
                pattern = '^[0-9][0-9].[0-9][0-9].$'
                if re.match(pattern, k.text.strip()): output[nr].append (k.text.strip()+cont[-4:])
                else: output[nr].append (k.text.strip())
            nr += 1

    # Aktionäre
    output[0].extend(["AKTIONÄRE",""])
    table = soup.find_all ("div", class_="aktStruktur abstand new")
    nr = 1
    for i in table:
        for j in i.find_all ("tr"):
            for k in j.find_all ("td"):
                if nr <= 10:
                    while (len(output[nr])<6): output[nr].append("")
                    output[nr].append (k.text.strip())
            nr += 1

    # Adresse von oben einfügen
    output.append(next_one_adress_row)

    # Management / Aufsichtsrat
    table = soup.find_all ("div", class_="management abstand new")
    for i in table:
        for j in i.find_all ("tr"):
            row = []
            for k in j.find_all ("td"):
                row.append (k.text.strip())
            output.append (row)

    # Profil
    table  = soup.find(id="profil_text")
    txt = ""
    for i in table.find_all ("p"):
        if txt == "": txt = txt + i.text.strip()
        else: txt = txt + " " + i.text.strip()
    output.append(["Profil",txt])

    return(output)

#stocks_dic = {'/apple-aktie': 'Apple', '/infineon-aktie': 'Infineon'}
stocks_dic = {'/bayer-aktie': 'Bayer'}

#Input-Parameter
#Input - Angabe welcher Index gelesen werden soll (z.B. DAX-30) - bei Angabe von 0 wird individuell lt. stocks_dic eingelesen
#Input - sek: Anzahl der Sekunden der Verzögerung bei VPN-Switch
index=0
vpn_land = "no-vpn"
#index="dax-30"
sek=17
#vpn_land = vpn_switch (sek)

if index != 0:
    stocks_dic = read_index(index)
for stock in stocks_dic:
    print("Verarbeitung ",stock," with VPN ",vpn_land)
    output = read_bilanz(stock)
    output_stamm = read_stamm(stock)
    output.insert(0,[])
    for i in range(len(output_stamm)-1,-1,-1):
        output.insert(0,output_stamm[i])
    save_xls(stocks_dic.get(stock), output, "Ariva_Data.xlsx" , 0)




