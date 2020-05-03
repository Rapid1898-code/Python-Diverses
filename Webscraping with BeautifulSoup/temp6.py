import requests
from bs4 import BeautifulSoup

def read_index(index_name):
    page_nr=0
    index_stocks = {}
    temp_stocks = {}
    while True:
        #page = requests.get ("https://www.ariva.de/"+index_name+"?page="+str(page_nr))
        page = requests.get ("https://www.ariva.de/" + index_name)
        soup = BeautifulSoup (page.content, "html.parser")
        table = soup.find(id="result_table_0")
        for row in table.find_all("td"):
            if row.get("class") == ["ellipsis", "nobr", "new", "padding-right-5"]:

                #print(row.prettify())
                #print("Wert1: ",row.find("a")["href"][1:])
                #print("Wert2: ",row.text.strip().capitalize())

                index_stocks[row.find("a")["href"][1:]] = row.text.strip().capitalize()

        print("PageNr: ",page_nr)
        print ("Temp Stock: ",temp_stocks)
        print ("Index  Stock:",index_stocks)
        print ("Temp-Index:  ", len (temp_stocks))
        print ("Len-Index:  ",len(index_stocks))

        #Dict sortieren nach Value
        index_stocks = {k: v for k, v in sorted(index_stocks.items(), key=lambda item: item[1])}
        if temp_stocks == index_stocks: break
        page_nr += 1
        temp_stocks = dict(index_stocks)
    return(index_stocks)

index = "s-p_500-index/kursliste"
stocks_final =  read_index(index)
print(stocks_final)
