import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date

stock = "aapl"

tday = datetime.today()
startDay = tday - timedelta(days=100)   
df = pd.DataFrame() # Empty DataFrame
df = yf.download(stock,start=startDay,end=tday)    

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
print(df)

# Supertrend
df.ta.supertrend(high=df["High"], low=df["Low"], close=["Close"], period=7, multiplier=3)


# df.ta.supertrend(high=df["High"], low=df["Low"], close=["Close"], period=7, multiplier=3)

# New Columns with results
# print(df.columns)
# print(df)

# Take a peek
df.tail()