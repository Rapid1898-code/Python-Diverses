import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date
import talib

stock = "AAPL"
stock = "0002.HK"

tday = datetime.today()
startDay = tday - timedelta(days=100)   
# df = pd.DataFrame() # Empty DataFrame
df = yf.download(stock,start=startDay,end=tday)    

startDay2 = tday - timedelta(days=400) 
df2 = yf.download(stock,start=startDay2,end=tday)    
seriesEMA100 = talib.EMA(df2["Close"], timeperiod=100) 

# Load data
# df = pd.read_csv("path/to/symbol.csv", sep=",")
# OR if you have yfinance installed
# df = df.ta.ticker("aapl")

# VWAP requires the DataFrame index to be a DatetimeIndex.
# Replace "datetime" with the appropriate column from your DataFrame
df.set_index(pd.DatetimeIndex(df.index), inplace=True)

# # Calculate Returns and append to the df DataFrame
# df.ta.log_return(cumulative=True, append=True)
# df.ta.percent_return(cumulative=True, append=True)

# print(df["High"])
# print(df)
highSeries = df["High"]
lowSeries = df["Low"]
closeSeries = df["Close"]

# Supertrend
df.ta.supertrend(high=highSeries, low=lowSeries, close=closeSeries, period=7, multiplier=3, append=True)

df["Buy_Signal"] = 0
df["Sell_Signal"] = 0
n = 7 
# # with normal close price
# for i in range(n,len(df)):
#     if closeSeries[i-1] <= df["SUPERT_7_3.0"][i-1] and closeSeries[i] > df["SUPERT_7_3.0"][i]:
#         df["Buy_Signal"][i] = 1
#     if closeSeries[i-1] >= df["SUPERT_7_3.0"][i-1] and closeSeries[i] < df["SUPERT_7_3.0"][i]:
#         df["Sell_Signal"][i] = 1    

# with ema100
for i in range(n,len(df)):
    if seriesEMA100[i-1] <= df["SUPERT_7_3.0"][i-1] and seriesEMA100[i] > df["SUPERT_7_3.0"][i]:
        df["Buy_Signal"][i] = 1
    if seriesEMA100[i-1] >= df["SUPERT_7_3.0"][i-1] and seriesEMA100[i] < df["SUPERT_7_3.0"][i]:
        df["Sell_Signal"][i] = 1   

print(df)

with pd.ExcelWriter("example.xlsx") as writer:		
	df.to_excel(writer, sheet_name="supertrend ema100")		

# writer = pd.ExcelWriter('PythonExport.xlsx')
# df.to_excel(writer,'Sheet5')
# writer.save()

# df.ta.supertrend(high=df["High"], low=df["Low"], close=["Close"], period=7, multiplier=3)

# New Columns with results
# print(df.columns)
# print(df)