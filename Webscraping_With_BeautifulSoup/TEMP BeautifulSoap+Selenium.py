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

stock = "AAPL"

erg = {}
tmp_list = []
link = "https://query1.finance.yahoo.com/v7/finance/download/" + stock + "?period1=345427200&period2=1592697600&interval=1d&events=history"
print ("Reading historical share price web data for", stock, "...")
ftpstream = urllib.request.urlopen (link)
csvfile = csv.reader (codecs.iterdecode (ftpstream, 'utf-8'))
for row in csvfile: tmp_list.append (row)
tmp_list.reverse ()
erg[tmp_list[-1][0]] = tmp_list[-1][1:]
for i in range (len (tmp_list)):
    erg[tmp_list[i][0]] = tmp_list[i][1:]
for key,val in erg.items(): print(key,val)

date = "1980-12-14"
print(read_dayprice(erg,date))

