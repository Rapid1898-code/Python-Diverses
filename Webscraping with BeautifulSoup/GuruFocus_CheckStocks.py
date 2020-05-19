import time
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# https://www.gurufocus.com/term/ev/BAYZF/Enterprise-Value/Bayer-AG
# https://www.gurufocus.com/term/ev/AAPL/Enterprise-Value/Apple

def check_symbol (symbol):
    link = "https://www.gurufocus.com/stock/" + symbol +"/summary"
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")
    table = soup.find_all("h1")
    for i in table:
        if "Stock Not Found" in i.text: return False
    table = soup.find_all("a")
    check = [False, False, False]
    for i in table:
        if "Premium Membership" in i.text: return False
        if "Financial Strength" in i.text: check[0] = True
        if "Profitability Rank" in i.text: check[1] = True
        if "Valuation Rank" in i.text: check[2] = True
        if False not in check: return True
    return False

for j in range (485):
    link = "https://www.gurufocus.com/stock_list.php?m_country[]=_Europe&m_country[]=DEU&m_country[]=FRA&m_country[]" \
           "=POL&m_country[]=RUS&m_country[]=SWE&m_country[]=TUR&m_country[]=BIH&m_country[]=ITA&m_country[]" \
           "=LUX&m_country[]=CHE&m_country[]=BEL&m_country[]=GRC&m_country[]=NOR&m_country[]=ESP&m_country[]" \
           "=DNK&m_country[]=BGR&m_country[]=NLD&m_country[]=ROU&m_country[]=FIN&m_country[]=SRB&m_country[]" \
           "=AUT&m_country[]=HRV&m_country[]=PRT&m_country[]=SVK&m_country[]=CYP&m_country[]=MKD&m_country[]" \
           "=SVN&m_country[]=UKR&m_country[]=HUN&m_country[]=LTU&m_country[]=LVA&m_country[]=MLT&m_country[]" \
           "=ISL&m_country[]=EST&m_country[]=CZE&m_country[]=_India&m_country[]=IND&m_country[]=PAK&sort=company&p=" + j + "&n=100"
    page = requests.get (link)
    soup = BeautifulSoup (page.content, "html.parser")

    checked = []
    stocks = []
    table = soup.find_all("td", class_="text")
    for i in range(0,len(table),2):
        idx = table[i].a.text.find(".")
        symbol = table[i].a.text[0:idx]
        name = table[i+1].a.text
        print ("Working on", symbol, name)
        if symbol not in checked:
            bool = check_symbol (symbol)
            if bool == True:
                stocks.append([symbol, name])
                print ("Found Stock: ", symbol, name)
            checked.append(symbol)
    print ("Check Page",j)
    print (stocks.sort())
print ("Final: ", stocks.sort())






