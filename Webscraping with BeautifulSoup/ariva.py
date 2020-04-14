import requests
import csv
import datetime
import calendar
from bs4 import BeautifulSoup

"""
# DAX-Unternehmen einlesen
page = requests.get ("https://www.ariva.de/dax-30")
soup = BeautifulSoup (page.content, "html.parser")
table  = soup.find(id="result_table_0")
dax = []
for row  in table.find_all("td"):
    if row.get("class") == ['ellipsis', 'nobr', 'new', 'padding-right-5']:
        dax.append(row.find("a")["href"])
        #print(row.find("a")["href"])
        #print(row.get("class"))
        #print(row)
#print(len(dax))
"""

# Aktienkurse für eine Unternehmen einlesen
def stock_prices (stock,month):
    url = "https://www.ariva.de" + stock + "/historische_kurse?boerse_id=40&month=" + month + "&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0"
    page = requests.get (url)
    soup = BeautifulSoup (page.content, "html.parser")
    # page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2020-04-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")

    # read table with monatlichen Kursen
    for result in soup.find_all("tr", class_="arrow0"):
        for row in result.find_all("td"):
            if row.get("class") == None \
                    or row.get("class") == ['font-size-14', 'right', 'colwin']\
                    or row.get("class") == ['font-size-14', 'right', 'colloss']:
                       print (row.text.strip())

def month_year_iter( start_month, start_year, end_month, end_year ):
    ym_start= 12*start_year + start_month - 1
    ym_end= 12*end_year + end_month - 1
    for ym in range( ym_start, ym_end ):
        y, m = divmod( ym, 12 )
        #yield y, m+1
        #yield m+1, y
        yield datetime.date(y,m+1,calendar.monthrange(y,m+1)[1])

#stock = "/apple-aktie"
#month = "2020-04-30"
#stock_prices(stock,month)

for i in month_year_iter(8, 2010, 5, 2012):
    print (i)






