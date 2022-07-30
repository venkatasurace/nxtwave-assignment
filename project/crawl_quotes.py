
import requests

from bs4 import BeautifulSoup



url = " http://quotes.toscrape.com/"

request = requests.get(url)

soup = BeautifulSoup(request.content,"html.parser")

quotes = soup.find_all("div" ,class_ = "quote")

print(quotes)