
import requests

from bs4 import BeautifulSoup

try:
    source_url = "http://quotes.toscrape.com/"
    source = requests.get(source_url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')

    source_quotes = soup.find_all("div",class_ = "quote")

    source_title = source_quotes.find_all("span",class_ = "text")

    for items in source_title:
        print(items)
        break

except Exception as e:
    print(e)