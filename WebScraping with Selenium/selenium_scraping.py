import time
import os
import selenium
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

webdriver = "C:\DOWNLOAD"
driver = Chrome(webdriver)

driver.get("https://www.bloomberg.com/quote/IBVC:IND")
time.sleep(3)
real_soup = BeautifulSoup(driver.page_source, 'html.parser')
open_ = real_soup.find("span", {"class": "priceText__1853e8a5"}).text
print(f"Price: {open_}")
time.sleep(3)
driver.quit()
