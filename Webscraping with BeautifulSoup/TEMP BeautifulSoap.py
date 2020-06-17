import requests
from bs4 import BeautifulSoup

link = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"
#link = "https://finance.yahoo.com/quote/CAT/key-statistics?p=CAT"

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

tmp = soup.find('div', attrs={"data-reactid": "51"})
for row in soup.find_all("div"): print(row.prettify())

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



