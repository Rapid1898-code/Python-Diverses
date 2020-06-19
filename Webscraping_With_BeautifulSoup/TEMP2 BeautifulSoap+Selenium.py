import requests
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

link = "https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL"
driver = webdriver.Chrome (os.getcwd () + '/chromedriver')
driver.get(link)
time.sleep(3)
driver.find_element_by_name("agree").click()
time.sleep (3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (3)
driver.quit ()

table  = soup.find(id="app")
print(table.prettify())
