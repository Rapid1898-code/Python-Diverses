import os
import win32com.client as win32
import datetime
from pandas_datareader import data

#working_dir = os.getcwd()
#ExcelApp = win32.Dispatch("Excel-Application")
#ExcelApp.visible = True
#wbStock.SaveAs(os.path.join(working_dir, "Output", "Stock Pull {0}".format(datetime.datetime.now().strftime("%m-%d-%Y"))))

tickers = ["MSFT","TLSA","GOOG","AAPL","DBX","FB","AMZN"]
#live_price_worksheet_Name = "Live Price"

livePrice = data.get_quote_yahoo(tickers)
print(len(livePrice))
print(livePrice)


