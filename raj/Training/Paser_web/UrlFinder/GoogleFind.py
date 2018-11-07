import bs4 as bs
import urllib.request

objet = "chat"
src = urllib.request.urlopen('https://www.google.com/search?q=' + objet)
soup = bs.BeautifulSoup(src, 'html.parser')

#syn = soup.find('div', {'class':'r'})
#print(syn.a.getText())
