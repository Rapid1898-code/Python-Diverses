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

def is_na(value):
    if "N/A" in value: return "N/A"
    else: return value

def read_dayprice(prices,date):
    nr = 0
    while nr < 100:
        if date in prices: return (date, erg[date][3])
        else:
            dt1 = datetime.strptime (date, "%Y-%m-%d")
            newdate = dt1 - timedelta (days=1)
            date = datetime.strftime (newdate, "%Y-%m-%d")
            nr +=1
    return ("1900-01-01",999999999)

stock = "HLMA.L"

erg = {}
link = "https://finance.yahoo.com/quote/" + stock + "/financials?p=" + stock
print("Reading income statement web data for", stock, "...approx 6sec...")
options = Options()
options.add_argument('--headless')
if platform == "win32": driver = webdriver.Chrome (os.getcwd () + '/chromedriver.exe', options=options)
elif platform =="linux": driver = webdriver.Chrome (os.getcwd () + '/chromedriver', options=options)
driver.get(link)                                               # Read link
time.sleep(2)                                                  # Wait till the full site is loaded
driver.find_element_by_name("agree").click()
time.sleep (2)
driver.find_element_by_xpath ('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span').click ()
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')        # Read page with html.parser
time.sleep (2)
driver.quit ()
div_id = soup.find(id="Col1-1-Financials-Proxy")

list_div = []
table = soup.find (id="quote-header-info")
for e in div_id.find_all (["div"]): list_div.append (e.text.strip ())
while list_div[0] != "Breakdown": list_div.pop (0)
for i in range (len (list_div) - 1, 0, -1):
    if list_div[i].replace (".", "").replace (",", "").replace ("-", "").isdigit () or list_div[i] == "-": continue
    elif i == len (list_div) - 1: del list_div[i]
    elif len (list_div[i]) == 0: del list_div[i]
    elif len (list_div[i]) > 50: del list_div[i]
    elif list_div[i] == list_div[i - 1]: del list_div[i]
    elif list_div[i + 1] in list_div[i]: del list_div[i]

for i in list_div: print(i)
