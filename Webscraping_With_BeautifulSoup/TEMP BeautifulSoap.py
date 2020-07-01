import requests
from bs4 import BeautifulSoup


link1 = "https://levermann24.com"
page1 = requests.get (link1)
soup1 = BeautifulSoup (page1.content, "html.parser")

list = []
for e in soup1.find_all("a"):
    if e.get("href") != None and "javascript" not in e.get("href"):
        tmp = e.get("href").replace("https://levermann24.com/","")[:-1]

        list.append(tmp)

print(list)












