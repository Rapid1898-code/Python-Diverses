from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys,os
from sys import platform

options = Options()
# options.add_argument('--headless')
options.add_experimental_option ('excludeSwitches', ['enable-logging'])
path = os.path.abspath (os.path.dirname (sys.argv[0]))
if platform == "win32": cd = '/chromedriver.exe'
elif platform == "linux": cd = '/chromedriver'
elif platform == "darwin": cd = '/chromedriver'
driver = webdriver.Chrome (path + cd, options=options)    

link = "https://www.orf.at/"
driver.get (link)
driver.close()
