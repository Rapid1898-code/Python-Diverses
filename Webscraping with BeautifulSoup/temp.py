import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

SCROLL_PAUSE_TIME = 0.5
COUNT_SCROLL_DOWN = 5
EMOJI = "🚨"     #🤝‍♂💪🚨
STOCKWITS = "mrinvestorpro"


link = "https://stocktwits.com/" + STOCKWITS
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get(link)
time.sleep(2)
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

for i in range(COUNT_SCROLL_DOWN):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find ('div', attrs={"infinite-scroll-component__outerdiv"})
divs = table.find_all ("div")
erg_divs=[]
erg_stocks=[]
for i in divs:
    if EMOJI in i.text and i.text.strip() not in erg_divs:
        if erg_divs != []:
            for j in i.text.strip().split():
                if "$" in j and j.replace("$","") not in erg_stocks: erg_stocks.append(j.replace("$",""))
                break
        erg_divs.append(i.text.strip())
if erg_divs != []: erg_divs.pop(0)
for i in erg_divs: print(i,"\n")
print(erg_stocks)
time.sleep (2)
driver.quit ()

"""
table = soup.find ('div', attrs={"class": "st_gIQ1cL6 st_2-AYUR9"})
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

