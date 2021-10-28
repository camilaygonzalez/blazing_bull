#!/usr/bin/env python3

#from urllib.request import urlopen 
from bs4 import BeautifulSoup #install with 'pip install BeautifulSoup4
import json
import requests #install with pip install requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
    }

url_to_scrape = "https://www.sephora.com/shop/hair-products"
source = requests.get('url_to_scrape') #making the http request
data = r.text
soup = BeautifulSoup(data,'html.parser') #    # Creating the Soup Object containing all data 

data = json.loads(soup.find('script', id='linkJSON').text)
products = data[3]['props']['products'] #how you get data in list/dictionary in Python json.loads convert the JSON data to Python's data structure

prefix = "https://www.sephora.com"

url_links = [prefix+p["targetUrl"] for p in products]
print(url_links)



#url_to_scrape = "https://example.com/"

request_page = urlopen(url_to_scrape).add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
print(request_page)
page_html = request_page.read()
print(page_html)
request_page.close()

print(request_page)

#html_soup = BeautifulSoup(page_html, 'html.parser')

#gather the data from the pages to form the csv

sephora_items = html_soup.find_all('div',{'class': "ProductTile-name css-h8cc3p eanm77i0"})

filename = "products.csv"
f = open(filename, 'w')

headers = "Title, Price /n"

f.write(headers)

for sephora in sephora_items:
    title = sephora.find ('div', {'class': "css-bpsjlq eanm77i0"}).text
    price = sephora.find ('div', {'class': "css-0"}).text

    f.write(title + ',' + price)

f.close()
