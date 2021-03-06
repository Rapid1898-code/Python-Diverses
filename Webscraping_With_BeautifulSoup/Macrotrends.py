# https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding
import requests
import csv
from bs4 import BeautifulSoup

data=[]
stocks=["/AAPL/apple/", "/SAP/sap-se/","/ADDYY/adidas-ag/","/BASFY/basf-se/",
        "/BAYRY/bayer/","/BAMXF/bmw/","/CTTAY/continental-ag/"]
# stocks=["/AAPL/apple/","/SAP/sap-se/","/ADDYY/adidas-ag/","/ALIZY/allianz-se/","/BASFY/basf-se/","/BAYRY/bayer/","/BAMXF/bmw/","/CTTAY/continental-ag/"]

def row_shares_outstanding(url,stock):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="style-1")
    # print(results.prettify())

    entries = results.find_all("div", class_="col-xs-6")
    entries.pop(0)
    # print(entries)

    entries2 = entries[0].find_all("td")

    time_ow = ""
    row = [stock]
    for i, entry in enumerate(entries2):
        if i%2 == 0: time_ow += " "+entry.text
        else:
            try:
                row.append(int(entry.text.replace(",","")))
            except:
                continue
    row.insert(1, time_ow)

    # print(time_ow)
    # print(row)
    return(row)

for stock in stocks:
    url= "https://www.macrotrends.net/stocks/charts"+stock+"shares-outstanding"
    tmp_row = row_shares_outstanding(url,stock)
    data.append(tmp_row)
# print(data)


with open ("marketshare.csv","w",newline="") as fp:
    a = csv.writer(fp,delimiter=",")
    a.writerows(data)



