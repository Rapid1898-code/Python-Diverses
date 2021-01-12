# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/resources/books/all
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/resources/books?author=Connie+Willis
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/resources/books?author=Connie+Willis&published=1993
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/resources/books?published=2010
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/incstat?ticker=FB
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/summary?ticker=CAT
# https://xnujiyxsb1.execute-api.eu-central-1.amazonaws.com/dev/api/v1/profile?ticker=FB


import flask
from flask import request, jsonify
import sqlite3
# import YahooCrawler as yc
# import RapidTechTools as rtt
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
from datetime import date
import calendar
import pycountry
import re

USE_PYCOUNTRY = True

def replace_more (inp_str, list_chars, target_char=""):
    """
    Replace several chars in a string
    :param inp_str: string which should be changed
    :param list_chars: which chars should be changed in list-form
    :param target_char: with which char the list_chars should be replaced - default is ""
    :return: changed string
    """
    for i in list_chars:
        inp_str = inp_str.replace(i,target_char)
    return inp_str

def clean_value(value, dp=".", tcorr=False, out="None"):
    """
    clean value to Float / Int / Char / None
    :param value: value which will be worked on
    :param dp: decimalpüint <.> or <,>
    :param tcorr: thousand corecction - if True numeric value will be multiplicated by 1000 - if False not
    :param out: output value in case of an invalid value
    :return: cleaned value (or error-value "N/A", None, "" defined in out)
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pattern1 = re.compile ("^[a-zA-Z]{3} [0-9]{2}, [0-9]{4}$")
    pattern2 = re.compile ("^[0-9]{4}-[0-9]{2}$")
    pattern3 = re.compile ("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    pattern4 = re.compile ("^[0-9]{1,2}/[0-9]{2}/[0-9]{4}$")
    value = replace_more(str(value).strip(), ["%","+-","+"])

    if pattern1.match(value) != None:
        value = datetime.strftime((datetime.strptime (value,"%b %d, %Y")),"%Y-%m-%d")
        return(value)
    elif pattern2.match(value) != None:
        dt = datetime.strptime (value, "%Y-%m")
        y = dt.year
        m = dt.month
        ultimo = calendar.monthrange (y, m)[1]
        value = datetime.strftime(date(y,m,ultimo), "%Y-%m-%d")
        return(value)
    elif pattern3.match(value) != None: return(value)
    elif pattern4.match (value) != None:
        value = datetime.strftime ((datetime.strptime (value, "%m/%d/%Y")), "%Y-%m-%d")
        return (value)
    elif value in ["N/A","None","nan","-","—","","∞","-∞","Invalid Date","�","undefined"]:
        if out == "None": return(None)
        elif out == "N/A": return("N/A")
    elif ("M" in value or "B" in value or "T" in value or "k" in value) and replace_more(value, [",",".","M","B","T","k","-"]).isdigit():
        if "M" in value: char = "M"
        elif "B" in value: char = "B"
        elif "T" in value: char = "T"
        elif "k" in value: char = "k"
        decimal_place = value.find(dp)
        b_place = value.find(char)
        if decimal_place == -1:
            b_place = 1
            decimal_place = 0
        #OLD: if char in ["M","B","T"]: value = value.replace(".","").replace(",","").replace(char,"")
        if char in ["M", "B", "T"]: value = replace_more(value, [".",",",char])
        # million
        if char == "M":
            for i in range (3 - (b_place - decimal_place - 1)): value = value + "0"
        # billion
        if char == "B":
            for i in range(6 - (b_place - decimal_place -1)): value = value + "0"
        # trillion
        if char == "T":
            for i in range(9 - (b_place - decimal_place -1)): value = value + "0"
        # thousand
        if char == "k":
            value = value.replace("k","")
        value = float(value)
        if tcorr: return (value * 1000)
        else: return (value)
    elif ":" in value: return(value)
    #OLD elif value.replace(",","").replace(".","").replace("-","").isdigit() == True:
    elif replace_more(value, [",",".","-"]).isdigit () == True:
        if dp == ",":
            if "." in value and "," in value: value = value.replace(".","")
            if "," in value: value = float(value.replace(",","."))
            else: value = int(value.replace(".",""))
            if tcorr: return(value * 1000)
            else: return (value)
        elif dp == ".":
            if "," in value and "." in value: value = value.replace(",","")
            if "." in value: value = float(value)
            else: value = int(value.replace(",",""))
            if tcorr: return(value * 1000)
            else: return (value)
        else: print(f"Wrong dp parameter vor {value}")
    else: return(value)

def read_yahoo_summary(stock,out=True,att=10):
    """
    Read summary stock data from yahoo
    :param stock: ticker-symbol which should be read
    :param out: when True then output some status informations during program running
    :param att: number of attempts how often the reading should be repeated in case of problems
    :return: dictionary with line per value
    """
    erg = {}
    link = "https://finance.yahoo.com/quote/" + stock
    if out: print ("Reading summary web data for", stock, "...")
    erg["symbol"] = stock

    attempt = 1
    while attempt < att:
        try:
            page = requests.get (link)
            soup = BeautifulSoup (page.content, "html.parser")
            time.sleep(1)
            table = soup.find ('div', id="quote-header-info")
        except:
            pass
        if table != None: break
        if out: print ("Read attempt name failed... Try", attempt)
        time.sleep (.5 + attempt)
        attempt += 1

    if table == None: return ({})
    else: header = table.find ("h1").text

    erg["name"] = header.strip ()

    erg["currency"] = table.find (["span"]).text.strip()[-3:].upper()
    erg["exchange"] = table.find (["span"]).text.split("-")[0].strip()

    tmp_vol = soup.find('td', attrs={"data-test": "TD_VOLUME-value"})
    if tmp_vol != None: tmp_vol = tmp_vol.text.strip().replace(",","")
    if tmp_vol != "N/A" and tmp_vol != None: erg["vol"] = float (tmp_vol.replace (",", ""))
    else: erg["vol"] = "N/A"

    tmp_avg_vol = soup.find('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"})
    if tmp_avg_vol != None: tmp_avg_vol = tmp_avg_vol.text.strip().replace(",","")
    if tmp_avg_vol != "N/A" and tmp_avg_vol != None: erg["avg_vol"] = float (tmp_avg_vol.replace (",", ""))
    else: erg["avg_vol"] = "N/A"

    # find price and change of day
    sp = table.find_all ("span")
    if sp != None:
        for i_idx, i in enumerate (sp):
            if i.text.replace (",", "").replace (".", "").strip ().isdigit ():
                erg["price"] = clean_value (sp[i_idx].text.strip ())
                change = sp[i_idx + 1].text.strip ()
                daychange_tmp = change.split ("(")
                if daychange_tmp != [""]:
                    erg["daychange_abs"] = clean_value (daychange_tmp[0].strip ())
                    erg["daychange_perc"] = clean_value (daychange_tmp[1][:-1].strip ())
                else:
                    erg["daychange_abs"] = "N/A"
                    erg["daychange_perc"] = "N/A"
                break
    else:
        erg["price"] = "N/A"
        erg["daychange_abs"] = "N/A"
        erg["daychange_perc"] = "N/A"

    d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"})
    if d_r_tmp != None:
        d_r_tmp = d_r_tmp.text.strip ().split ('-')
        erg["day_range_from"] = clean_value(d_r_tmp[0].strip().replace(",",""))
        erg["day_range_to"] = clean_value(d_r_tmp[1].strip().replace(",",""))
    else:
        erg["day_range_from"] = "N/A"
        erg["day_range_to"] = "N/A"

    f_r_tmp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"})
    if f_r_tmp != None and len(f_r_tmp.text.strip()) != 0:
        f_r_tmp = f_r_tmp.text.strip ().split ('-')
        erg["fifty_range_from"] = clean_value(f_r_tmp[0].strip().replace(",",""))
        erg["fifty_range_to"] = clean_value(f_r_tmp[1].strip().replace(",",""))
    else:
        erg["fifty_range_from"] = "N/A"
        erg["fifty_range_to"] = "N/A"

    tmp_marketcap = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"})
    if tmp_marketcap != None: tmp_marketcap = tmp_marketcap.text.strip()
    if tmp_marketcap != "N/A" and tmp_marketcap != None: erg["marketcap"] = clean_value(tmp_marketcap) * 1000
    else: erg["marketcap"] = "N/A"

    tmp_beta = soup.find('td', attrs={"data-test": "BETA_5Y-value"})
    if tmp_beta != None: tmp_beta = tmp_beta.text.strip()
    if tmp_beta not in [None,"N/A"] and len(tmp_beta) < 10: erg["beta"] = clean_value(tmp_beta)
    else: erg["beta"] = None

    tmp_pe_ratio = soup.find ('td', attrs={"data-test": "PE_RATIO-value"})
    if tmp_pe_ratio != None: tmp_pe_ratio = tmp_pe_ratio.text.strip()
    if tmp_pe_ratio != "N/A" and tmp_pe_ratio != None: erg["pe_ratio"] = clean_value(tmp_pe_ratio)
    else: erg["pe_ratio"] = "N/A"

    tmp_eps = soup.find ('td', attrs={"data-test": "EPS_RATIO-value"})
    if tmp_eps != None: erg["eps_ratio"] = clean_value(tmp_eps.text.strip())
    else: erg["eps_ratio"] = "N/A"

    temp_div = soup.find ('td', attrs={"data-test": "DIVIDEND_AND_YIELD-value"})
    if temp_div != None: temp_div = temp_div.text.strip ().split ("(")
    if temp_div == None:
        erg["forw_dividend"] = "N/A"
        erg["div_yield"] = "N/A"
    elif "N/A" in temp_div[0].strip():
        erg["forw_dividend"] = "N/A"
        erg["div_yield"] = "N/A"
    else:
        erg["forw_dividend"] = clean_value(temp_div[0])
        erg["div_yield"] = clean_value(temp_div[1][:-1])

    tmp_oytp = soup.find ('td', attrs={"data-test": "ONE_YEAR_TARGET_PRICE-value"})
    if tmp_oytp != None: tmp_oytp = tmp_oytp.text.strip()
    if tmp_oytp != "N/A" and tmp_oytp != None: erg["price1Yest"] = float (tmp_oytp.replace (",", ""))
    else: erg["price1Yest"] = "N/A"

    tmp_next_ed = soup.find ('td', attrs={"data-test": "EARNINGS_DATE-value"})
    if tmp_next_ed == None: erg["next_earnings_date"] = "N/A"
    else:
        tmp_next_ed = tmp_next_ed.text.strip()
        if len(tmp_next_ed) > 15 and "-" in tmp_next_ed:
            tmp_next_ed = tmp_next_ed.split("-")[0].strip()
        if tmp_next_ed != "N/A":
            erg["next_earnings_date"] = datetime.strftime((datetime.strptime (tmp_next_ed,"%b %d, %Y")),"%Y-%m-%d")

    tmp_ex_dd = soup.find ('td', attrs={"data-test": "EX_DIVIDEND_DATE-value"})
    if tmp_ex_dd == None: erg["last_dividend_date"] = "N/A"
    else:
        tmp_ex_dd = tmp_ex_dd.text.strip()
        if len (tmp_ex_dd) > 15: tmp_ex_dd = "N/A"
        if tmp_ex_dd != "N/A":
            erg["last_dividend_date"] = datetime.strftime((datetime.strptime (tmp_ex_dd,"%b %d, %Y")),"%Y-%m-%d")

    return(erg)

def read_yahoo_profile(stock,out=True):
    """
    Read profile stock data from yahoo
    :param stock: ticker-symbol which should be read
    :param out: when True then output some status informations during program running
    :return: dictionary with line per value
    """
    erg = {}
    if out: print("Reading profile web data for",stock,"...")
    link = "https://finance.yahoo.com/quote/" + stock + "/profile?p=" + stock
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")
    time.sleep (0.5)
    erg["symbol"] = stock

    table = soup.find ('div', attrs={"class": "asset-profile-container"})
    if table == None:
        return ({})
    else:
        spans = table.find_all ("span")
    if len(spans[5].text.strip()) == 0:
        erg["empl"] = "N/A"
    else:
        erg["empl"] = int(spans[5].text.strip ().replace (",", ""))
    erg["sector"] = spans[1].text.strip ()
    erg["industry"] = spans[3].text.strip ()

    ps = table.find_all("a")

    erg["tel"] = ps[0].text
    erg["url"] = ps[1].text
    if "." in ps[1].text:
        if USE_PYCOUNTRY:
            land = ps[1].text.split(".")[-1].upper()
            if land == "COM":
                erg["country"] = "USA"
            else:
                country = pycountry.countries.get (alpha_2=land)
                if country != None:
                    erg["country"] = country.name
                else:
                    erg["country"] = "N/A"
        else:
            erg["country"] = "N/A"
    else: erg["country"] = "N/A"

    table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
    if table == None: erg["desc"] = "N/A"
    else: erg["desc"] = table.find ("p").text.strip ()

    return(erg)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''Distant Reading Archive: A prototype API for distant reading of science fiction novels.'''

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    # print(f"DEBUG: Allbooks {all_books}")
    # print(f"DEBUG: {len(all_books)}")
    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(e):
    return "404. The resource could not be found.", 404

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)

    query = query[:-4] + ';'

    print(f"DEBUG: Query: {query}")
    print(f"DEBUG to_filter: {to_filter}")

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

@app.route('/api/v1/summary', methods=['GET'])
def api_summary():
    # http://127.0.0.1:5000/api/v1/summary?ticker=CAT
    query_parameters = request.args
    ticker = query_parameters.get ('ticker')
    if "ticker" in request.args:
        summary = read_yahoo_summary(ticker, att=3)
        # print(f"DEBUG: {summary}")
        if summary != {}:
            return jsonify (summary)
        else:
            return f"No summary data found for ticker {ticker}"
    else:
        return "Error: No ticker provided!"

@app.route('/api/v1/profile', methods=['GET'])
def api_profile():
    # http://127.0.0.1:5000/api/v1/profile?ticker=CAT
    query_parameters = request.args
    ticker = query_parameters.get ('ticker')
    if "ticker" in request.args:
        profile = read_yahoo_profile(ticker)
        print(f"DEBUG: {profile}")
        print(f"DEBUG: {type(profile)}")
        if profile != {}:
            return jsonify (profile)
        else:
            return f"No profile data found for ticker {ticker}"
    else:
        return "Error: No ticker provided!"

@app.route ('/api/v1/incstat', methods=['GET'])
def api_incStat():
    # http://127.0.0.1:5000/api/v1/incstat?ticker=FB

    # local db with maria-db
    #engine = create_engine ("mysql+pymysql://root:I65faue#MB7#@localhost/stockdb?host=localhost?port=3306")
    # hosted db on a2hosting with read permission only
    engine = create_engine ("mysql+pymysql://rapidtec_Reader:I65faue#RR6#@nl1-ss18.a2hosting.com/rapidtec_stockdb")
    conn = engine.connect ()

    query_parameters = request.args
    ticker = query_parameters.get ('ticker')
    if "ticker" in request.args:
        # Read data from stock_income_stat for ticker
        # print("Read data from stock income statement...")
        lstStockIncStat = []
        t = text ("select ticker, ultimo, total_revenue,"  # 0, 1, 2
                  "net_income, diluted_eps, operating_income,"  # 3, 4, 5
                  "diluted_avg_shares, ebit, gross_profit,"  # 6, 7, 8
                  "total_revenue "  # 9
                  "from stock_income_stat where ticker = :w")
        result = conn.execute (t, w=ticker)
        titles = ["ticker", "ultimo", "total_revenue", "net_income", "diluted_eps", "operating_income",
                  "diluted_avg_shares", "ebit", "gross_profit", "total_revenue"]
        for row in result:
            lstRow = {}
            for idx, elem in enumerate(row): lstRow[titles[idx]] = elem
            lstStockIncStat.insert (0, lstRow)
        # for i in lstStockIncStat: print(f"DEBUG: {i}")

        if lstStockIncStat != []:
            return jsonify (lstStockIncStat)
        else:
            return f"No data found for ticker {ticker}"
    else:
        return "Error: No ticker provided!"

# We only need this for local development.
if __name__ == '__main__':
 app.run()
