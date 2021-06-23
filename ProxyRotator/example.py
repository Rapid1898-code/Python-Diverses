from random import choice
import requests
from bs4 import BeautifulSoup

def proxy_generator():
  response = requests.get("https://sslproxies.org/")
  soup = BeautifulSoup(response.content, 'html5lib')
  erg = list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text, soup.findAll('td')[1::8]))))) 
  erg = [x for x in erg if len(x) > 10]
  proxy = {'https://': choice(erg)}  
  return proxy

def data_scraper(request_method, url, **kwargs):
    while True:
        try:
            proxy = proxy_generator()
            print("Proxy currently being used: {}".format(proxy))
            response = requests.request(request_method, url, proxies=proxy, timeout=7, **kwargs)
            break
            # if the request is successful, no exception is raised
        except:
            print("Connection error, looking for another proxy")
            pass
    return response

response = data_scraper('get', "https://zenscrape.com/ultimate-list-15-best-services-offering-rotating-proxies/")
print(response.text)
