import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.maier.fr"
uri = "/occasions"

# récupere tous les liens 
# revoi un tableau de liens 
def getEndpoints(swoup):
    links = []

    lis = swoup.findAll("article",{"class":"product"})
    for li in lis:
        a = li.find("a")
        links.append(a["href"])
        print(a["href"])

    return links

#recupere les infos de la page 
def getInfoByPage(swoup):
    infosTriees = [swoup]
    return infosTriees

#connexion a la page 
def swoup(url, process):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        return process(soup)
    return []

#lis le fichier CSV
def fileReader(file):
    result = []
    with open(file, 'r', encoding="UTF8", newline="") as f:
        reader = csv.DictReader(f)
        for line in reader:
           result.append(line) 
    return result

#ecrit fichier csv
def fileWriter(file, fieldnames, data):
    with open(file, 'w', encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return fileReader(file)


data = fileReader("links.csv")

fields = ['test']
fileWriter('infos.csv', fields, data )

endpoints = swoup(url + uri,  getEndpoints)

""""
page = requests.get(url + uri)

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

"""