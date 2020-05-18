import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

# put the driver in the folder of this code

def read_ms_analysts(stock):
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
    link = "http://financials.morningstar.com/valuation/earnings-estimates.html?t=" + stock + "&region=usa&culture=en-US"
    driver.get(link)

    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', id="analyst_opinion_table")
    rows = table.findAll('tr')
    rating = False
    for idx, cont in enumerate(rows):
        if rating == True:
            return cont.text.strip().replace("—","").replace("\n","")
            break
        if "Average Rating" in cont.text.strip(): rating = True
    time.sleep (2)
    driver.quit ()

stock = "AAPL"
erg = read_ms_analysts(stock)
print(stock, ":", erg)



