import requests
import csv
from datetime import datetime
from datetime import date
import calendar
from bs4 import BeautifulSoup


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
# boerse_id 6 = Xetra
def stock_prices (stock,month):
    url = "https://www.ariva.de" + stock + "/historische_kurse?boerse_id=6&month=" + month + "&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, "html.parser")
    # page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2020-04-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")

    # read table with monatlichen Kursen
    for result in soup.find_all("tr", class_="arrow0"):
        for row in result.find_all("td"):
            if row.get("class") == None:
                yield "datum", row.text.strip()
            elif row.get("class") == ["font-size-14", "right", "colwin"]\
                  or row.get("class") == ["font-size-14", "right", "colloss"]:
                yield "price", row.text.strip()

# Monatsultimo ermitteln
def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range(ym_end, ym_start-1, -1):
        y, m = divmod( ym, 12 )
        #yield y,m+1
        yield date(y,m+1,calendar.monthrange(y,m+1)[1])


stocks = ["/apple-aktie","/wirecard-aktie","/volkswagen_vz-aktie"]
end_year = 2019
output = []

for stock in stocks:
    title_row = [stock]
    stock_row = [stock]
    for i in month_year_iter(1, end_year, datetime.now().month, datetime.now().year):
        for j in stock_prices(stock,str(i)):
            if j[0] == "datum": title_row.append(j[1])
            if j[0] == "price": stock_row.append(j[1])
    output.append(title_row)
    output.append(stock_row)
    print (title_row)
    print (stock_row)









