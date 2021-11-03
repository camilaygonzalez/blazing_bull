#!/usr/bin/env python3
from bs4 import BeautifulSoup #installl with 'pip install BeautifulSoup4'
from urllib.request import urlopen
# variable to store website link as string
page = range(50)
for i in page:
    url_to_scrape = 'http://books.toscrape.com/catalogue/page-' + str(i+1) + '.html'
    # read and close HTML
    request_page = urlopen(url_to_scrape)
    page_html = request_page.read()
    #request_page.close()
    # call BeautifulSoup for parsing
    html_soup = BeautifulSoup(page_html, 'html.parser')
    print(html_soup.prettify()[:1000])
    book_items = html_soup.find_all('article',class_="product_pod")
    print(book_items)
    # create csv file of all products
    filename = "bookproducts.csv"
    f = open(filename, 'a')
    headers = "Title, Price, Availibility, Rating(Stars), \n"
    f.write(headers)
    for book in book_items:
        # collect title of all books
        Title = book.find('h3').find('a').get('title').replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u201c', '"').replace(u'\u201d', '"').replace(u'\xe1',' ').replace(u'\xe9',' ')
        # collect price of all books
        Price = "$" + book.find('p', class_='price_color').text.strip().encode('ascii','ignore').decode('ascii')
        #collect availibilty of all books
        Availibility = book.find('p', class_='instock').text.strip().encode('ascii','ignore').decode('ascii')
        #collect rating of all books
        Rating = book.find('p', class_='star-rating').get('class')[1]
        #print(title)
        #print(price)
        #print(availibility)
        #print(rating)
        f.write(Title + ',' + Price + ',' + Availibility + ',' + Rating + '\n')
    f.close()
