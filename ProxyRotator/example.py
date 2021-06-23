from random import choice
import requests
from bs4 import BeautifulSoup
import time
import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sys import platform 
from datetime import datetime, timedelta
from datetime import date
import re
import RapidTechTools as rtt

def proxy_generator():
  response = requests.get("https://sslproxies.org/")
  soup = BeautifulSoup(response.content, 'html5lib')
  erg = list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))) 
  erg = [x for x in erg if len(x) > 10]
  proxy = {'https://': choice(erg)}  
  return proxy

def clean_value(value, dp=".", tcorr=False, out="None"):
    """
    clean value to Float / Int / Char / None
    :param value: value which will be worked on
    :param dp: decimalpüint <.> or <,>
    :param tcorr: thousand corecction - if True numeric value will be multiplicated by 1000 - if False not
    :param out: output value in case of an invalid value
    :return: cleaned value (or error-value "N/A", None, "" defined in out)
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    pattern1 = re.compile ("^[a-zA-Z]{3} [0-9]{2}, [0-9]{4}$")
    pattern2 = re.compile ("^[0-9]{4}-[0-9]{2}$")
    pattern3 = re.compile ("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
    pattern4 = re.compile ("^[0-9]{1,2}/[0-9]{2}/[0-9]{4}$")
    pattern5 = re.compile ("^[a-zA-Z]{3}[0-9]{2}$")
    pattern6 = re.compile ("^[a-zA-Z]{3}[0-9]{4}$")
    value = rtt.replace_more(str(value).strip(), ["%","+-","+","$","€"])

    if pattern1.match(value) != None:
        value = datetime.strftime((datetime.strptime (value,"%b %d, %Y")),"%Y-%m-%d")
        return(value)
    elif pattern2.match(value) != None:
        dt = datetime.strptime (value, "%Y-%m")
        y = dt.year
        m = dt.month
        ultimo = calendar.monthrange (y, m)[1]
        value = datetime.strftime(date(y,m,ultimo), "%Y-%m-%d")
        return(value)
    elif pattern3.match(value) != None: return(value)
    elif pattern4.match (value) != None:
        value = datetime.strftime ((datetime.strptime (value, "%m/%d/%Y")), "%Y-%m-%d")
        return (value)
    elif pattern5.match (value) != None or pattern6.match (value) != None:
        if pattern5.match (value) != None:
            searchText = "%b%y"
        if pattern6.match (value) != None:
            searchText = "%b%Y"
        dt = datetime.strptime (value, searchText)
        m = dt.month
        y = dt.year
        ultimo = calendar.monthrange (y, m)[1]
        value = datetime.strftime (date (y, m, ultimo), "%Y-%m-%d")
        return(value)
    elif value in ["N/A","None","nan","-","—","","∞","-∞","Invalid Date","�","undefined"]:
        if out == "None": return(None)
        elif out == "N/A": return("N/A")
    elif ("M" in value or "B" in value or "T" in value or "k" in value) and rtt.replace_more(value, [",",".","M","B","T","k","-","$"]).isdigit():
        if "M" in value: char = "M"
        elif "B" in value: char = "B"
        elif "T" in value: char = "T"
        elif "k" in value: char = "k"
        decimal_place = value.find(dp)
        b_place = value.find(char)
        if decimal_place == -1:
            b_place = 1
            decimal_place = 0
        if char in ["M", "B", "T"]: value = rtt.replace_more(value, [".",",",char])
        # million
        if char == "M":
            for i in range (3 - (b_place - decimal_place - 1)): value = value + "0"
        # billion
        if char == "B":
            for i in range(6 - (b_place - decimal_place -1)): value = value + "0"
        # trillion
        if char == "T":
            for i in range(9 - (b_place - decimal_place -1)): value = value + "0"
        # thousand
        if char == "k":
            value = value.replace("k","")
        value = float(value)
        if tcorr: return (value * 1000)
        else: return (value)
    elif ":" in value: return(value)
    elif rtt.replace_more(value, [",",".","-","$"]).isdigit () == True:
        if dp == ",":
            if "." in value and "," in value: value = value.replace(".","")
            if "," in value: value = float(value.replace(",","."))
            else: value = int(value.replace(".",""))
            if tcorr: return(value * 1000)
            else: return (value)
        elif dp == ".":
            if "," in value and "." in value: value = value.replace(",","")
            if "." in value: value = float(value)
            else: value = int(value.replace(",",""))
            if tcorr: return(value * 1000)
            else: return (value)
        else: print(f"Wrong dp parameter vor {value}")
    else: return(value)

# def data_scraper(request_method, url, **kwargs):
#     while True:
#         try:
#             proxy = proxy_generator()
#             print("Proxy currently being used: {}".format(proxy))
#             response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
#             break
#             # if the request is successful, no exception is raised
#         except:
#             print("Connection error, looking for another proxy")
#             pass
#     return response

# response = data_scraper('get', "https://zenscrape.com/ultimate-list-15-best-services-offering-rotating-proxies/")
# print(response.text)



# # reading with requests with proxy+header
# link = "https://finance.yahoo.com/quote/AAPL"
# headers = {
#     # 'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
# }
# proxy = proxy_generator()

# while True:
#     try:
#         page = requests.get (link, headers=headers, proxies=proxy)
#         break
#     except:
#         print(f"Working with proxy {proxy} not possible - try another one...")
#         proxy = proxy_generator()

# soup = BeautifulSoup (page.content, "html.parser")
# time.sleep(1)
# table = soup.find ('div', id="quote-header-info")
# header = table.find ("h1").text
# erg = {}
# erg["name"] = header.strip ()
# erg["currency"] = table.find (["span"]).text.strip()[-3:].upper()
# erg["exchange"] = table.find (["span"]).text.split("-")[0].strip()
# print(f"Data read with random proxy {proxy}...")
# for key, val in erg.items ():
#     print (f"{key} => {val} {type(val)}")


# reading with selenium with proxy+header
link = "https://finance.yahoo.com/quote/AAPL/balance-sheet?p=AAPL"
if platform == "win32": cd = '/chromedriver.exe'
elif platform == "linux": cd = '/chromedriver'
elif platform == "darwin": cd = '/chromedriver'
options = Options()
# options.add_argument('--headless')
options.add_experimental_option ('excludeSwitches', ['enable-logging'])        
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36")   
path = os.path.abspath (os.path.dirname (sys.argv[0]))

proxy = proxy_generator()
for key, value in proxy.items():
    proxySelenium = value

while True:
    # try:
        # options.add_argument('--proxy-server=http://%s' %proxy)
        # options.add_argument(f"--proxy-server={proxySelenium}")
        driver = webdriver.Chrome (path + cd, options=options)
        driver.get (link)
        break
    # except:
        proxy = proxy_generator()
        print(f"Working with proxy {proxy} not possible - try another one...")

erg = {}

try:
    driver.find_element_by_name ("agree").click ()
    time.sleep (2)
except:
    pass
driver.find_element_by_xpath ('//*[@id="Col1-1-Financials-Proxy"]/section/div[2]/button/div/span').click ()
time.sleep (2)
soup = BeautifulSoup (driver.page_source, 'html.parser')

table = soup.find (id="quote-header-info")
erg["Header"] = ["AAPL", "in thousands", table.find (["span"]).text.strip ()]
table = soup.find (id="Col1-1-Financials-Proxy")

list_div = []
for e in table.find_all (["div"]): list_div.append (e.text.strip ())

while list_div[0] != "Breakdown": list_div.pop(0)
for i in range (len (list_div) - 1, 0, -1):
    if list_div[i].replace (".", "").replace (",", "").replace ("-", "").isdigit () or list_div[i] == "-": continue
    elif i == len (list_div) - 1: del list_div[i]
    elif len (list_div[i]) == 0: del list_div[i]
    elif len (list_div[i]) > 50: del list_div[i]
    elif i == 0: break
    elif list_div[i] == list_div[i - 1]: del list_div[i]
    elif list_div[i + 1] in list_div[i]: del list_div[i]

# Eliminate numeric entries on the false position
pos = list_div.index ("Total Assets")
idx = 0
# If the element is a Digit - this is wrong and the elements got deleted as long they are an digit
while idx < len (list_div):
    # When Non-Digit - jump POS forward
    if list_div[idx].replace (",", "").replace ("-", "").replace (".", "").isdigit () == False and list_div[idx] != "-":
        idx += pos
    else:
        while list_div[idx].replace (",", "").replace ("-", "").replace (".", "").isdigit () == True or list_div[idx] == "-":
            del list_div[idx]
            # if the wrong digit values are at the very end - check if end of list is reached
            if idx == len(list_div):
                break

for i in range(len(list_div)-1):
    if list_div[i].replace(".", "").replace(",", "").replace("-", "").isdigit():
        list_div[i] = float(list_div[i].replace(",",""))

idx = 0
while idx < len (list_div):
    erg[list_div[idx]] = list_div[idx + 1:idx + pos]
    idx += pos

for key,val in erg.items():
    for idx,cont in enumerate(val):
        erg[key][idx] = clean_value(erg[key][idx],tcorr=True)

# skip one day future
# when reading online the ultimo is 1 day minus in contrast to the csv-reading
for idx,cont in enumerate(erg["Breakdown"]):
    if cont == "ttm": continue
    tmp = datetime.strptime(cont, "%Y-%m-%d") + timedelta(days=1)
    erg["Breakdown"][idx] = datetime.strftime(tmp, "%Y-%m-%d")

for key, val in erg.items ():
    print (f"{key} => {val} {type(val)}")