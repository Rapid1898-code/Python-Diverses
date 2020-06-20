import time
import os
import requests
import re
from selenium import webdriver
from bs4 import BeautifulSoup

link = "https://www.gurufocus.com/stock/" + symbol +"/summary"
page = requests.get (link)
soup = BeautifulSoup (page.content, "html.parser")
table = soup.find_all("h1")

