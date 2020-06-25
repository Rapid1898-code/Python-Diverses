import YahooCrawler
from datetime import datetime, timedelta
from datetime import date
import timeit
import calendar

stock = "AAPL"
index = "SP500"
finance_stock = "n"
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

#4 - P/E-Ratio History 5Y / KGV Historisch 5J
net_income = insstat["Net Income"]
count = eps_hist = 0
pe_ratio_hist_list = []
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
        pe_ratio_hist_list.append(round(tmp_price / (cont / shares_outstanding),2))
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

#5 - P/E-Ratio Actual / KGV Aktuell
summary = YahooCrawler.read_yahoo_summary(stock)
pe_ratio = float(summary["pe_ratio"])

#6 - Analyst Opinions / Analystenmeinung
analyst_rating = YahooCrawler.read_zacks_rating(stock)
rating = analyst_rating["Rating"][0]

#7 Reaction to quarter numbers / Reaktion auf Quartalszahlen
dates_earnings = YahooCrawler.read_yahoo_earnings_cal(stock)
#DEBUG INFO
#print(dates_earnings)
for key in sorted(dates_earnings.keys(), reverse=True):
    if datetime.strptime(key,"%Y-%m-%d") < datetime.today(): break
last_earningsinfo = key
stock_price_before = YahooCrawler.read_dayprice(hist_price_stock,key,"+")
dt1 = datetime.strptime(stock_price_before[0],"%Y-%m-%d") + timedelta (days=1)
dt2 = datetime.strftime (dt1, "%Y-%m-%d")
stock_price_after = YahooCrawler.read_dayprice(hist_price_stock,dt2,"+")
index_price_before = YahooCrawler.read_dayprice(hist_price_index,stock_price_before[0],"+")
index_price_after = YahooCrawler.read_dayprice(hist_price_index,dt2,"+")
stock_reaction = ((stock_price_after[1]-stock_price_before[1])/stock_price_before[1])*100
index_reaction = ((index_price_after[1]-index_price_before[1])/index_price_before[1])*100
reaction = round(stock_reaction - index_reaction,2)

#8 Profit Revision / Gewinnrevision
#13 - Profit Growth / Gewinnwachstum
analysis = YahooCrawler.read_yahoo_analysis(stock)
next_year_est_current = float(analysis["Current Estimate"][3])
next_year_est_90d_ago = float(analysis["90 Days Ago"][3])
profit_revision = next_year_est_current - next_year_est_90d_ago
profit_revision = round(((next_year_est_current-next_year_est_90d_ago)/next_year_est_90d_ago)*100,2)
profit_growth_act = float(analysis["Current Estimate"][2])
profit_growth_fut = float(analysis["Current Estimate"][3])
profit_growth = round(((profit_growth_fut - profit_growth_act) / profit_growth_act)*100,2)

#9 Price Change 6month / Kurs Heute vs. Kurs vor 6M
#10 Price Change 12month / Kurs Heute vs. Kurs vo 1J
#11 Price Momentum / Kursmomentum Steigend
dt1 = datetime.strftime (datetime.today(), "%Y-%m-%d")
dt2 = datetime.today() - timedelta (days=180)
dt2 = datetime.strftime(dt2, "%Y-%m-%d")
dt3 = datetime.today() - timedelta (days=360)
dt3 = datetime.strftime(dt3, "%Y-%m-%d")
price_today = YahooCrawler.read_dayprice(hist_price_stock,dt1,"-")
price_6m_ago = YahooCrawler.read_dayprice(hist_price_stock,dt2,"+")
price_1y_ago = YahooCrawler.read_dayprice(hist_price_stock,dt3,"+")
change_price_6m = round(((price_today[1]-price_6m_ago[1]) / price_6m_ago[1])*100,2)
change_price_1y = round(((price_today[1]-price_1y_ago[1]) / price_1y_ago[1])*100,2)

#12 Dreimonatsreversal
dt_today = datetime.today()
m = dt_today.month
y = dt_today.year
d = dt_today.day
dates = []
for i in range(4):
    m -= 1
    if m == 0:
        y -= 1
        m = 12
    ultimo = calendar.monthrange(y,m)[1]
    dates.append(datetime.strftime(date(y,m,ultimo), "%Y-%m-%d"))
stock_price = []
index_price = []
for i in dates:
    pr1 = YahooCrawler.read_dayprice(hist_price_stock, i, "-")
    stock_price.append([pr1[0],round(pr1[1],2)])
    pr2 = YahooCrawler.read_dayprice(hist_price_index, i, "-")
    index_price.append([pr2[0],round(pr2[1],2)])

stock_change = []
index_change = []
for i in range(3,0,-1):
    stock_change.append(round(((stock_price[i][1] - stock_price[i-1][1]) / stock_price[i-1][1])*100,2))
    index_change.append(round(((index_price[i][1] - index_price[i-1][1]) / index_price[i-1][1])*100,2))


stop = timeit.default_timer()

