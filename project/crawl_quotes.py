
import requests
 
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")


quotes = soup.find_all("span" ,class_ = "text")

quotes = [quote.text[1:-1] for quote in quotes]

authors = soup.find_all("small" ,class_ = "author")

authors = [author.text[1:-1] for author in authors]

tags = soup.find_all("div" ,class_ = "tags")

total_tags = []

for i in range(len(tags)):
    k = []
    for j in tags[i].find_all("a",class_= "tag"):
        k.append(j.text)
    total_tags.append("," .join(k))
print(total_tags)

