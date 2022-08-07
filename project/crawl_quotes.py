import requests
 
from bs4 import BeautifulSoup

import pprint

def data_crawl_quotes(tittles,authors,tags):
        list_a = []
        for quote,author,tag in zip(tittles,authors,tags):
            quote_text = quote.getText()
            author_text = author.getText()
            tags_text = tag.get("content")
            list_a.append({ "quotes":quote_text,"author":author_text,"Tags":tags_text})
        return list_a

source_url = "http://quotes.toscrape.com/"
full_list = []
for i in range(1,11):
    
    url = source_url
    response = requests.get(url)

    soup = BeautifulSoup(response.content,"html.parser")

    tittles = soup.select('.text')
    authors = soup.select('.author')
    tags = soup.select(".keywords")

    complete_data = data_crawl_quotes(tittles,authors,tags)
    full_list.append(complete_data)
    url = "http://quotes.toscrape.com/page/"+"str(i)"+"/"




pprint.pprint(full_list)



