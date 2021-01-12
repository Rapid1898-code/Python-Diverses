import flask
from flask import request, jsonify
import YahooCrawler as yc
import RapidTechTools as rtt
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return '''Yahoo Finance Api'''

@app.route('/api/v1/summary', methods=['GET'])
def api_summary():
    # http://127.0.0.1:5000/api/v1/summary?ticker=CAT
    query_parameters = request.args
    ticker = query_parameters.get ('ticker')
    if "ticker" in request.args:
        summary = yc.read_yahoo_summary (ticker, att=3)
        # print(f"DEBUG: {summary}")
        if summary != {}:
            return jsonify (summary)
        else:
            return f"No data found for ticker {ticker}"
    else:
        return "Error: No ticker provided!"

@app.route('/api/v1/profile', methods=['GET'])
def api_profile():
    # http://127.0.0.1:5000/api/v1/profile?ticker=CAT
    query_parameters = request.args
    ticker = query_parameters.get ('ticker')
    if "ticker" in request.args:
        profile = yc.read_yahoo_profile(ticker)
        # print(f"DEBUG: {summary}")
        if profile != {}:
            return jsonify (profile)
        else:
            return f"No data found for ticker {ticker}"
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
        lst_stock_incStat = []
        t = text ("select ticker, ultimo, total_revenue,"  # 0, 1, 2
                  "net_income, diluted_eps, operating_income,"  # 3, 4, 5
                  "diluted_avg_shares, ebit, gross_profit,"  # 6, 7, 8
                  "total_revenue "  # 9
                  "from stock_income_stat where ticker = :w")
        result = conn.execute (t, w=ticker)
        for row in result:
            lstRow = []
            for elem in row: lstRow.append (elem)
            lst_stock_incStat.insert (0, lstRow)
        # for i in lst_stock_incStat: print(i)        # Debug

        if lst_stock_incStat != []:
            return jsonify (lst_stock_incStat)
        else:
            return f"No data found for ticker {ticker}"
    else:
        return "Error: No ticker provided!"








app.run()
