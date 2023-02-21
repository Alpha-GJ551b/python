import requests
from bs4 import BeautifulSoup

url = "https://www.lego.com/fr-fr"
uri = ""
page = requests.get(url + uri)

# Voir le code html source
print(page.ok)
#print(page.content)

if page.ok:
    soup = BeautifulSoup(page.text,'html.parser')
    ul = soup.find("ul")
    uls = soup.findAll("ul",{"class":"results"})
    lis = ul.findAll("li")
    for li in lis:
        a =li.find("a")
        print(a)
        print(url + a["href"])
        
    print(lis)
    print(len(uls))
    print(soup)




