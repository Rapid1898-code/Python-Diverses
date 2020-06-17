import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

def is_na(value):
    if "N/A" in value: return "N/A"
    else: return value

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
    if "N/A" in soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ():
        erg["pe_ratio"] = "N/A"
    else:
        erg["pe_ratio"] = float(soup.find ('td', attrs={"data-test": "PE_RATIO-value"}).text.strip ())
    erg["eps_ratio"] = float(soup.find ('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip ())
    div_temp = soup.find ('td', attrs={"data-test": "DIVIDEND_AND_YIELD-value"}).text.strip ().split ("(")
    if "N/A" in div_temp[0].strip():
        erg["forw_dividend"] = "N/A"
        erg["div_yield"] = "N/A"
    else:
        erg["forw_dividend"] = float (div_temp[0].strip ())
        erg["div_yield"] = float (div_temp[1].replace ("%", "").replace (")", ""))
    if "N/A" in soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip():
        erg["price1Yest"] = "N/A"
    else:
        erg["price1Yest"] = float (soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text.strip().replace(",",""))

    return(erg)

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

def read_yahoo_statistics(stock):
# Read statistics stock data from yahoo
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/key-statistics?p=" + stock
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")
    erg["symbol"] = stock

    erg["fiscal_year_ends"] = is_na(soup.find('td', attrs={'data-reactid': '320'}).text.strip())
    erg["recent_quarter"] = is_na(soup.find('td', attrs={"data-reactid": "327"}).text.strip())
    erg["profit_margin"] = is_na(soup.find('td', attrs={"data-reactid": "341"}).text.strip())
    erg["operating_margin"] = is_na(soup.find('td', attrs={"data-reactid": "348"}).text.strip())
    erg["ROA"] = is_na(soup.find('td', attrs={"data-reactid": "362"}).text.strip())
    erg["ROE"] = is_na(soup.find('td', attrs={"data-reactid": "369"}).text.strip())
    erg["revenue"] = is_na(soup.find('td', attrs={"data-reactid": "383"}).text.strip())
    erg["revenue_per_share"] = is_na(soup.find('td', attrs={"data-reactid": "390"}).text.strip())
    erg["quart_rev_growth"] = is_na(soup.find('td', attrs={"data-reactid": "397"}).text.strip())
    erg["gross_profit"] = is_na(soup.find ('td', attrs={"data-reactid": "404"}).text.strip ())
    erg["EBITDA"] = is_na(soup.find ('td', attrs={"data-reactid": "411"}).text.strip ())
    erg["netincome"] = is_na(soup.find ('td', attrs={"data-reactid": "418"}).text.strip ())
    erg["dil_eps"] = is_na(soup.find ('td', attrs={"data-reactid": "425"}).text.strip ())#
    erg["quart_earnings_growth"] = is_na(soup.find ('td', attrs={"data-reactid": "432"}).text.strip ())
    erg["total_cash"] = is_na(soup.find ('td', attrs={"data-reactid": "448"}).text.strip ())
    erg["total_cash_per_share"] = is_na(soup.find ('td', attrs={"data-reactid": "453"}).text.strip ())
    erg["total_debt"] = is_na(soup.find ('td', attrs={"data-reactid": "460"}).text.strip ())
    erg["total_debt_equity"] = is_na(soup.find ('td', attrs={"data-reactid": "467"}).text.strip ())
    erg["current_ratio"] = is_na (soup.find ('td', attrs={"data-reactid": "474"}).text.strip ())
    erg["book_value_per_share"] = is_na (soup.find ('td', attrs={"data-reactid": "481"}).text.strip ())
    erg["oper_cashflow"] = is_na (soup.find ('td', attrs={"data-reactid": "495"}).text.strip ())
    erg["free_cashflow"] = is_na (soup.find ('td', attrs={"data-reactid": "502"}).text.strip ())
    erg["52w_change"] = is_na (soup.find ('td', attrs={"data-reactid": "106"}).text.strip ())
    erg["52w_change"] = is_na (soup.find ('td', attrs={"data-reactid": "106"}).text.strip ())
    erg["50d_ma"] = is_na (soup.find ('td', attrs={"data-reactid": "134"}).text.strip ())
    erg["200d_ma"] = is_na (soup.find ('td', attrs={"data-reactid": "141"}).text.strip ())
    erg["avg_vol_3m"] = is_na (soup.find ('td', attrs={"data-reactid": "155"}).text.strip ())
    erg["avg_vol_10d"] = is_na (soup.find ('td', attrs={"data-reactid": "162"}).text.strip ())
    erg["shares_outstanding"] = is_na (soup.find ('td', attrs={"data-reactid": "169"}).text.strip ())
    erg["float"] = is_na (soup.find ('td', attrs={"data-reactid": "176"}).text.strip ())
    erg["held_insiders"] = is_na (soup.find ('td', attrs={"data-reactid": "183"}).text.strip ())
    erg["held_institutions"] = is_na (soup.find ('td', attrs={"data-reactid": "190"}).text.strip ())
    erg["shares_short"] = is_na (soup.find ('td', attrs={"data-reactid": "197"}).text.strip ())
    erg["short_rato"] = is_na (soup.find ('td', attrs={"data-reactid": "204"}).text.strip ())
    erg["short_of_float"] = is_na (soup.find ('td', attrs={"data-reactid": "211"}).text.strip ())
    erg["short_of_shares_outstanding"] = is_na (soup.find ('td', attrs={"data-reactid": "218"}).text.strip ())
    erg["shares_short"] = is_na (soup.find ('td', attrs={"data-reactid": "225"}).text.strip ())
    erg["forw_dividend"] = is_na (soup.find ('td', attrs={"data-reactid": "239"}).text.strip ())
    erg["forw_div_yield"] = is_na (soup.find ('td', attrs={"data-reactid": "246"}).text.strip ())
    erg["trailing_dividend"] = is_na (soup.find ('td', attrs={"data-reactid": "253"}).text.strip ())
    erg["trailing_div_yield"] = is_na (soup.find ('td', attrs={"data-reactid": "260"}).text.strip ())
    erg["5y_avg_div_yield"] = is_na (soup.find ('td', attrs={"data-reactid": "267"}).text.strip ())
    erg["payout_ratio"] = is_na (soup.find ('td', attrs={"data-reactid": "274"}).text.strip ())
    erg["dividend_date"] = is_na (soup.find ('td', attrs={"data-reactid": "281"}).text.strip ())
    erg["ex_dividend_date"] = is_na (soup.find ('td', attrs={"data-reactid": "290"}).text.strip ())
    erg["last_split_factor"] = is_na (soup.find ('td', attrs={"data-reactid": "295"}).text.strip ())
    erg["last_split_date"] = is_na (soup.find ('td', attrs={"data-reactid": "302"}).text.strip ())


    return (erg)

def read_yahoo_statistics_valuation(stock):
# Read statistics valuation stock data from yahoo
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/key-statistics?p=" + stock
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')       # Use chromedriver.exe to read website
    driver.get(link)                                               # Read link
    time.sleep(2)                                                  # Wait till the full site is loaded
    driver.find_element_by_name("agree").click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')        # Read page with html.parser
    time.sleep (2)
    driver.quit ()
    tmp = soup.find('div', attrs={"data-reactid": "51"})

    row = [stock]
    for i in ["64","69","71","73","75","77"]:
        row.append(soup.find('span', attrs={"data-reactid": i}).text.strip())
    erg["title"]=row

    row = [soup.find('span', attrs={"data-reactid": "81"}).text.strip()]
    for i in ["86","87","88","89","90","91"]:
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["marketcap"]=row

    row = [soup.find ('span', attrs={"data-reactid": "94"}).text.strip ()]
    for i in ["99","100","101","102","103","104"]:
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["enterprise_value"] = row

    row = [soup.find ('span', attrs={"data-reactid": "107"}).text.strip ()]
    for i in range(112,118,1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["enterprise_value"] = row

    row = [soup.find ('span', attrs={"data-reactid": "120"}).text.strip ()]
    for i in range (125, 131, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["forward_pe"] = row

    row = [soup.find ('span', attrs={"data-reactid": "133"}).text.strip ()]
    for i in range (138, 144, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["peg_ratio_expected"] = row

    row = [soup.find ('span', attrs={"data-reactid": "146"}).text.strip ()]
    for i in range (151, 157, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["price_sales"] = row

    row = [soup.find ('span', attrs={"data-reactid": "159"}).text.strip ()]
    for i in range (164, 170, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["price_book"] = row

    row = [soup.find ('span', attrs={"data-reactid": "172"}).text.strip ()]
    for i in range (177, 183, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["ev_revenue"] = row

    row = [soup.find ('span', attrs={"data-reactid": "185"}).text.strip ()]
    for i in range (190, 196, 1):
        row.append (soup.find ('td', attrs={"data-reactid": i}).text.strip ())
    erg["ev_ebidta"] = row

    return (erg)

def read_yahoo_income_statement(stock):
# Read income statement stock data from yahoo
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/financials?p=" + stock
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')       # Use chromedriver.exe to read website
    driver.get(link)                                               # Read link
    time.sleep(2)                                                  # Wait till the full site is loaded
    driver.find_element_by_name("agree").click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')        # Read page with html.parser
    time.sleep (2)
    driver.quit ()
    div_id = soup.find(id="Col1-1-Financials-Proxy")

    tmp_list = []
    for row in div_id.find_all("span"): tmp_list.append(row.text.strip())
    while tmp_list[0] != "Breakdown": tmp_list.pop(0)
    idx = 0
    while idx<len(tmp_list):
        tmp_list[idx] = tmp_list[idx].lower().replace(" ","_")
        check_missing = True
        tmp_row = tmp_list[idx+1:idx+6]
        diff_tmp = 0
        while True:
            if tmp_row == []: break
            if tmp_row[0] == "ttm": break
            shift=False
            for tr_idx,tr_cont in enumerate(tmp_row):
                if tr_cont[0].isalpha():
                    tmp_row.insert(0,"-")
                    tmp_row.pop()
                    diff_tmp += 1
                    shift=True
            if shift == False: break
        erg[tmp_list[idx]] = tmp_row
        idx = idx + 6 - diff_tmp

    del_list = []
    # format alle float-content of the dict
    for key,val in erg.items():
        if val == []: del_list.append(key)
        for val_i, val_cont in enumerate(val):
            if val_cont.replace(",","").replace("-","").isdigit():
                val[val_i] = float(val_cont.replace(",",""))
        erg[key] = val
    # delete entries with empty content
    for i in del_list: del erg[i]

    return (erg)






stock = "AAPL"
#erg = read_yahoo_summary(stock)
#erg2 = read_yahoo_profile(stock)
#erg3 = read_yahoo_statistics(stock)
#erg4 = read_yahoo_statistics_valuation(stock)
erg5 = read_yahoo_income_statement(stock)

#print(erg,"\n")
#print(erg2,"\n")
#print(erg3,"\n")
#print(erg4,"\n")
print(erg5,"\n")

# for key, val in erg.items():
#     print(key,":",val)
#     print(type(val))
# for key, val in erg2.items():
#     print(key,":",val)
#     print(type(val))
#for key,val in erg5.items():
#    print(key,val)
