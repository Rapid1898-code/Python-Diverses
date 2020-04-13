# https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding

import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="style-1")
# print(results.prettify())

entries = results.find_all("td")
# print(entries)
for i, entry in enumerate(entries):
    print(i, entry.text)



