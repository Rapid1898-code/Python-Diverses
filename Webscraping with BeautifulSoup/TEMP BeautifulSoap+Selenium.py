import requests
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

link = "https://finance.yahoo.com/quote/AAPL/financials?p=AAPL"
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get(link)
time.sleep(2)
driver.find_element_by_name("agree").click()
time.sleep(2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (2)
driver.quit ()

table  = soup.find(id="Col1-1-Financials-Proxy")                        # Read specific invidual id
tmp = table.find_all(["div"])
for row in tmp:
    print(row.text.strip())

"""
tmp = soup.find('div', attrs={"data-reactid": "51"})
print(soup.find('span', attrs={"data-reactid": "64"}).text.strip())
for row in soup.find_all("tr"): print(row.prettify())
table = soup.find ('p', attrs={"class": "businessSummary Mt(10px) Ov(h) Tov(e)"})
spans = table.find_all ("span")
sector = spans[1].text.strip()
industry = spans[3].text.strip()
empl = spans[5].text.strip()
table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
description = table.find("p").text.strip()
print(sector)
print(industry)
print(description)
"""








"""
for row in soup.find_all("tr"): print(row.prettify())
table = soup.find ('p', attrs={"class": "businessSummary Mt(10px) Ov(h) Tov(e)"})
spans = table.find_all ("span")
sector = spans[1].text.strip()
industry = spans[3].text.strip()
empl = spans[5].text.strip()
table = soup.find ('section', attrs={"class": "quote-sub-section Mt(30px)"})
description = table.find("p").text.strip()
print(sector)
print(industry)
print(description)
"""



