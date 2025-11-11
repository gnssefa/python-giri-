import requests
from bs4 import BeautifulSoup

url = requests.get("https://covid19.saglik.gov.tr/")
if url.status_code == 200:
    print("Siteden Veri Çekilebilir")
else:
    print("SİTE VERİ ÇEKİMİNE KAPALI")

soup = BeautifulSoup(url.content,"html.parser")



div =  soup.find("post-data-harita",{"class":" col-xl-3 col-lg-12 col-md-12 "})
print(div)