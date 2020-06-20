# https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/

import requests
from bs4 import BeautifulSoup

URL = "https://www.bloomberg.com/quote/SPX:IND"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


name_box = soup.find("h1", attrs={"class": "companyName__99a4824b"})
print (name_box)
