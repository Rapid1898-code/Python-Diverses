from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
# import os,sys

chromedriver_autoinstaller.install()

options = Options()
# cd = '/chromedriver.exe'
# path = os.path.abspath (os.path.dirname (sys.argv[0]))
driver = webdriver.Chrome (chromedriver_autoinstaller.install(), options=options)
driver.get("http://www.python.org")
assert "Python" in driver.title