# pyinstaller --onefile --hidden-import pycountry --exclude-module matplotlib StockMA2.py
# .env file with gmail-token in it

# import StockCrawler as yc
# import RapidTechTools as rtt
from datetime import datetime, timedelta
from datetime import date
import os
import xlwings as xw
import time
import sys
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import sqlalchemy.sql.default_comparator
import pymysql
import timeit
from email.mime.text import MIMEText
import smtplib
import string
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests
import talib
import talib.stream
import yfinance
import pandas

stock = "AAPL"
tday = datetime.today()
startDay = tday - timedelta(days=365)        
df = yfinance.download(stock,start=startDay,end=tday) 

# print(df.iloc[-1:])
# exit()

# # EMA - Exponential Moving Average
# ema5 = talib.EMA(df["Close"], timeperiod=5)#
# print(f"EMA5: {ema5.iloc[-1:]}")

# STOCH - Stochastic, STOCHF - Stochastic Fast
slowk, slowd = talib.STOCH(df["High"],df["Low"],df["Close"], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
fastk, fastd = talib.STOCHF(df["High"],df["Low"],df["Close"], fastk_period=5, fastd_period=3, fastd_matype=0)
print(f"slowk: {slowk.iloc[-1:]}")
print(f"slowd: {slowd.iloc[-1:]}")
print(f"fastk: {fastk.iloc[-1:]}")
print(f"fastd: {fastd.iloc[-1:]}")