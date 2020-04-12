import urllib.request
from bs4 import BeautifulSoup


# specify the url
quote_page = "https://www.bloomberg.com/quote/SPX:IND"

# query the website and return the html to the variable "page"
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable "soup"
soup = BeautifulSoup(page)

# Take out the <div> of name and get its value
price_box = soup.find_all("div",{"class":"priceText__1853e8a5"}).get_text()
print(price_box)

