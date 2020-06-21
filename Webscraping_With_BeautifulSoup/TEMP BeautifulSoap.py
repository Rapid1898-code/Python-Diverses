import requests
from bs4 import BeautifulSoup

link = "https://finance.yahoo.com/quote/AAPL/history?period1=345427200&period2=1592697600&interval=1d&filter=history&frequency=1d"
#link = "https://finance.yahoo.com/quote/CAT/key-statistics?p=CAT"

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

table  = soup.find(id="Col1-1-HistoricalDataTable-Proxy")
for e in table.find_all(["th","td"]): print(e.text.strip())
#print(tmp.prettify())
"""
for row in soup.find_all("tr"): print(row.prettify())
table = soup.find ('p', attrs={"class": "businessSummary Mt(10px) Ov(h) Tov(e)"})
spans = table.find_all ("span")
sector = spans[1].text.strip()
industry = spans[3].text.strip()
empl = spans[5].text.strip()
table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
description = table.find("p").text.strip()
print(sector)
print(industry)
print(description)
"""



