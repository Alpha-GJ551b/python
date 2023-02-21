import requests
from bs4 import BeautifulSoup

url = "https://www.maier.fr"
uri = "/occasions"
page = requests.get(url + uri)

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
    
    #print(ul)
    #print(lis)
    print(len(lis))
    #print(soup)

