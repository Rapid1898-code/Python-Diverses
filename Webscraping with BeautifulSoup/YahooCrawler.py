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

def read_yahoo_balance_sheet(stock):
# Read balance_sheet stock data from yahoo
# Overview over the different informations (??? are not displayed on the html-page)
####################################################################################
# Breakdown => Breakdown ['9/29/2019', '9/29/2018', '9/29/2017', '9/29/2016']
# (Total) Assets        => Total Assets ['338,516,000', '365,725,000', '375,319,000', '321,686,000']
#   => = Total liabilities and stockholderes equity
# Total Current Assets / Current Assets    => Current Assets ['162,819,000', '131,339,000', '128,645,000', '106,869,000']
# Total Cash / Cash     => Cash, Cash Equivalents & Short Term Investments ['100,557,000', '66,301,000', '74,181,000', '67,155,000']
# Cash And Cash Equivalents     => Cash And Cash Equivalents ['48,844,000', '25,913,000', '20,289,000', '20,484,000']
# ???               => Cash ['12,204,000', '11,575,000', '7,982,000', '8,601,000']
# ???               => Cash Equivalents ['36,640,000', '14,338,000', '12,307,000', '11,883,000']
# Other Short Term Investments      => Other Short Term Investments ['51,713,000', '40,388,000', '53,892,000', '46,671,000']
# ???               => Receivables ['45,804,000', '48,995,000', '35,673,000', '29,299,000']
# Net receivable    => Accounts receivable ['22,926,000', '23,186,000', '17,874,000', '15,754,000']
# ???               => Gross Accounts Receivable ['-', '-', '17,932,000', '15,807,000']
# ???               => Allowance For Doubtful Accounts Receivable ['-', '-', '-58,000', '-53,000']
# ???               => Other Receivables ['22,878,000', '25,809,000', '17,799,000', '13,545,000']
# Inventory         => Inventory ['4,106,000', '3,956,000', '4,855,000', '2,132,000']
# Other Current Assets      => Other Current Assets ['12,352,000', '12,087,000', '13,936,000', '8,283,000']
# (Total) Non-current assets        => Total non-current assets ['175,697,000', '234,386,000', '246,674,000', '214,817,000']
# (Net) Property, plant, equipment        => Net PPE ['37,378,000', '41,304,000', '33,783,000', '27,010,000']
# Gross Property, plant, equipment          => Gross PPE ['95,957,000', '90,403,000', '75,076,000', '61,245,000']
# ???               => Properties ['0', '0', '0', '0']
# ???               => Land And Improvements ['17,085,000', '16,216,000', '13,587,000', '10,185,000']
# ???               => Machinery Furniture Equipment ['69,797,000', '65,982,000', '54,210,000', '44,543,000']
# ???               => Leases ['9,075,000', '8,205,000', '7,279,000', '6,517,000']
# Accumulated Depreciation      => Accumulated Depreciation ['-58,579,000', '-49,099,000', '-41,293,000', '-34,235,000']
# ???               => Goodwill And Other Intangible Assets ['-', '-', '8,015,000', '8,620,000']
# Goodwill          => Goodwill ['-', '-', '5,717,000', '5,414,000']
# Intabgible Assets         => Other Intangible Assets ['-', '-', '2,298,000', '3,206,000']
# Equity and other investments      => Investments And Advances ['105,341,000', '170,799,000', '194,714,000', '170,430,000']
# Equity and other investments      => Investment in Financial Assets ['105,341,000', '170,799,000', '194,714,000', '170,430,000']
# Equity and other investments      => Available for Sale Securities ['105,341,000', '170,799,000', '194,714,000', '170,430,000']
# Other long-term assets        => Other Non Current Assets ['32,978,000', '22,283,000', '10,162,000', '8,757,000']
# (Total) Liabilities           => Total Liabilities Net Minority Interest ['248,028,000', '258,578,000', '241,272,000', '193,437,000']
# (Total) Current Liabilities      => Current Liabilities ['105,718,000', '116,866,000', '100,814,000', '79,006,000']
# ???               => Payables And Accrued Expenses ['46,236,000', '55,888,000', '74,793,000', '59,321,000']
# ???               => Payables ['46,236,000', '55,888,000', '49,049,000', '37,294,000']
# Accounts Payable          => Accounts Payable ['46,236,000', '55,888,000', '49,049,000', '37,294,000']
# Accrued Liabilities           => Current Accrued Expenses ['-', '-', '25,744,000', '22,027,000']
# ???               => Current Debt And Capital Lease Obligation ['16,240,000', '20,748,000', '18,473,000', '11,605,000']
# Current Debt          => Current Debt ['16,240,000', '20,748,000', '18,473,000', '11,605,000']
# ???               => Commercial Paper ['5,980,000', '11,964,000', '11,977,000', '8,105,000']
# ???               => Other Current Borrowings ['10,260,000', '8,784,000', '6,496,000', '3,500,000']
# Deffered revenues             => Current Deferred Liabilities ['5,522,000', '7,543,000', '7,548,000', '8,080,000']
# Deffered revenues             => Current Deferred Revenue ['5,522,000', '7,543,000', '7,548,000', '8,080,000']
# Other Current Liabilities         => Other Current Liabilities ['37,720,000', '32,687,000', '-', '-']
# ???           => Long Term Debt And Capital Lease Obligation ['91,807,000', '93,735,000', '97,207,000', '75,427,000']
# Long Term Debt            => Long Term Debt ['91,807,000', '93,735,000', '97,207,000', '75,427,000']
# ???           => Non Current Deferred Liabilities ['-', '3,223,000', '34,340,000', '28,949,000']
# Deferred Tabex Liabilities        => Non Current Deferred Taxes Liabilities ['-', '426,000', '31,504,000', '26,019,000']
# Deferred revenues         => Non Current Deferred Revenue ['-', '2,797,000', '2,836,000', '2,930,000']
# ???           => Tradeand Other Payables Non Current ['29,545,000', '33,589,000', '-', '-']
# Other Non Current Liabilities         => Other Non Current Liabilities ['20,958,000', '11,165,000', '8,911,000', '10,055,000']
# ???           => Total Equity Gross Minority Interest ['90,488,000', '107,147,000', '134,047,000', '128,249,000']
# (Total) Stockholder Equity        => Stockholders' Equity ['90,488,000', '107,147,000', '134,047,000', '128,249,000']
# ???           => Capital Stock ['45,174,000', '40,201,000', '35,867,000', '31,251,000']
# Common Stock      => Common Stock ['45,174,000', '40,201,000', '35,867,000', '31,251,000']
# Retained Earnings         => Retained Earnings ['45,898,000', '70,400,000', '98,330,000', '96,364,000']
# Gains Losses Not Affecting Retained Earnings ['-584,000', '-3,454,000', '-150,000', '634,000']
# ???           => Total Capitalization ['182,295,000', '200,882,000', '231,254,000', '203,676,000']
# ???           => Common Stock Equity ['90,488,000', '107,147,000', '134,047,000', '128,249,000']
# ???           => Net Tangible Assets ['90,488,000', '107,147,000', '126,032,000', '119,629,000']
# ???           => Working Capital ['57,101,000', '14,473,000', '27,831,000', '27,863,000']
# ???           => Invested Capital ['198,535,000', '221,630,000', '249,727,000', '215,281,000']
# ???           => Tangible Book Value ['90,488,000', '107,147,000', '126,032,000', '119,629,000']
# ???           => Total Debt ['108,047,000', '114,483,000', '115,680,000', '87,032,000']
# ???           => Net Debt ['59,203,000', '88,570,000', '95,391,000', '66,548,000']
# ???           => Share Issued ['4,443,236', '4,754,986', '5,126,201', '5,336,166']
# ???           => Ordinary Shares Number ['4,443,236', '4,754,986', '5,126,201', '5,336,166']

    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/balance-sheet?p=" + stock

    driver = webdriver.Chrome (os.getcwd () + '/chromedriver')
    driver.get (link)
    time.sleep (2)
    driver.find_element_by_name ("agree").click ()
    time.sleep (2)
    driver.find_element_by_xpath ('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span').click ()
    time.sleep (2)
    soup = BeautifulSoup (driver.page_source, 'html.parser')
    time.sleep (2)
    driver.quit ()
    table = soup.find (id="Col1-1-Financials-Proxy")

    list_div = []
    for e in table.find_all (["div"]): list_div.append (e.text.strip ())
    while list_div[0] != "Breakdown": list_div.pop (0)
    for i in range (len (list_div) - 1, 0, -1):
        if list_div[i].replace (",", "").replace ("-", "").isdigit () or list_div[i] == "-": continue
        elif i == len (list_div) - 1: del list_div[i]
        elif len (list_div[i]) == 0: del list_div[i]
        elif len (list_div[i]) > 50: del list_div[i]
        elif i == 0: break
        elif list_div[i] == list_div[i - 1]: del list_div[i]
        elif list_div[i + 1] in list_div[i]: del list_div[i]
    idx = 0
    while idx < len (list_div):
        if list_div[idx].replace (",", "").replace ("-", "").isdigit () == False and list_div[idx] != "-":
            idx += 5
        else:
            while list_div[idx].replace (",", "").replace ("-", "").isdigit () == True or list_div[idx] == "-":
                del list_div[idx]
    idx = 0
    while idx < len (list_div):
        erg[list_div[idx]] = list_div[idx + 1:idx + 5]
        idx += 5

    return (erg)

