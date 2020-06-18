import requests
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup

#link = "https://finance.yahoo.com/quote/AAPL/balance-sheet?p=AAPL"
link = "https://finance.yahoo.com/quote/CAT/balance-sheet?p=CAT"
#link = "https://finance.yahoo.com/quote/MSFT/balance-sheet?p=MSFT"
driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get(link)
time.sleep(2)
driver.find_element_by_name("agree").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span').click()
time.sleep (2)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (2)
driver.quit ()
table  = soup.find(id="Col1-1-Financials-Proxy")

erg = {}
list_div = []
for e in table.find_all(["div"]): list_div.append(e.text.strip())
while list_div[0] != "Breakdown": list_div.pop(0)
for i in range(len(list_div)-1,0,-1):
    if list_div[i].replace(",","").replace("-","").isdigit() or list_div[i] == "-": continue
    elif i == len(list_div)-1: del list_div[i]
    elif len(list_div[i]) == 0: del list_div[i]
    elif len (list_div[i]) > 50: del list_div[i]
    elif i == 0: break
    elif list_div[i] == list_div[i-1]: del list_div[i]
    elif list_div[i+1] in list_div[i]: del list_div[i]
idx = 0
while idx < len(list_div):
    if list_div[idx].replace(",","").replace("-","").isdigit() == False and list_div[idx] != "-": idx += 5
    else:
        while list_div[idx].replace(",","").replace("-","").isdigit() == True or list_div[idx] == "-":
            del list_div[idx]
idx = 0
while idx < len(list_div):
    erg[list_div[idx]] = list_div[idx+1:idx+5]
    idx += 5

for key,val in erg.items():
    print(key,val)
print(len(erg))


#idx = 0
#while idx < len(list_span)L
#    key = list_span[idx]
#    list_div.index()



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



