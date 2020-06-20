import requests
import csv
from bs4 import BeautifulSoup

page = requests.get ("https://www.finanzen.net/historische-kurse/apple")
soup = BeautifulSoup (page.content, "html.parser")
#results = soup.find_all("div", class_="table-responsive")
results = soup.find_all("tr")
for result in results:
    print(result)
