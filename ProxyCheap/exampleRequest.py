import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
import os, sys, time

WAIT = 3

def getRequestInfos (useProxy=False,useUserAgent=False):
  if useProxy:
    load_dotenv(find_dotenv()) 
    PROXY_USER = os.environ.get("PROXY_USER")
    PROXY_PW= os.environ.get("PROXY_PW")
    PROXY_HOST= os.environ.get("PROXY_HOST")  # rotating proxy or host
    PROXY_PORT= os.environ.get("PROXY_PORT")
    proxyLink = f'http://{PROXY_USER}:{PROXY_PW}@{PROXY_HOST}:{PROXY_PORT}'
    PROXY = {'http': proxyLink}
    print(f"DEBUG ProxyLink: {PROXY}")
  else:
    PROXY = {}

  if useUserAgent:
    ua = UserAgent()
    userAgent = ua.random
    HEADERS = {'User-Agent': userAgent}
  else:
    HEADERS = {}

  return HEADERS, PROXY



link = "http://ifconfig.co/"

HEADERS, PROXY = getRequestInfos(useProxy=True, useUserAgent=True)
page = requests.get (link, headers=HEADERS, proxies=PROXY)

soup = BeautifulSoup (page.content, "html.parser")
tmpErg = soup.find_all("tr")
print("\n")
for elem in tmpErg:
    print(f'{elem.find("th").text.strip()}: {elem.find("td").text.strip()}')