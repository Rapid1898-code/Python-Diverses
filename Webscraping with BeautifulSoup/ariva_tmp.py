import requests
import csv
from datetime import datetime
from datetime import date
import calendar
from bs4 import BeautifulSoup

page = requests.get ("https://www.ariva.de/wirecard-aktie/historische_kurse?boerse_id=40&month=2020-04-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")
soup = BeautifulSoup (page.content, "html.parser")
table  = soup.find(id="result_table_0")
print (table)
