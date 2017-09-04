import requests
from bs4 import BeautifulSoup
import re

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_" + str(page) + '.html'
        source_code = requests.get(url)

        source_code.encoding = 'gb18030'
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'ulink'}):
            href = "http://www.ygdy8.net" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1


trade_spider(2)



