import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.maier.fr"
uri = "/occasions"
page = requests.get(url + uri)
tab = []

# Voir le code html source
print(page.ok)
#print(page.content)

if page.ok:
    soup = BeautifulSoup(page.text,'html.parser')
    lis = soup.findAll("article",{"class":"product"})

    for li in lis:
        a = li.find("a")
        #print(a)
        print(a["href"])
        page = requests.get(a["href"])
        soup = BeautifulSoup(page.text,'html.parser')
        price = soup.find("p",{"class":"product-sell-price"}).text
        caracteristiques = soup.findAll("section",{"class":"product-features"})
        print(price)
        print(len(caracteristiques))

    
    #print(ul)
    #print(lis)
    print(len(lis))   
    #print(soup)

