import pandas as pd
import pandas_ta as ta
import yfinance as yf
from datetime import datetime, timedelta
from datetime import date

# Create a DataFrame so 'ta' can be used.
df = pd.DataFrame()

# Help about this, 'ta', extension
# help(df.ta)


# List of all indicators
# print(df.ta.indicators

# Help about an indicator such as bbands
# print(help(ta.bbands))
print(help(ta.supertrend))
