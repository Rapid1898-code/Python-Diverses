import requests_cache
import requests
import yfinance as yf
import pandas
from datetime import datetime, timedelta
from datetime import date

# session = requests_cache.CachedSession('yfinance.cache')
session = requests.Session()
session.headers['User-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

ticker = "AAPL"
# ticker = "1561.HK"
# ticker = "CAT"
# ticker = "1010.SR"
# ticker = "ABNB.VI"
# ticker = "BTC-USD"
# ticker = "%5EGDAXI"
# ticker = "IPV"

# dataYF = yf.Ticker(ticker, session=session)
dataYF = yf.Ticker(ticker)

# Summary Infos
# for key, val in dataYF.info.items ():
#     if val not in [False,None]:
#         print (f"{key} => {val} {type(val)}")

# Price data
# tday = datetime.today()
# print(yf.download(ticker,"2020-01-01",end=tday))
# print(yf.download(ticker,"1980-01-01",end=tday))
# print(yf.download(ticker))

# Intraday Price data
# print(dataYF.history(period="12mo",interval="1h"))

# print(dataYF.financials)
# print(dataYF.dividends)
# print(dataYF.splits)
# print(dataYF.major_holders)
# print(dataYF.institutional_holders)
print(dataYF.balance_sheet)
# tmp = dataYF.balance_sheet.iloc[:,0]
# print(tmp.get("Total Stockholder Equity ","N/A"))
# print(dataYF.balance_sheet.loc["Total Stockholder Equity"][0])

# print(dataYF.cashflow)
# print(dataYF.earnings)
# print(dataYF.sustainability)

# tday = datetime.today()
# fromDT = str((tday - timedelta(days=360)).date())
# tday = str(tday.date())

# dfRecommendations = dataYF.recommendations

# if dfRecommendations is not None:
#     pandas.set_option('display.max_rows', dfRecommendations.shape[0]+1)
#     dfRecommendations = dfRecommendations.loc[fromDT:tday]
#     dfRecommendations = dfRecommendations.reset_index()
#     dfRecommendations = dfRecommendations.sort_values('Date', ascending=False)
#     # print(dfRecommendations)
#     # print(len(dfRecommendations))

#     erg = dfRecommendations.set_index('Date').T.to_dict('list')					
#     # for key, val in erg.items (): print (f"{key} => {val} {type(val)}")

#     listFirms = []
#     # Grades: ["Strong Buy", "Buy", "Hold", "Underperform", "Sell"]
#     listGrades = [0,0,0,0,0]
#     for key, val in erg.items (): 
#         if val[0] not in listFirms:
#             listFirms.append(val[0])
#             if val[1] in ["Strong Buy"]:
#                 listGrades[0] += 1
#             elif val[1] in ["Buy","Market Outperform","Sector Outperform", "Outperform", "Overweight", "Positive"]:
#                 listGrades[1] += 1            
#             elif val[1] in ["Hold","Equal-Weight","In-Line","Market Perform","Neutral","Peer Peform","Perform","Sector Perform","Sector Weight","Mixed"]:
#                 listGrades[2] += 1            
#             elif val[1] in ["Underperform"]:
#                 listGrades[3] += 1            
#             elif val[1] in ["Sell","Underperform","Underperformer","Underweight","Negative","Reduce"]:
#                 listGrades[4] += 1            
#             else:
#                 print(f"Error - wrong Grade Value {val[1]} in dataframe / dictionary...")

#     sumFirms = sum(listGrades)
#     sumGrades = 0
#     for i,e in enumerate(listGrades):
#         sumGrades += e * (i+1)

#     print(f"DEBUG: SumGrade: {sumGrades}")
#     print(f"DEBUG: SumFirms: {sumFirms}")
#     rating = round(sumGrades / sumFirms,1)
#     print(listGrades)
#     print(sumFirms)
#     print(rating)

# else:
#     print("No Rating")

# print(dataYF.calendar)
# print(dataYF.isin)







