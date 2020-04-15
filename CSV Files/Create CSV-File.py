# DevNami: https://www.youtube.com/watch?v=T8IJ59s8ZoE

import csv

while True:
    try:
        with open("test.csv","w",newline="") as fp:
            a = csv.writer (fp, delimiter=",")
            data = [["Stock", "Sales"],
                    ["100", "24"],
                    ["120", "33"],
                    ["99", "666"]]
            a.writerows (data)
            break
    except:
        input("Datei kann nicht geöffent werden - bitte schließen und <Enter> drücken!")



