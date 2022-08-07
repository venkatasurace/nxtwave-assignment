
import requests
 
from bs4 import BeautifulSoup

import pandas as pd

url = "http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

tittles = soup.select('.text')
authors = soup.select('.author')
tags = soup.select('.keywords')




def data_crawl_quotes(tittles,authors,tags):
    data_list = []
    for quote,author,tag in tittles,authors,tags:
        quote_text = quote.getText()
        author_text = author.getText()
        tags_text = tag.gettext()
        print(author_text)

data_crawl_quotes(tittles,authors,tags)



