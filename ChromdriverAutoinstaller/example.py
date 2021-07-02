# from selenium import webdriver
import chromedriver_autoinstaller
# from selenium.webdriver.chrome.options import Options
# import os,sys

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

# options = Options()
# cd = '/chromedriver.exe'
# path = os.path.abspath (os.path.dirname (sys.argv[0]))
# driver = webdriver.Chrome (path + cd, options=options)
# driver.get("http://www.python.org")
# assert "Python" in driver.title