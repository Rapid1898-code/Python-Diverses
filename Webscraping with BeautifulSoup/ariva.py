import requests
import csv
from bs4 import BeautifulSoup

page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2001-11-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")
soup = BeautifulSoup (page.content, "html.parser")

# read table with monatlichen Kursen
for result in soup.find_all("tr", class_="arrow0"):
    for row in result.find_all("td"):
        if row.text[0].isdigit(): print (row.text.strip())


