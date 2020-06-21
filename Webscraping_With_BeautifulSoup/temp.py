import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from sys import platform
import urllib.request
import codecs
import csv
from datetime import datetime, timedelta

#link = "https://finance.yahoo.com/calendar/earnings/?symbol=AAPL"
link = "https://finance.yahoo.com/calendar/earnings/?symbol=BAYRY"

erg = {}
tmp_list = []
page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")
table  = soup.find(id="fin-cal-table")
for row in soup.find_all("td"): tmp_list.append(row.text.strip())
idx = 0

while idx < len (tmp_list):
    tmp = tmp_list[idx+2][:-3]
    dt1 = datetime.strptime (tmp, "%b %d, %Y, %I %p")
    dt2 = datetime.strftime(dt1, "%Y-%m-%d")
    erg[dt2] = [tmp_list[idx+0],tmp_list[idx+1],tmp_list[idx+3],tmp_list[idx+4],tmp_list[idx+5]]
    idx += 6
for key, val in erg.items (): print (key, val)



