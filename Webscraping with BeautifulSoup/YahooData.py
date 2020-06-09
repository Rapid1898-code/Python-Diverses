import time
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# https://www.gurufocus.com/term/ev/BAYZF/Enterprise-Value/Bayer-AG
# https://www.gurufocus.com/term/ev/AAPL/Enterprise-Value/Apple

symbol = "AAPL"
link = "https://finance.yahoo.com/quote/"+symbol
link2 = link+"/profile?p="+symbol

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

# Read stockname, actual price, daychange
table = soup.find('div', id="quote-header-info")
name = table.find("h1").text.split("-")[1].strip()
price = soup.find('span', attrs={"data-reactid": "14"}).text.strip()
daychange_tmp = soup.find('span', attrs={"data-reactid": "16"}).text.strip().split("(")
daychange = daychange_tmp[0].strip()
daychange_perc = daychange_tmp[1].strip().replace(")","")

# Read Volumes
table = soup.find('div', id="quote-header")
volume = soup.find('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip()
avg_volume = soup.find('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip()

# Read Ranges
d_r_tmp = soup.find('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip().split('-')
day_range_from, day_range_to = d_r_tmp[0].strip(), d_r_tmp[1].strip()
f_r_temp = soup.find('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip().split('-')
fifty_range_from, fifty_range_to = f_r_temp[0].strip(), f_r_temp[1].strip()

# Read MarketCap, PrevClose, PE, EPS
marketcap = soup.find('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip()
prevclose = soup.find('td', attrs={"data-test": "PREV_CLOSE-value"}).text.strip()
pe_ratio = soup.find('td', attrs={"data-test": "PE_RATIO-value"}).text.strip()
eps_ratio = soup.find('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip()
print(prevclose)

for row in soup.find_all('td'): print(row)

# Read Additional Infos
page = requests.get (link2)
soup = BeautifulSoup (page.content, "html.parser")
empl = soup.find('span', attrs={"data-reactid": "30"}).text.strip()
sector_tmp = soup.find_all('span', attrs={"data-reactid": "21"})
for row in sector_tmp:
    if row.get("class") != None: sector = row.text.strip()
industry_tmp = soup.find_all('span', attrs={"data-reactid": "25"})
for row in industry_tmp:
    if row.get("class") != None: technology = row.text.strip()
description = soup.find('p', attrs={"data-reactid": "141"}).text.strip()
print(empl)
print(technology)
print(description)

print("\nALERT TRACKER")
print("Symbol:", symbol)
print("Name:", name)
print("Sector:", sector)
print("Price:", price)
print("DayChange:",daychange)
print("DayChange_Perc:",daychange_perc)
print("MarketCap:", marketcap)
print("PE-Rato:", pe_ratio)
print("EPS-Ratio:", eps_ratio)
print("52W Low:", fifty_range_from)
print("52W HIgh:", fifty_range_to)
print("\nDASHBOARD")

print("Current Volume:", volume)
print("Average Volume:", avg_volume)
print("Day Low/High:", day_range_from,"/", day_range_to)
print("52W Range:", fifty_range_from,"/",fifty_range_to)
















