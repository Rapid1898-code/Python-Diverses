 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv, find_dotenv
import os
import requests

load_dotenv(find_dotenv())
COINMARKETCAP_API = os.environ.get("COINMARKETCAP_API")

# get coinmarketcap id map
link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/map"
response = requests.get(link).json()
dataErg = response["data"]

for idx, i in enumerate(dataErg):
    print(i)
    if idx == 10:
        exit()
          
# # get latest data for crypto listings
# link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2&convert=USD"
# response = requests.get(link).json()
# dataErg = response["data"][0]
# for key, val in dataErg.items ():  
#     if key == "quote":
#         for quoteKey, quoteVal in val.items():                              
#             print(quoteKey)
#             for quoteKey2, quoteVal2 in quoteVal.items():                              
#                 print(quoteKey2, quoteVal2)
#     else:        
#         print(key, val)

# # get historical data for crypto listings (specific date)
# link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/historical?date=1587925956&start=1&limit=2&convert=USD"
# response = requests.get(link).json()
# dataErg = response["data"][0]
# for key, val in dataErg.items ():  
#     if key == "quote":
#         for quoteKey, quoteVal in val.items():                              
#             print(quoteKey)
#             for quoteKey2, quoteVal2 in quoteVal.items():                              
#                 print(quoteKey2, quoteVal2)
#     else:        
#         print(key, val)

# # get historical data for crypto listings (specific date)
# link = f"https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/historical?date=1587925956&start=1&limit=2&convert=USD"
# response = requests.get(link).json()
# dataErg = response["data"][0]
# for key, val in dataErg.items ():  
#     if key == "quote":
#         for quoteKey, quoteVal in val.items():                              
#             print(quoteKey)
#             for quoteKey2, quoteVal2 in quoteVal.items():                              
#                 print(quoteKey2, quoteVal2)
#     else:        
#         print(key, val)



# # get latest data for crypto listings
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = {'symbol': ['BTC',], 'convert':'USD'}
# # parameters = {'start':'1', 'limit':'2', 'convert':'USD'}
# headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': COINMARKETCAP_API,}

# session = Session()
# session.headers.update(headers)

# try:
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)

#     print(data)
#     exit()

#     # dataErg = data["data"][0]
#     for key, val in dataErg.items ():  
#         if key == "quote":
#             for quoteKey, quoteVal in val.items():                              
#                 print(quoteKey)
#                 for quoteKey2, quoteVal2 in quoteVal.items():                              
#                     print(quoteKey2, quoteVal2)
#         else:        
#             print(key, val)

# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)


# # get latest data for crypto listings
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
# parameters = {'start':'1', 'limit':'2', 'convert':'USD'}
# headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': COINMARKETCAP_API,}

# session = Session()
# session.headers.update(headers)

# try:
#     response = session.get(url, params=parameters)
#     data = json.loads(response.text)

#     print(data)
#     exit()


#     for key, val in dataErg.items ():  
#         if key == "quote":
#             for quoteKey, quoteVal in val.items():                              
#                 print(quoteKey)
#                 for quoteKey2, quoteVal2 in quoteVal.items():                              
#                     print(quoteKey2, quoteVal2)
#         else:        
#             print(key, val)

# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)