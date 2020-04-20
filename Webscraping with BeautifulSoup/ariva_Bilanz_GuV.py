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
    output_temp = []
    output_gesamt = []
    seite = 0
    jahre_titelleiste = []

    # output_gesamt initial definieren
    # output bilden für seite (+bereinigung)
    # SPRUNG1: aktuelle titelzeitleiste speichern
    # seite um 6 erhöhen
    # output bilden für (neue) seite (+bereinigung)
    # wenn titelzeitleiste = gespeicherte titelzeitleiste => Break! aus while True Schleife und return des ergebnises
    # ermitteln welche Spalten eingefügt werden müssen
        #von rechts nach links lesen
        #wenn Jahr schon vorhanden => skip
        #wenn Jahr noch nicht vorhanden => an Pos1 in output_gesamt einfügen für jede Zeile (evt. inkl. Überprüfung ob Text zusammenpasst)
    # zu SPRUNG1

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
            #Leerzeilen entfernen
            empty = True
            for j in range(len(output_temp[0])-1):
                if output_temp[i][j] != "": empty = False
            if empty == True: del output_temp[i]
            #Doppelte Jahreszahlen entfernen
            if i != 0 and output_temp[i] == output_temp[0]: del output_temp[i]
            text_dic = {'Umsatz': 'Revenue in M', 'Bruttoergebnis vom Umsatz': 'Gross Profit in M ', 'Operatives Ergebnis (EBIT)': 'EBIT in M',
                        'Finanzergebnis':'Financial Result in M','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val','key':'val',
                        }
            #Formate und Texte anpassen

        #Eckdaten Kennzahlen ermitteln und links oben im Sheet speichern
        if seite == 0:
            table = soup.find_all ("h3", class_="arhead undef")
            for i in table:
                if "Bilanz" in i.text and "Geschäftsjahresende" in i.text:
                    output_temp[0][0] = "Bilanz in Mio. " + i.text.strip()[18:22] + " per " + i.text.strip()[-7:-1]

        #Einfügen weiterer Jahreswerte

        #print (output_temp[0][1:7])
        #print (jahre_titelleiste)

        if output_temp[0][1:7] == jahre_titelleiste:
            break
        else:
            jahre_titelleiste = output_temp[0][1:7]
            seite +=6;
            if output_gesamt == []:
                output_gesamt = output_temp
            else:

                print ("drinne!", len(output_temp[0]))

                for i in range(len(output_temp[0])-1,1,-1):

                    print(i)
                    #print(output_temp[0][i])
                    #print(output_gesamt[0][1:len(output_gesamt[0])-1])

                    if output_temp[0][i] in output_gesamt[0][1:len(output_gesamt[0])-1]: continue
                    else:
                        pos_insert = i
                        break
                for i in range(pos_insert,1,-1):
                    for j in range (0,len(output_gesamt)-1):
                        output_gesamt[j][1] = output_temp[j][i]
                        if j > 0 and output_gesamt[j] != output_temp[j]:
                            print("Beschriftung unterschiedlich in Output-Gesamt und Output-Temp in Zeile: ",j)
            output_temp = []
    return output


stocks_dic = {'/apple-aktie': 'Apple'}
for stock in stocks_dic:
    output = read_bilanz(stock)
csv_write(output,"ariva_data.csv")



