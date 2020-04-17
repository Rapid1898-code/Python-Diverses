import pandas
import datetime
import csv
from itertools import zip_longest

# Ausgabe der Liste als CSV-File
def csv_write(result, filename):
    while True:
        try:
            with open (filename,"w",newline="") as fp:
                a = csv.writer(fp,delimiter=",")
                a.writerows(result)
                break
        except:
            input ("Datei kann nicht geöffent werden - bitte schließen und <Enter> drücken!")
    fp.close()

df = pandas.read_excel('DAX Price2.xlsx') # The options of that method are quite neat; Stores to a pandas.DataFrame object
products_list = [df.columns.values.tolist()] + df.values.tolist()
for i in range(len(products_list)):
    for j in range(len(products_list[0])):
        if type(products_list[i][j]) == pandas._libs.tslibs.timestamps.Timestamp:
            products_list[i][j] = products_list[i][j].strftime("%d.%m.%Y")
        if pandas.isnull(products_list[i][j]):
            products_list[i][j] = ""

print(products_list)



#result = [list(filter(None,i)) for i in zip_longest(*products_list)]
#result = products_list
#csv_write(result, "testout.csv")







