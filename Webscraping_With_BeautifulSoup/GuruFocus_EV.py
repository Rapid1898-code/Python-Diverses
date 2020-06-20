import time
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# https://www.gurufocus.com/term/ev/BAYZF/Enterprise-Value/Bayer-AG
# https://www.gurufocus.com/term/ev/AAPL/Enterprise-Value/Apple

link = "https://www.gurufocus.com/term/ev/AAPL/Enterprise-Value/Apple"

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

#driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
#driver.get(link)
#time.sleep(2)
#soup = BeautifulSoup(driver.page_source, 'html.parser')

table = soup.find('div', id="def_body_detail_height")
erg = table.font.text
erg = re.sub("\D", "", erg)
print(erg)

#time.sleep (2)
#driver.quit ()




