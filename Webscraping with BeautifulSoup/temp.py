import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

def read_stocktwits(account,emoji,scrolls=0):
    SCROLL_PAUSE_TIME = 0.5
    link = "https://stocktwits.com/" + account
    driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
    driver.get(link)
    time.sleep(2)
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(scrolls):
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
        if emoji in i.text and i.text.strip() not in erg_divs:
            if erg_divs != []:
                for j in i.text.strip().split():
                    if "$" in j and j.replace("$","") not in erg_stocks: erg_stocks.append(j.replace("$",""))
                    break
            erg_divs.append(i.text.strip())
    if erg_divs != []: erg_divs.pop(0)
    return(erg_divs, erg_stocks)
    time.sleep (2)
    driver.quit ()


COUNT_SCROLL_DOWN = 4
EMOJI = "🚨"     #🤝‍♂💪🚨
STOCKTWITS = "mrinvestorpro"

erg_cont, erg_stocks = read_stocktwits(STOCKTWITS,EMOJI,COUNT_SCROLL_DOWN)
print(erg_stocks)
