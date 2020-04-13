import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

# put the driver in the folder of this code
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')

driver.get("https://www.bloomberg.com/quote/IBVC:IND")
time.sleep(3)
real_soup = BeautifulSoup(driver.page_source, 'html.parser')
open_ = real_soup.find("span", {"class": "priceText__1853e8a5"}).text
print(f"Price: {open_}")
time.sleep(3)
driver.quit()
