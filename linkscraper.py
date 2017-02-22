import urllib.request
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=memes"

response = urllib.request.urlopen(url)

html = response.read()
soup = BeautifulSoup(html,'html.parser')
tag = soup.find()
print(tag.get_text())
