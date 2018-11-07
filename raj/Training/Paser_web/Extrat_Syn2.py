import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.cnrtl.fr/lexicographie/chien')
soup = bs.BeautifulSoup(source, 'lxml')

syn = soup.find('span',{'class':'tlf_csynonime'})
SynWord = syn.i.getText()

print("\nLe synonime de chien est: " + SynWord)
