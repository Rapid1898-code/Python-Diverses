import requests
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

def is_na(value):
    if "N/A" in value: return "N/A"
    else: return value

#stock = "AAPL"
#link = "https://finance.yahoo.com/quote/" + stock + "/key-statistics?p=" + stock
#link = "https://finance.yahoo.com/quote/" + stock + "/balance-sheet?p=" + stock
#link = "https://finance.yahoo.com/quote/AAPL/cash-flow?p=AAPL"
link = "https://finance.yahoo.com/quote/AAPL/history?period1=345427200&period2=1592697600&interval=1d&filter=history&frequency=1d"
#link = "https://finance.yahoo.com/quote/CAT/analysis?p=CAT"
#link = "https://finance.yahoo.com/quote/MSFT/analysis?p=MSFT"
#options = Options()
#options.add_argument('--headless')
#driver = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)
driver = webdriver.Chrome (os.getcwd () + '/chromedriver')
driver.get(link)
time.sleep(3)
driver.find_element_by_name("agree").click()
time.sleep (3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep (3)
driver.quit ()

table  = soup.find(id="Col1-1-HistoricalDataTable-Proxy")
for e in table.find_all(["th","td"]): print(e.text.strip())


"""
tmp_list = []
#table  = soup.find(id="YDC-Col2")
table = soup.find("div", class_="Pos(r) T(5px) Miw(100px) Fz(s) Fw(500) D(ib) C($primaryColor)Ta(c) Translate3d($half3dTranslate)")
#table = soup.find (id="mrt-node-Col2-4-QuoteModule")
for i in table.find_all(["div"]): print(i.text.strip())

#for e in table.find_all(["span"]): print(e.text.strip())
#for e in table.find_all(["div"]): tmp_list.append(e.text.strip())
#for i in range (len(tmp_list)-1,0,-1):
#    if len(tmp_list[i]) != 1: del tmp_list[i]
    tmp_list.append(e.text.strip())
    tmp_list.append(e.text.strip())
    tmp_list.append(e.text.strip())
    tmp_list.append(e.text.strip())
"""

"""
list_div = []
table = soup.find(id="Col1-1-Financials-Proxy")
for e in table.find_all (["div"]): print(e.text.strip())
"""

"""
erg_stat = {}
erg_val = {}
tmp_list = []
table  = soup.find(id="Col1-0-KeyStatistics-Proxy")
for e in table.find_all(["th","td"]): tmp_list.append(e.text.strip())
for idx,cont in enumerate(tmp_list):
    if "Beta" in cont:
        tmp_list_stat = list(tmp_list[idx:])
        tmp_list_val =  list(tmp_list[:idx])
for i in range(0,len(tmp_list_stat),2): erg_stat[tmp_list_stat[i]] = is_na(tmp_list_stat[i+1])
for i in range(0,len(tmp_list_val),7): erg_val[tmp_list_val[i]] = tmp_list_val[i+1:i+7]
"""

#for key,val in erg_stat.items():
#    print(key,val)
#print(len(erg_stat))

#for key,val in erg_val.items():
#    print(key,val)
#print(len(erg_val))

"""
table  = soup.find(id="YDC-Col1")
erg = {}
list_table = []
for e in table.find_all(["th","td"]): list_table.append(e.text.strip())
for i in range(0,len(list_table),5): erg[list_table[i]] = list_table[i+1:i+5]

for key,val in erg.items():
    print(key,val)
print(len(erg))
"""

"""
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



