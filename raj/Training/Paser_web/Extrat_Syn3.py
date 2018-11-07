import bs4 as bs
import urllib.request

scr = urllib.request.urlopen("http://www.cnrtl.fr/definition/chat")
soup = bs.BeautifulSoup(scr, 'lxml')

syn = soup.find('span',{'class':'tlf_cdefinition'})
print(syn.text)
