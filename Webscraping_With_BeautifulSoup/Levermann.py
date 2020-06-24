import YahooCrawler
from datetime import datetime, timedelta
from datetime import date
import timeit

stock = "AAPL"
index = "SP500"
#stock = "BAYRY"
#index = "DAX"

start = timeit.default_timer()

#1 - Return On Equity RoE / Eigenkapitalrendite
stat1,stat2 = YahooCrawler.read_yahoo_statistics(stock)
roe = float(stat1["Return on Equity (ttm)"].replace("%",""))
marketcap = stat2["Market Cap (intraday)"]
shares_outstanding = stat1["Shares Outstanding"]

hist_price_stock = YahooCrawler.read_yahoo_histprice(stock)
hist_price_index = YahooCrawler.read_yahoo_histprice(index)

#2 - EBIT-Margin / EBIT Marge
insstat = YahooCrawler.read_yahoo_income_statement(stock)
ebit = insstat["EBIT"][0]
revenue = insstat["Total Revenue"][0]
ebit_marge = round(ebit / revenue * 100,2)

#13 - Profit Growth / Gewinnwachstum
net_income = insstat["Net Income"]
i = len(net_income)-1
growth_sum = growth_count = 0
while i > 0:
    if net_income[i] != "-" and net_income[i-1] != "-":
        growth = (net_income[i-1] - net_income[i]) / net_income[i]
        growth_sum += growth
        growth_count += 1
        i -= 1
growth_hist = round(growth_sum / growth_count * 100,2)
#DEBUG INFO
#print(growth_sum)
#print(growth_count)

#5 - P/E-Ratio History 5Y / KGV Historisch 5J
count = eps_hist = 0
for idx,cont in enumerate(net_income):
    if cont == "-": continue
    elif insstat["Breakdown"][idx] == "ttm": continue
    else:
        dt1 = datetime.strptime(insstat["Breakdown"][idx],"%m/%d/%Y")
        dt2 = datetime.strftime(dt1, "%Y-%m-%d")
        tmp_date, tmp_price = YahooCrawler.read_dayprice(hist_price_stock,dt2,"+")
        #DEBUG-INFO
        #print("Price: ", tmp_price)
        #print("NetIncome: ", cont)
        #print("Shares Outstanding: ", shares_outstanding)
        #print("\n")
        eps_hist += tmp_price / (cont / shares_outstanding)
        count += 1
#DEBUG-INFO
#print("EPS-Hist-Summe: ", eps_hist)
#print("EPS-Hist-Count: ", count)
#print(pe_ratio_hist)
pe_ratio_hist = round(eps_hist / count,2)

#3 - Equity Ratio / Eigenkaptialquote
bal_sheet = YahooCrawler.read_yahoo_balance_sheet(stock)
equity = bal_sheet["Stockholders' Equity"][0]
total_assets = bal_sheet["Total Assets"][0]
eq_ratio = round(equity / total_assets * 100,2)

#4 - P/E-Ratio Actual / KGV Aktuell
summary = YahooCrawler.read_yahoo_summary(stock)
pe_ratio = float(summary["pe_ratio"])

#6 - Analyst Opinions / Analystenmeinung
analyst_rating = YahooCrawler.read_zacks_rating(stock)

#7 Reaction to quarter numbers / Reaktion auf Quartalszahlen
dates_earnings = YahooCrawler.read_yahoo_earnings_cal(stock)
#DEBUG INFO
#print(dates_earnings)
for key in sorted(dates_earnings.keys(), reverse=True):
    if datetime.strptime(key,"%Y-%m-%d") < datetime.today(): break
last_earn_info_price = YahooCrawler.read_dayprice(hist_price_stock,key,"+")
dt1 = datetime.strptime(last_earn_info_price[0],"%Y-%m-%d") + timedelta (days=1)
dt2 = datetime.strftime (dt1, "%Y-%m-%d")
last_earn_reaction_price = YahooCrawler.read_dayprice(hist_price_index,dt2,"+")

#8 Profit Revision / Gewinnrevision
analysis = YahooCrawler.read_yahoo_analysis(stock)
next_year_est_current = float(analysis["Current Estimate"][3])
next_year_est_90d_ago = float(analysis["90 Days Ago"][3])

#9 Price Change 6month / Kurs Heute vs. Kurs vor 6M
#10 Price Change 12month / Kurs Heute vs. Kurs vo 1J
#11 Price Momentum / Kursmomentum Steigend
#12 Dreimonatsreversal
dt1 = datetime.strftime (datetime.today(), "%Y-%m-%d")
dt2 = datetime.today() - timedelta (days=180)
dt2 = datetime.strftime(dt2, "%Y-%m-%d")
dt3 = datetime.today() - timedelta (days=360)
dt3 = datetime.strftime(dt3, "%Y-%m-%d")
price_today = YahooCrawler.read_dayprice(hist_price_stock,dt1,"-")
price_6m_ago = YahooCrawler.read_dayprice(hist_price_stock,dt2,"+")
price_1y_ago = YahooCrawler.read_dayprice(hist_price_stock,dt3,"+")

stop = timeit.default_timer()

print("\n",stock,"calculated in ",round((stop-start)/60,2),"min")
print("1 - Return on Equity RoE: ",roe)
print("2 - Ebit-Margin: ",ebit_marge)
print("3 - Equity Ratio: ",eq_ratio)
print("4 - P/E-Ratio: ",pe_ratio)
print("5 - P/E-Ratio History: ",pe_ratio_hist)
print("6 - Analyst Opinions: ",analyst_rating)
print("7 - Recation to quarter numbers: ",last_earn_info_price,"=>",last_earn_reaction_price)
print("8 - Profit Revision: ",next_year_est_current,"<=",next_year_est_current)
print("9 - Price Change for 6 month: ",price_today,"=>",price_6m_ago)
print("10 - Price Change for 12 month: ",price_today,"=>",price_1y_ago)
print("11 - Kursmomentum: ")
print("12 - Dreimonatsreversal: ")
print("13 - Profit Growth: ",growth_hist)












