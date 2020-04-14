import requests
import csv
from bs4 import BeautifulSoup

page = requests.get ("https://www.ariva.de/apple-aktie/historische_kurse?boerse_id=40&month=2001-11-30&currency=EUR&clean_split=1&clean_split=0&clean_payout=0&clean_bezug=1&clean_bezug=0")
soup = BeautifulSoup (page.content, "html.parser")

# read table with monatlichen Kursen
results = soup.find_all("tr", class_="arrow0")
results2 = []

for result in results:
    results2.append(result.find_all("td"))

for result in results2:
    for row in result:
        if row.text[0].isdigit(): print (row.text.strip())


