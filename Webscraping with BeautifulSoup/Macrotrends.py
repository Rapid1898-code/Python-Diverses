# https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding
import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.macrotrends.net/stocks/charts/AAPL/apple/shares-outstanding"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="style-1")
# print(results.prettify())

entries = results.find_all("div", class_="col-xs-6")
entries.pop(0)
# print(entries)

entries2 = entries[0].find_all("td")

time_ow = ""
row = ["AAPL"]
for i, entry in enumerate(entries2):
    if i%2 == 0: time_ow += entry
    else: row.append(int(entry))







