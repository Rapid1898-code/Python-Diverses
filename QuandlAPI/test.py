# Docu: https://www.quandl.com/databases/SF1/documentation
# Time Dimensions: https://www.quandl.com/databases/SF1/documentation?anchor=dimensions
# Data Organization: https://docs.quandl.com/docs/data-organization
import quandl
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) 
QUANDL_TSTAPI = os.environ.get("QUANDL_TSTAPI")
quandl.ApiConfig.api_key=QUANDL_TSTAPI

erg = quandl.get_table('SHARADAR/SF1', ticker='AAPL')
events = quandl.get_table('SHARADAR/EVENTS', ticker='AAPL')
meta = quandl.get_table('SHARADAR/TICKERS', table='SF1', ticker='AAPL')
indicator = quandl.get_table('SHARADAR/INDICATORS', table='SF1')
daily = quandl.get_table('SHARADAR/DAILY', ticker='AAPL')
actions = quandl.get_table('SHARADAR/ACTIONS', ticker='AAPL')
prices = quandl.get('WIKI/AAPL')

# print(erg)
# print(erg.columns)
# print(events)
# print(events.columns)
# print(meta)
# print(meta.columns)
# print(indicator)
# print(indicator.columns)
# print(daily)
# print(daily.columns)
# print(actions)
# print(actions.columns)
print(prices)
print(prices.columns)


