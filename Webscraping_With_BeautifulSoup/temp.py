import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options
from sys import platform
import os
from selenium import webdriver

def is_na(value):
    if "N/A" in value: return "N/A"
    else:
        try:
            return (float(value))
        except ValueError:
            return (value)

#stock = "UG.PA"
#stock = "AAPL"
#stock = "DLR"
stock = "SIX"

while True:

    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock
    print ("Reading summary web data for", stock, "...")

    #options = Options()
    #options.add_argument('--headless')
    #if platform == "win32": driver = webdriver.Chrome (os.getcwd () + '/chromedriver.exe', options=options)
    #elif platform =="linux": driver = webdriver.Chrome (os.getcwd () + '/chromedriver', options=options)
    #driver.get(link)                                               # Read link
    #time.sleep(2)
    #soup = BeautifulSoup (driver.page_source, 'html.parser')
    #driver.quit ()

    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")

    #print(soup.prettify())

    #time.sleep (0.5)

    erg["symbol"] = stock
    erg["name"] = soup.find("h1").text.split ("-")[1].strip ()
    erg["vol"] = int (soup.find ('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip ().replace (",", ""))
    erg["avg_vol"] = int (
        soup.find ('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip ().replace (",", ""))
    erg["price"] = float (soup.find ('span', attrs={"data-reactid": "14"}).text.strip ().replace (",", ""))
    daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
    erg["daychange_abs"] = float (daychange_tmp[0])
    erg["daychange_perc"] = float (
        daychange_tmp[1].strip ().replace (")", "").replace ("+", "").replace ("-", "").replace ("%", ""))
    d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
    erg["day_range_from"] = float (d_r_tmp[0].strip ().replace (",", ""))
    erg["day_range_to"] = float (d_r_tmp[1].strip ().replace (",", ""))
    f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
    erg["fifty_range_from"] = float (f_r_temp[0].strip ().replace (",", ""))
    erg["fifty_range_to"] = float (f_r_temp[1].strip ().replace (",", ""))
    erg["marketcap"] = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
    erg["beta"] = is_na (soup.find ('td', attrs={"data-test": "BETA_5Y-value"}).text.strip ())
    if "N/A" in soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ():
        erg["pe_ratio"] = "N/A"
    else:
        erg["pe_ratio"] = float (soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ())
    erg["eps_ratio"] = is_na (soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ())
    div_temp = soup.find ('td', attrs={"data-test": "DIVIDEND_AND_YIELD-value"}).text.strip ().split ("(")
    if "N/A" in div_temp[0].strip ():
        erg["forw_dividend"] = "N/A"
        erg["div_yield"] = "N/A"
    else:
        erg["forw_dividend"] = float (div_temp[0].strip ())
        erg["div_yield"] = float (div_temp[1].replace ("%", "").replace (")", ""))
    if "N/A" in soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip ():
        erg["price1Yest"] = "N/A"
    else:
        erg["price1Yest"] = float (
            soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip ().replace (",", ""))

    #for key,val in erg.items(): print(key,val)
    print(erg)
