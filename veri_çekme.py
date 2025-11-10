import requests
from bs4 import BeautifulSoup

url = requests.get("https://emektra.com/")

soup = BeautifulSoup(url.content,"html.parser")

yazdır = soup.find_all("p")

for i in yazdır:
    print(i.text)