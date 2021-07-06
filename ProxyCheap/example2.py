from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys, time
from sys import platform 
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def getChromeDriver(useProxy=False,useUserAgent=False,headless=False):
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
        options_seleniumWire = {
            'proxy': {
                'https': f'https://{PROXY_USER}:{PROXY_PW}@{PROXY_HOST}:{PROXY_PORT}',
            }
        }        

    if useUserAgent:
        ua = UserAgent()
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')                

    driver = webdriver.Chrome (path + cd, options=options, seleniumwire_options=options_seleniumWire)
    return driver

WAIT = 3
path = os.path.abspath (os.path.dirname (sys.argv[0]))
cd = '/chromedriver.exe'
load_dotenv(find_dotenv()) 
PROXY_USER = os.environ.get("PROXY_USER")
PROXY_PW= os.environ.get("PROXY_PW")
PROXY_HOST= os.environ.get("PROXY_HOST")  # rotating proxy or host
PROXY_PORT= os.environ.get("PROXY_PORT")

ua = UserAgent()
userAgent = ua.random

options = Options()
options.add_argument('--headless')
options.add_argument("--window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument(f'user-agent={userAgent}')        

options_seleniumWire = {
    'proxy': {
        'https': f'https://{PROXY_USER}:{PROXY_PW}@{PROXY_HOST}:{PROXY_PORT}',
    }
}
 
driver = webdriver.Chrome (path + cd, options=options, seleniumwire_options=options_seleniumWire)



driver.get("https://ifconfig.co/")

time.sleep(WAIT)
soup = BeautifulSoup (driver.page_source, 'html.parser')#
tmpErg = soup.find_all("tr")
print("\n")
for elem in tmpErg:
    print(f'{elem.find("th").text.strip()}: {elem.find("td").text.strip()}')