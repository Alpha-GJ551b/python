import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.maier.fr"
uri = "/occasions"
page = requests.get(url + uri)
tabLinks = []

# Voir le code html source
print(page.ok)
#print(page.content)

if page.ok:
    soup = BeautifulSoup(page.text,'html.parser')
    lisMain = soup.findAll("article",{"class":"product"})

    for li in lisMain:
        a = li.find("a")
        tabLinks.append(a["href"])
        #print(a)
        print(a["href"])
        page = requests.get(a["href"])
        soup = BeautifulSoup(page.text,'html.parser')

        header = soup.find("section",{"class":"product-informations"})
        name = header.find("h1").text
        marque = header.find("h2").text
        print (name," ",marque)

        refs = soup.findAll("span",{"class":"product-reference"})
        print (refs)
        price = soup.find("p",{"class":"product-sell-price"}).text
        print(price)

        section = soup.find("section",{"class":"product-features"})
        lis = section.findAll("li")
        for li in lis:
            p = li.find("p").text
            span = li.find("span").text
            print(p," ",span)
        #caracteristiques = soup.findAll("section",{"class":"product-features"})
        #print(len(caracteristiques))

    
    #print(ul)
    #print(lis)
    print(len(lis))   
    #print(soup)

