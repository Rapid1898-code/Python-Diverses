import requests
from bs4 import BeautifulSoup

def read_index(index_name):
    page = requests.get ("https://www.ariva.de/"+index_name)
    soup = BeautifulSoup (page.content, "html.parser")
    table  = soup.find(id="result_table_0")
    index_stocks = {}
    print(type(index_stocks))
    for row  in table.find_all("td"):
        if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:
            index_stocks[row.find("a")["href"]] = row.text.strip()
    print(type(index_stocks))

    #index_stocks = sorted(index_stocks.items (), key=lambda x: x[1])
    index_stocks = {k: v for k, v in sorted(index_stocks.items(), key=lambda item: item[1])}


    print (type (index_stocks))
    return(index_stocks)

idx = read_index("dax-30")
print(idx)

