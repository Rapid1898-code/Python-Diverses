import requests
from bs4 import BeautifulSoup

link = "https://finance.yahoo.com/quote/CAT/profile?p=CAT"
page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")
table = soup.find('section', attrs={"class": "quote-sub-section Mt(30px)"})
print(table.find("p").text.strip())