def read_yahoo_analysis(stock):
# Read analysis stock data from yahoo
# Earnings Estimate ['Current Qtr. (Jun 2020)', 'Next Qtr. (Sep 2020)', 'Current Year (2020)', 'Next Year (2021)']
# No. of Analysts ['28', '28', '35', '34']
# Avg. Estimate ['51.52B', '62.07B', '263.67B', '296.08B']
# Low Estimate ['42.8B', '50.47B', '252.81B', '261.66B']
# High Estimate ['55.84B', '73.55B', '279.52B', '326.68B']
# Year Ago EPS ['2.18', '3.03', '11.89', '12.39']
# Revenue Estimate ['Current Qtr. (Jun 2020)', 'Next Qtr. (Sep 2020)', 'Current Year (2020)', 'Next Year (2021)']
# Year Ago Sales ['53.81B', '64.04B', '260.17B', '263.67B']
# Sales Growth (year/est) ['-4.30%', '-3.10%', '1.30%', '12.30%']
# Earnings History ['6/29/2019', '9/29/2019', '12/30/2019', '3/30/2020']
# EPS Est. ['2.1', '2.84', '4.55', '2.26']
# EPS Actual ['2.18', '3.03', '4.99', '2.55']
# Difference ['0.08', '0.19', '0.44', '0.29']
# Surprise % ['3.80%', '6.70%', '9.70%', '12.80%']
# EPS Trend ['Current Qtr. (Jun 2020)', 'Next Qtr. (Sep 2020)', 'Current Year (2020)', 'Next Year (2021)']
# Current Estimate ['2', '2.82', '12.39', '14.86']
# 7 Days Ago ['1.99', '2.81', '12.38', '14.86']
# 30 Days Ago ['2', '2.8', '12.32', '14.73']
# 60 Days Ago ['2.06', '2.95', '12.4', '14.85']
# 90 Days Ago ['2.37', '3.23', '13.15', '15.45']
# EPS Revisions ['Current Qtr. (Jun 2020)', 'Next Qtr. (Sep 2020)', 'Current Year (2020)', 'Next Year (2021)']
# Up Last 7 Days ['2', '2', '2', '1']
# Up Last 30 Days ['5', '6', '9', '8']
# Down Last 7 Days ['N/A', 'N/A', 'N/A', 'N/A']
# Down Last 30 Days ['N/A', 'N/A', 'N/A', '2']
# Growth Estimates ['AAPL', 'Industry', 'Sector', 'S&P 500']
# Current Qtr. ['-8.30%', 'N/A', 'N/A', '-0.44']
# Next Qtr. ['-6.90%', 'N/A', 'N/A', '-0.16']
# Current Year ['4.20%', 'N/A', 'N/A', '-0.22']
# Next Year ['19.90%', 'N/A', 'N/A', '0.30']
# Next 5 Years (per annum) ['11.47%', 'N/A', 'N/A', '0.03']
# Past 5 Years (per annum) ['8.42%', 'N/A', 'N/A', 'N/A']
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock + "/analysis?p=" + stock
    driver = webdriver.Chrome (os.getcwd () + '/chromedriver')
    driver.get (link)
    time.sleep (2)
    driver.find_element_by_name ("agree").click ()
    time.sleep (2)
    soup = BeautifulSoup (driver.page_source, 'html.parser')
    time.sleep (2)
    driver.quit ()

    table  = soup.find(id="YDC-Col1")
    erg = {}
    list_table = []
    for e in table.find_all (["th", "td"]): list_table.append (e.text.strip ())
    for i in range (0, len (list_table), 5): erg[list_table[i]] = list_table[i + 1:i + 5]

    return (erg)

stock = "AAPL"
#stock = "AMZN"
#erg = read_yahoo_summary(stock)
#erg2 = read_yahoo_profile(stock)
#erg3 = read_yahoo_statistics(stock)
#erg4 = read_yahoo_statistics_valuation(stock)
#erg5 = read_yahoo_income_statement(stock)
#erg6 = read_yahoo_balance_sheet(stock)
erg8 = read_yahoo_analysis(stock)

#print(erg,"\n")
#print(erg2,"\n")
#print(erg3,"\n")
#print(erg4,"\n")
#print(erg5,"\n")
#print(erg6,"\n")
#print(erg7,"\n")
#print(erg8,"\n")

# for key, val in erg.items():
#     print(key,":",val)
#     print(type(val))
# for key, val in erg2.items():
#     print(key,":",val)
#     print(type(val))
for key,val in erg8.items():
    print(key,val)
