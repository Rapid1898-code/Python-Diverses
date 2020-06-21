import requests
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import ctypes

#user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
options = Options()
options.add_argument('--headless')
#options.add_argument("--width=100")
#options.add_argument("--heigth=100")
link = "https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL"
driver = webdriver.Chrome (os.getcwd () + '/chromedriver', options=options)
#driver.set_window_size(100,100)
driver.get(link)
time.sleep(3)
driver.find_element_by_name("agree").click()
time.sleep (3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (3)
driver.quit ()

table = soup.find(id="YDC-Col1")
erg = {}
list_table = []
for e in table.find_all(["th", "td"]): list_table.append(e.text.strip())
for i in range(0, len(list_table), 5): erg[list_table[i]] = list_table[i + 1:i + 5]
print(erg)