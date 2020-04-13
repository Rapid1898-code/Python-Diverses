# https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.at/jobs/suche/?q=Software-Devel&where=Graz"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

name_box = soup.findAll("div", attrs={"class": "company"})
print (name_box)
