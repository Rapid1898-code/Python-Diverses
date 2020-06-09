import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
import smtplib
from email.mime.text import MIMEText

wb = load_workbook("AlertSheet.xlsx")
ws_db = wb["Dashboard"]
ws_at = wb["Alert Tracker"]

stocks = []
for col in ws_at["A"]: stocks.append(col.value)

if ws_db["C3"].value != None and ws_db["C3"].value not in stocks:
    msg = ""
    symbol = ws_db["C3"].value
    link = "https://finance.yahoo.com/quote/" + symbol
    link2 = link + "/profile?p=" + symbol
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")

    # Read Volumes
    table = soup.find ('div', id="quote-header")
    volume = soup.find ('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip ()
    avg_volume = soup.find ('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip ()

    # Read Ranges
    d_r_tmp = soup.find ('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip ().split ('-')
    day_range_from, day_range_to = d_r_tmp[0].strip (), d_r_tmp[1].strip ()
    f_r_temp = soup.find ('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip ().split ('-')
    fifty_range_from, fifty_range_to = f_r_temp[0].strip (), f_r_temp[1].strip ()

    # Read stockname, actual price, daychange
    table = soup.find ('div', id="quote-header-info")
    name = table.find ("h1").text.split ("-")[1].strip ()
    price = soup.find ('span', attrs={"data-reactid": "14"}).text.strip ()
    daychange_tmp = soup.find ('span', attrs={"data-reactid": "16"}).text.strip ().split ("(")
    daychange = daychange_tmp[0].strip ()
    daychange_perc = daychange_tmp[1].strip ().replace (")", "")

    # Read MarketCap, PrevClose, PE, EPS
    marketcap = soup.find ('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip ()
    prevclose = soup.find ('td', attrs={"data-test": "PREV_CLOSE-value"}).text.strip ()

    # Read Additional Infos
    page = requests.get (link2)
    soup = BeautifulSoup (page.content, "html.parser")
    empl = soup.find ('span', attrs={"data-reactid": "30"}).text.strip ()
    sector_tmp = soup.find_all ('span', attrs={"data-reactid": "21"})
    for row in sector_tmp:
        if row.get ("class") != None: sector = row.text.strip ()
    industry_tmp = soup.find_all ('span', attrs={"data-reactid": "25"})
    for row in industry_tmp:
        if row.get ("class") != None: industry = row.text.strip ()
    description = soup.find ('p', attrs={"data-reactid": "141"}).text.strip ()

    s = smtplib.SMTP ('smtp.gmail.com', 587)  # SMTP-Server and port number from the mail provider (e.g. GMail)
    print (s.ehlo ())  # Check if OK - Response 250 means connection is ok
    print (s.starttls ()) # Check if OK
    print (s.login (ws_db["A15"].value, ws_db["D15"].value)) # Check if OK

    msg =   "DASHBOARD/nCurrent Volume:"+ volume +\
            "/nAverage Volume:"+ avg_volume +\
            "/nDay Low/High:"+ day_range_from,"/",day_range_to +\
            "/n52W Range:" + fifty_range_from,"/",fifty_range_to +\
            "/nSymbol-Name:" + symbol,"-",name+\
            "/nSector:" + sector +\
            "/nIndustry:" + industry +\
            "/nCurrent Price (day change %):" + price,daychange_perc +\
            "/nCompany Description:",description +\
            "/nMarketCap:" + marketcap +\
            "/nPrev close:" + prevclose +\
            "/n# of Employees:",empl

"""
symbol = "AAPL"
link = "https://finance.yahoo.com/quote/"+symbol
link2 = link+"/profile?p="+symbol

page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")

# Read stockname, actual price, daychange
table = soup.find('div', id="quote-header-info")
name = table.find("h1").text.split("-")[1].strip()
price = soup.find('span', attrs={"data-reactid": "14"}).text.strip()
daychange_tmp = soup.find('span', attrs={"data-reactid": "16"}).text.strip().split("(")
daychange = daychange_tmp[0].strip()
daychange_perc = daychange_tmp[1].strip().replace(")","")

# Read Volumes
table = soup.find('div', id="quote-header")
volume = soup.find('td', attrs={"data-test": "TD_VOLUME-value"}).text.strip()
avg_volume = soup.find('td', attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text.strip()

# Read Ranges
d_r_tmp = soup.find('td', attrs={"data-test": "DAYS_RANGE-value"}).text.strip().split('-')
day_range_from, day_range_to = d_r_tmp[0].strip(), d_r_tmp[1].strip()
f_r_temp = soup.find('td', attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.strip().split('-')
fifty_range_from, fifty_range_to = f_r_temp[0].strip(), f_r_temp[1].strip()

# Read MarketCap, PrevClose, PE, EPS
marketcap = soup.find('td', attrs={"data-test": "MARKET_CAP-value"}).text.strip()
prevclose = soup.find('td', attrs={"data-test": "PREV_CLOSE-value"}).text.strip()
pe_ratio = soup.find('td', attrs={"data-test": "PE_RATIO-value"}).text.strip()
eps_ratio = soup.find('td', attrs={"data-test": "EPS_RATIO-value"}).text.strip()

# Read Additional Infos
page = requests.get (link2)
soup = BeautifulSoup (page.content, "html.parser")
empl = soup.find('span', attrs={"data-reactid": "30"}).text.strip()
sector_tmp = soup.find_all('span', attrs={"data-reactid": "21"})
for row in sector_tmp:
    if row.get("class") != None: sector = row.text.strip()
industry_tmp = soup.find_all('span', attrs={"data-reactid": "25"})
for row in industry_tmp:
    if row.get("class") != None: industry = row.text.strip()
description = soup.find('p', attrs={"data-reactid": "141"}).text.strip()

print("\nALERT TRACKER")
print("Symbol:", symbol)
print("Name:", name)
print("Sector:", sector)
print("Price:", price)
print("DayChange:",daychange)
print("DayChange_Perc:",daychange_perc)
print("MarketCap:", marketcap)
print("PE-Rato:", pe_ratio)
print("EPS-Ratio:", eps_ratio)
print("52W Low:", fifty_range_from)
print("52W HIgh:", fifty_range_to)

print("\nDASHBOARD")
print("Current Volume:", volume)
print("Average Volume:", avg_volume)
print("Day Low/High:", day_range_from,"/", day_range_to)
print("52W Range:", fifty_range_from,"/",fifty_range_to)
print("Symbol-Name:",symbol,"-",name)
print("Sector:",sector)
print("Industry:",industry)
print("Current Price (day change %):",price,daychange_perc)
print("Company Description:",description)
print("MarketCap:",marketcap)
print("Prev close:",prevclose)
print("# of Employees:",empl)
"""















