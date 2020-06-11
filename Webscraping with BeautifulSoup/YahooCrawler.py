import requests
from bs4 import BeautifulSoup

def yahoo_summary(stock):
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")
    erg["symbol"] = stock

    table = soup.find ('div', id="quote-header-info")
    name = table.find ("h1").text.split ("-")[1].strip ()
    erg["name"] = table.find ("h1").text.split ("-")[1].strip ()

    table = soup.find ('div', id="quote-header")
    erg["vol"] = int(soup.find('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip().replace(",",""))
    erg["avg_vol"] = int(soup.find('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip().replace(",",""))

    table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
    erg["price"] = float(soup.find ('span', attrs={"data-reactid": "14"}).text.strip ())
    daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
    erg["daychange_abs"] = float(daychange_tmp[0])
    erg["daychange_perc"] = float (daychange_tmp[1].strip ().replace (")", "").replace ("+", "").replace ("-", "").replace ("%", ""))
    d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
    erg["day_range_from"] = float(d_r_tmp[0].strip())
    erg["day_range_to"] = float(d_r_tmp[1].strip())
    f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
    erg["fifty_range_from"] = float(f_r_temp[0].strip())
    erg["fifty_range_to"] = float(f_r_temp[1].strip ())
    erg["marketcap"] = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
    erg["beta"] = float (soup.find ('td', attrs={"data-test": "BETA_5Y-value"}).text.strip ())
    erg["pe_ratio"] = float(soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ())
    erg["eps_ratio"] = float(soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ())
    div_temp = soup.find ('td', attrs={"data-test": "DIVIDEND_AND_YIELD-value"}).text.strip ().split ("(")
    erg["forw_dividend"] = float (div_temp[0].strip ())
    erg["div_yield"] = float (div_temp[1].replace ("%", "").replace (")", ""))
    erg["price1Yest"] = float (soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip ())

    return(erg)

stock = "AAPL"
erg = yahoo_summary(stock)
for key, val in erg.items():
    print(key,":",val)
    #print(type(val))
