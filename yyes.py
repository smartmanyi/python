import requests
from bs4 import BeautifulSoup
import re

def trade_spider():

    url = "http://www.yyetss.com/detail-2913.html"
    source_code = requests.get(url)
    source_code.encoding = 'tuf-8'
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)


trade_spider()