import csv
import urllib.request
import codecs

url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1592697600&interval=1d&events=history'
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
for row in csvfile: print(row)



