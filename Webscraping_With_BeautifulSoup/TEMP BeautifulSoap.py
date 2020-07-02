import requests
from bs4 import BeautifulSoup

link1 = "http://www.aastocks.com/en/stocks/market/index/hk-index-con.aspx"
page1 = requests.get (link1)
soup1 = BeautifulSoup (page1.content, "html.parser")

erg_stock = {}
list = []

for e in soup1.find_all("a"):
    if e.get("title") != None and ".HK" in e.get("title"):
        list.append(e.get("title"))

erg_stock["hang-seng"] = list
for key, val in erg_stock.items (): print (key, val)











