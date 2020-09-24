import yfinance as yf
import pandas as pd

ticker = yf.Ticker("AAPL")
#ticker = yf.Ticker("BAS.DE")
#ticker = yf.Ticker('BAYN.DE')
#ticker = yf.Ticker("MSFT")

#print(ticker.info)

#info = ticker.info
#hist = ticker.history(period="max")
hist = ticker.history(period="5d")
#action = ticker.actions
#dividends = ticker.dividends
#splits = ticker.splits
#fin = ticker.cashflow
#msft = yf.Ticker("MSFT")

#for key,val in ticker.info.items(): print(key,val)
#for key,val in ticker.history(period="max").items(): print(key,val)

#for key in hist.keys(): print(key)
#print(hist["Close"])
#print(hist.loc[["2020-07-20"],["Close"]])
#print(hist.loc["2020-07-20"]["Close"])
#print(type(hist.loc["2020-07-20"]["Close"]))
#print(type(hist))
#print(hist.loc[["2020-07-22","2020-07-20"], :])

#print(hist)
#print(hist.head(3))
#print(hist.loc["2020-07-20"])
#rint(hist.loc["2020-07-20":"2020-07-22"])

#print(info)
#for key in info.keys(): print(key)
#for val in info.values(): print(val)
#print(hist)
#print(hist.info())
#print(action)
#print(action.info())
#print(dividends)
#print(splits)
#print(msft.cashflow)

#bayn = ticker.history(period='max')
#print(bayn)

#print(hist)
#for i in ["2020-07-20","2020-07-22"]: print(hist.loc[i]["Open"])
#print(hist["Open"])
print(hist.loc[[0:1],:])



