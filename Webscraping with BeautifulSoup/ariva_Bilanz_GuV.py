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

def read_bilanz(stock):
    output = []
    page = 0

    # output_gesamt initial definieren
    # output bilden für page (+bereinigung)
    # SPRUNG1: aktuelle titelzeitleiste speichern
    # page um 6 erhöhen
    # output bilden für (neue) page (+bereinigung)
    # wenn titelzeitleiste = gespeicherte titelzeitleiste => Break! aus while True Schleife und return des ergebnises
    # ermitteln welche Spalten eingefügt werden müssen
        #von rechts nach links lesen
        #wenn Jahr schon vorhanden => skip
        #wenn Jahr noch nicht vorhanden => an Pos1 in output_gesamt einfügen für jede Zeile (evt. inkl. Überprüfung ob Text zusammenpasst)
    # zu SPRUNG1

    while True:
        link = "https://www.ariva.de" + stock + "/bilanz-guv?page=" + page + "#stammdaten"
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
                output.append(row)
        #Bereinigung und Formatierung
        for i in range(len(output)-1,0,-1):
            #Quartalswerte entfernen
            if "Quartal" in output[i][0]: del output[i]
            #Leerzeilen entfernen
            empty = True
            for j in range(len(output[0])-1):
                if output[i][j] != "": empty = False
            if empty == True: del output[i]
            #Doppelte Jahreszahlen entfernen
            if i != 0 and output[i] == output[0]: del output[i]
            text_dic = {'Umsatz': 'Revenue in M', 'Bruttoergebnis vom Umsatz': 'Gross Profit in M ', 'Operatives Ergebnis (EBIT)': 'EBIT in M',
                        'Finanzergebnis':'Financial Result in M','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val',
                        }
            #Formate und Texte anpassen


        #Eckdaten Kennzahlen ermitteln und links oben im Sheet speichern
        if page == 0:
            table = soup.find_all ("h3", class_="arhead undef")
            for i in table:
                if "Bilanz" in i.text and "Geschäftsjahresende" in i.text:
                    output[0][0] = "Bilanz in Mio. " + i.text.strip()[18:22] + " per " + i.text.strip()[-7:-1]

stocks_dic = {'/apple-aktie': 'Apple'}
for stock in stocks_dic:
    read_bilanz(stock)
csv_write(output,"ariva_data.csv")



