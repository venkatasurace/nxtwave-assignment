import requests
 
from bs4 import BeautifulSoup

import pprint

import pandas as pd

url = "http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

tittles = soup.select('.text')
authors = soup.select('.author')
tags = soup.select(".keywords")


def data_crawl_quotes(tittles,authors,tags):
    list_a = []
    for quote,author,tag in zip(tittles,authors,tags):
        quote_text = quote.getText()
        author_text = author.getText()
        tags_text = tag.get("content")
        list_a.append({ "quotes":quote_text,"author":author_text,"Tags":tags_text})
    return list_a

pprint.pprint(data_crawl_quotes(tittles,authors,tags))