lm_points = 0
lm_score = {}
if roe > 20: lm_score["roe"] = 1
elif roe < 10: lm_score["roe"] = -1
else: lm_score["roe"] = 0
if ebit_marge > 12 and finance_stock.upper() == "N": lm_score["ebit_marge"] = 1
elif ebit_marge < 6 and finance_stock.upper() == "N": lm_score["ebit_marge"] = -1
else: lm_score["ebit_marge"] = 0
if eq_ratio > 25: lm_score["eq_ratio"] = 1
elif eq_ratio < 15: lm_score["eq_ratio"] = -1
else: lm_score["eq_ratio"] = 0
if pe_ratio <12 and pe_ratio > 0: lm_score["pe_ratio"] = 1
elif pe_ratio >16 or pe_ratio <0: lm_score["pe_ratio"] = -1
else: lm_score["pe_ratio"] = 0
if pe_ratio_hist <12 and pe_ratio_hist > 0: lm_score["pe_ratio_hist"] = 1
elif pe_ratio_hist >16 or pe_ratio_hist <0: lm_score["pe_ratio_hist"] = -1
else: lm_score["pe_ratio_hist"] = 0
if rating >= 4: lm_score["rating"] = 1
elif rating <= 2: lm_score["rating"] = -1
else: lm_score["rating"] = 0
if reaction >1: lm_score["reaction"] = 1
elif reaction <-1: lm_score["reaction"] = -1
else: lm_score["reaction"] = 0
if profit_revision >1: lm_score["profit_revision"] = 1
elif profit_revision <-1: lm_score["profit_revision"] = -1
else: lm_score["profit_revision"] = 0
if next_year_est_current >1: lm_score["next_year_est_current"] = 1
elif next_year_est_current <-1: lm_score["next_year_est_current"] = -1
else: lm_score["next_year_est_current"] = 0
if change_price_6m >5: lm_score["change_price_6m"] = 1
elif change_price_6m <-5: lm_score["change_price_6m"] = -1
else: lm_score["change_price_6m"] = 0
if change_price_1y >5: lm_score["change_price_1y"] = 1
elif change_price_1y <-5: lm_score["change_price_1y"] = -1
else: lm_score["change_price_1y"] = 0
if lm_score["change_price_6m"] == 1 and lm_score["change_price_1y"] in [0,-1]:
    lm_score["price_momentum"] = 1
elif lm_score["change_price_6m"] == -1 and lm_score["change_price_1y"] in [0,1]:
    lm_score["price_momentum"] = -1
else: lm_score["price_momentum"] = 0
if stock_change[2]<index_change[2] and stock_change[1]<index_change[1] and stock_change[0]<index_change[0]:
    lm_score["3monatsreversal"] = 1
elif stock_change[2]>index_change[2] and stock_change[1]>index_change[1] and stock_change[0]>index_change[0]:
    lm_score["3monatsreversal"] = -1
else: lm_score["3monatsreversal"] = 0
if profit_growth >5: lm_score["profit_growth"] = 1
elif profit_growth <-5: lm_score["profit_growth"] = -1
else: lm_score["profit_growth"] = 0

lm_sum = 0
for val in lm_score.values(): lm_sum += val

print(stock,"calculated in",round((stop-start)/60,2),"min")
print("Index: ",index," ,MarketCap:",marketcap," ,Finance Stock:")
print("1 - Return on Equity RoE:",roe,"=>",lm_score["roe"])
print("\n2 - Ebit-Margin:",ebit_marge,"=>",lm_score["ebit_marge"])
print("\n3 - Equity Ratio:",eq_ratio,"=>",lm_score["eq_ratio"])
print("\n4 - P/E-Ratio History:",pe_ratio_hist,"=>",lm_score["pe_ratio_hist"])
print("Dates:",insstat["Breakdown"][1:])
print("P/E-Ratio History:",pe_ratio_hist_list)
print("\n5 - P/E-Ratio Actual:",pe_ratio,"=>",lm_score["pe_ratio"])
print("\n6 - Analyst Opinions:",rating,"=>",lm_score["rating"])
print("\n7 - Reaction to quarter numbers:",reaction,"=>",lm_score["reaction"])
print ("Last Earnings Info: ",last_earningsinfo)
print(round(stock_price_before[1],2),"=>",round(stock_price_after[1],2),"=>",round(stock_reaction,2))
print(round(index_price_before[1],2),"=>",round(index_price_after[1],2),"=>",round(index_reaction,2))
print("\n8 - Profit Revision:",round(profit_revision,2),"=>",lm_score["profit_revision"])
print("90Day ago:",next_year_est_90d_ago,"=> Current:",next_year_est_current)
print("\n9 - Price Change for 6 month:",change_price_6m,"=>",lm_score["change_price_6m"])
print("6M ago:",round(price_6m_ago[1],2),"=> Today:",round(price_today[1],2),"=> Change:",change_price_6m)
print("\n10 - Price Change for 12 month:",change_price_1y,"=>",lm_score["change_price_1y"])
print("1Y ago:",round(price_1y_ago[1],2),"=> Today:",round(price_today[1],2),"=> Change:",change_price_1y)
print("\n11 - Kursmomentum:",lm_score["price_momentum"])
print("\n12 - Dreimonatsreversal:",lm_score["3monatsreversal"])
print("Stock Price: ",stock_price)
print("Index Price: ",index_price)
print("Stock Change: ",stock_change)
print("Index Change: ",index_change)
print("\n13 - Profit Growth:",profit_growth,"=>",lm_score["profit_growth"])
print("Estimate Current Year:",profit_growth_act,"=> Estimate Next Year:",profit_growth_fut)
print("\nSumme Levermann-Score:",lm_sum)













