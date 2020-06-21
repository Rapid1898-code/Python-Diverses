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
link = "https://www.zacks.com/stock/quote/FB"
driver = webdriver.Chrome (os.getcwd () + '/chromedriver.exe', options=options)
#driver.set_window_size(100,100)
driver.get(link)
time.sleep (2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (2)
driver.quit ()

tmp = []
table = soup.find(id="right_content")
for row in soup.find_all("p", class_="rank_view"): tmp.append(row.text.strip())
print(tmp[0][-1])


