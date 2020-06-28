import requests
from bs4 import BeautifulSoup
import time

def is_na(value):
    if "N/A" in value: return "N/A"
    else:
        try:
            return (float(value))
        except ValueError:
            return (value)

stock = "UG.PA"
#stock = "AAPL"

erg = {}
print ("Reading profile web data for", stock, "...")
link = "https://finance.yahoo.com/quote/" + stock + "/profile?p=" + stock
page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")
time.sleep (0.5)
erg["symbol"] = stock

table = soup.find ('div', attrs={"class": "asset-profile-container"})
if table == None:
    print("None!")
else:
    spans = table.find_all ("span")

if len (spans[5].text.strip ()) == 0:
    erg["empl"] = "N/A"
else:
    erg["empl"] = int (spans[5].text.strip ().replace (",", ""))

erg["sector"] = spans[1].text.strip ()
erg["industry"] = spans[3].text.strip ()
table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
erg["desc"] = table.find ("p").text.strip ()

for key,val in erg.items(): print(key,val)
