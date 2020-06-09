import time
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# https://www.gurufocus.com/term/ev/BAYZF/Enterprise-Value/Bayer-AG
# https://www.gurufocus.com/term/ev/AAPL/Enterprise-Value/Apple

link = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

# Read actual price
table = soup.find('div', id="quote-header-info")
erg = table.find('div', attrs={"class": ""})
for idx,cont in enumerate(erg):
    if idx==0: print(cont.text)

# Read Stock Name
name = table.find("h1")
print (name.text.strip())

table = soup.find('div', id="quote-header")
volume = soup.find('td', attrs={"data-test": "TD_VOLUME-value"})
print(volume.text.strip())
avg_volume = soup.find('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"})
print(avg_volume.text.strip())

for row in table.find_all("td"):
    print(row)







