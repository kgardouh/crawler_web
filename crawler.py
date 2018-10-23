import requests
from bs4 import BeautifulSoup


def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('li', {'class':'mw-search-result'}):
            tet = link.get('Pont du Gard')
            print(link.find('a', {'class':''}).get('title'))

web(1,"https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Recherche&search=chien&fulltext=1&profile=default")