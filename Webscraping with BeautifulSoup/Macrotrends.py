# https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding

import requests
import datetime
import re
from bs4 import BeautifulSoup

URL = "https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="style-1")
# print(results.prettify())

entries = results.find_all("div", class_="col-xs-6")
entries.pop(0)
print(entries)

"""
    entries_final = []
    for i, entry in enumerate(entries):
        if i%2 != 0:
            continue
        else:
            datetime.datetime.strptime(entry, "%y/%m/%d")
    print(i, entry.text)
"""






