import YahooCrawler
from datetime import datetime, timedelta
from datetime import date

stock = "AAPL"

#stat1,stat2 = YahooCrawler.read_yahoo_statistics(stock)
#roe = float(stat1["Return on Equity (ttm)"].replace("%",""))
#print(roe)

hist_price = YahooCrawler.read_yahoo_histprice(stock)

# insstat = YahooCrawler.read_yahoo_income_statement(stock)
# ebit = float(insstat["EBIT"][0].replace(",",""))
# revenue = float(insstat["Total Revenue"][0].replace(",",""))
# ebit_marge = round(ebit / revenue * 100,2)
# eps_list = insstat["Basic EPS"]
# print(ebit_marge)
# count = eps_hist = 0
# for idx,cont in enumerate(eps_list):
#     if cont == "-": continue
#     else:
#         dt1 = datetime.strptime(insstat["Breakdown"][idx],"%m/%d/%Y")
#         dt2 = datetime.strftime(dt1, "%Y-%m-%d")
#         tmp_date, tmp_price = YahooCrawler.read_dayprice(hist_price,dt2)
#         count += 1
#         #Debug-Info
#         #print("Price: ", float(tmp_price))
#         #print("EPS: ", float(cont)*1000)
#         #print("P/E-Ratio: ", float(tmp_price) / (float(cont)*1000))
#         #print("\n")
#         eps_hist += float(tmp_price) / (float(cont) * 1000)
# pe_ratio_hist = round(eps_hist / count,2)
# print(pe_ratio_hist)

# bal_sheet = YahooCrawler.read_yahoo_balance_sheet(stock)
# equity = float(bal_sheet["Stockholders' Equity"][0].replace(",",""))
# total_assets = float(bal_sheet["Total Assets"][0].replace(",",""))
# eq_ratio = round(equity / total_assets * 100,2)
# print(eq_ratio)

# summary = YahooCrawler.read_yahoo_summary(stock)
# pe_ratio = float(summary["pe_ratio"])
# print(pe_ratio)

#analyst_rating = YahooCrawler.read_zacks_rating(stock)
#print(analyst_rating)

# dates_earnings = YahooCrawler.read_yahoo_earnings_cal(stock)
# print(dates_earnings)
# for key in sorted(dates_earnings.keys(), reverse=True):
#     if datetime.strptime(key,"%Y-%m-%d") < datetime.today(): break
# last_earn_info_price = YahooCrawler.read_dayprice(hist_price,key,"+")
# dt1 = datetime.strptime(key,"%Y-%m-%d") + timedelta (days=1)
# dt2 = datetime.strftime (dt1, "%Y-%m-%d")
# last_earn_reaction_price = YahooCrawler.read_dayprice(hist_price,dt2,"+")
# print(last_earn_info_price)
# print(last_earn_reaction_price)

# analysis = YahooCrawler.read_yahoo_analysis(stock)
# next_year_est_current = float(analysis["Current Estimate"][3])
# next_year_est_90d_ago = float(analysis["90 Days Ago"][3])
# print(next_year_est_current)
# print(next_year_est_90d_ago)

dt1 = datetime.strftime (datetime.today(), "%Y-%m-%d")
dt2 = datetime.today() - timedelta (days=180)
dt2 = datetime.strftime(dt2, "%Y-%m-%d")
dt3 = datetime.today() - timedelta (days=360)
dt3 = datetime.strftime(dt3, "%Y-%m-%d")
price_today = YahooCrawler.read_dayprice(hist_price,dt1,"-")
price_6m_ago = YahooCrawler.read_dayprice(hist_price,dt2,"+")
price_1y_ago = YahooCrawler.read_dayprice(hist_price,dt3,"+")
print(price_today)
print(price_6m_ago)
print(price_1y_ago)




