import yfinance as yf
from datetime import datetime, timedelta
from datetime import date

ticker = "AAPL"
ticker = "CAT"
ticker = "1010.SR"
# ticker = "BTC-USD"

dataYF = yf.Ticker(ticker)


# Summary Infos
for key, val in dataYF.info.items ():
    if val not in [False,None]:
        print (f"{key} => {val} {type(val)}")
print(type(dataYF.info))
print(dataYF.info["logo_url"])
print(dataYF.info.get("logo_url","N/A"))



# # Price data
# tday = datetime.today()
# print(yf.download(ticker,"2020-01-01",end=tday))

# # Intraday Price data
# print(dataYF.history(period="1mo",interval="2m"))

# print(dataYF.financials.loc["Net Income",].iloc[0])

# print(dataYF.financials)
# print(dataYF.dividends)
# print(dataYF.splits)
# print(dataYF.major_holders)
# print(dataYF.institutional_holders)

# print(dataYF.balance_sheet)
# print(dataYF.cashflow)
# print(dataYF.earnings)
# print(dataYF.sustainability)
# print(dataYF.recommendations)
# print(dataYF.calendar)
# print(dataYF.isin)








# print(dataYF.financials[:,[0]])
