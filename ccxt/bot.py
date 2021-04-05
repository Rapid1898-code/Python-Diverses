import ccxt

# print(ccxt.exchanges)

exchange = ccxt.coinmarketcap()
# markets = exchange.load_markets()
currencies = exchange.fetch_currencies()
print(currencies)



# const exchangeId = 'binance'
#     , exchangeClass = ccxt[exchangeId]
#     , exchange = new exchangeClass ({
#         'apiKey': 'YOUR_API_KEY',
#         'secret': 'YOUR_SECRET',
#         'timeout': 30000,
#         'enableRateLimit': true,
#     })