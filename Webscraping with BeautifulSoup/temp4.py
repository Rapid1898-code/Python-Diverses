import requests
from bs4 import BeautifulSoup

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