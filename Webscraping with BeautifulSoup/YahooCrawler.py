import requests
from bs4 import BeautifulSoup

def read_yahoo_profile(stock):
# Read profile stock data from yahoo
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/profile?p=" + stock
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")
    erg["symbol"] = stock

    tmp_empl = soup.find ('span', attrs={"data-reactid": "30"})
    # there 2 different kinds of site-information - so there are 2 ways
    if tmp_empl != None:
        erg["empl"] = int(tmp_empl.text.strip().replace(",",""))
        sector_tmp = soup.find_all ('span', attrs={"data-reactid": "21"})
        for row in sector_tmp:
            if row.get ("class") != None: erg["sector"] = row.text.strip ()
        industry_tmp = soup.find_all ('span', attrs={"data-reactid": "25"})
        for row in industry_tmp:
            if row.get ("class") != None: erg["industry"] = row.text.strip ()
        erg["desc"] = soup.find ('p', attrs={"data-reactid": "141"}).text.strip ()
    else:
        table = soup.find ('div', attrs={"class": "asset-profile-container"})
        spans = table.find_all ("span")
        erg["empl"] = int(spans[5].text.strip().replace(",",""))
        erg["sector"] = spans[1].text.strip ()
        erg["industry"] = spans[3].text.strip ()
        table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
        erg["desc"] = table.find ("p").text.strip ()

    return(erg)

def read_yahoo_summary(stock):
# Read summary stock data from yahoo
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

    erg["price"] = float(soup.find ('span', attrs={"data-reactid": "14"}).text.strip().replace(",",""))
    daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
    erg["daychange_abs"] = float(daychange_tmp[0])
    erg["daychange_perc"] = float (daychange_tmp[1].strip ().replace (")", "").replace ("+", "").replace ("-", "").replace ("%", ""))
    d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
    erg["day_range_from"] = float(d_r_tmp[0].strip().replace(",",""))
    erg["day_range_to"] = float(d_r_tmp[1].strip().replace(",",""))
    f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
    erg["fifty_range_from"] = float(f_r_temp[0].strip().replace(",",""))
    erg["fifty_range_to"] = float(f_r_temp[1].strip ().replace(",",""))
    erg["marketcap"] = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
    erg["beta"] = float (soup.find ('td', attrs={"data-test": "BETA_5Y-value"}).text.strip ())
    erg["pe_ratio"] = float(soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ())
    erg["eps_ratio"] = float(soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ())
    div_temp = soup.find ('td', attrs={"data-test": "DIVIDEND_AND_YIELD-value"}).text.strip ().split ("(")
    if div_temp[0].strip() == "N/A":
        erg["forw_dividend"] = div_temp[0].strip()
        erg["div_yield"] = div_temp[1].strip()
    else:
        erg["forw_dividend"] = float (div_temp[0].strip ())
        erg["div_yield"] = float (div_temp[1].replace ("%", "").replace (")", ""))
    erg["price1Yest"] = float (soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip().replace(",",""))

    return(erg)

stock = "CAT"
erg = read_yahoo_summary(stock)
erg2 = read_yahoo_profile(stock)

print(erg)
print(erg2)

# for key, val in erg.items():
#     print(key,":",val)
#     print(type(val))
# for key, val in erg2.items():
#     print(key,":",val)
#     print(type(val))
