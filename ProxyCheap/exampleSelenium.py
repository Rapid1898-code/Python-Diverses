from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys, time
from sys import platform 
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

WAIT = 3

def getSeleniumDriver(useProxy=False,useUserAgent=False,headless=False):
    path = os.path.abspath (os.path.dirname (sys.argv[0])) 
    if platform == "win32": cd = '/chromedriver.exe'
    elif platform == "linux": cd = '/chromedriver'
    elif platform == "darwin": cd = '/chromedriver'  

    options_seleniumWire = {}

    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')         
    if headless:
        options.add_argument('--headless')

    if useProxy:
        load_dotenv(find_dotenv()) 
        PROXY_USER = os.environ.get("PROXY_USER")
        PROXY_PW= os.environ.get("PROXY_PW")
        PROXY_HOST= os.environ.get("PROXY_HOST")  # rotating proxy or host
        PROXY_PORT= os.environ.get("PROXY_PORT")
        proxyLink = f'https://{PROXY_USER}:{PROXY_PW}@{PROXY_HOST}:{PROXY_PORT}'
        print(f"DEBUG ProxyLink: {proxyLink}")
        
        options_seleniumWire = {
            'proxy': {
                'https': proxyLink,
            }
        }        

    if useUserAgent:
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')                

    driver = webdriver.Chrome (path + cd, options=options, seleniumwire_options=options_seleniumWire)
    return driver

driver = getSeleniumDriver(useProxy=True,useUserAgent=True,headless=True)
# driver = getChromeDriver(useProxy=False,useUserAgent=False,headless=True)
# driver = getChromeDriver(useProxy=False,useUserAgent=True,headless=True)

driver.get("https://ifconfig.co/")

time.sleep(WAIT)
soup = BeautifulSoup (driver.page_source, 'html.parser')#
tmpErg = soup.find_all("tr")
print("\n")
for elem in tmpErg:
    print(f'{elem.find("th").text.strip()}: {elem.find("td").text.strip()}')