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
#link = "https://finance.yahoo.com/quote/" + stock + "/financials?p=" + stock
link = "https://www.wsj.com/market-data/quotes/XE/XETR/BAYN/research-ratings"
options = Options()
options.add_argument('--headless')
if platform == "win32": driver = webdriver.Chrome (os.getcwd () + '/chromedriver.exe', options=options)
elif platform =="linux": driver = webdriver.Chrome (os.getcwd () + '/chromedriver', options=options)
driver.get(link)                                               # Read link

#time.sleep(1)                                                  # Wait till the full site is loaded
#driver.find_element_by_name("agree").click()
#time.sleep (2)
#driver.find_element_by_xpath ('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span').click ()
#time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')        # Read page with html.parser

#time.sleep (2)
driver.quit ()
div_id = soup.find(id="historicalCol")
erg = {}
tmp = []
for row in div_id.find_all("span"):
    if len(row.text.strip()) != 0: tmp.append(row.text.strip())

for i in tmp: print(i)

erg["Header"] = ["Current","1 Month Ago","3 Month Ago"]
idx_tmp = 0
while idx_tmp < len(tmp):
    if tmp[idx_tmp] in ["Buy","Overweight","Hold","Underweight","Sell"]:
        erg[tmp[idx_tmp]] = [int(tmp[idx_tmp+3]),int(tmp[idx_tmp+2]),int(tmp[idx_tmp+1])]
        idx_tmp += 4
    else: idx_tmp += 1

sum_rat = 0
count_rat = 0
for idx,cont in enumerate(["Buy","Overweight","Hold","Underweight","Sell"]):
    sum_rat += erg[cont][0] * (idx+1)
    count_rat += erg[cont][0]
rat = round(sum_rat / count_rat,2)
erg["Rating"] = [rat,'1Buy to 5Sell']

for key, val in erg.items (): print (key, val)



