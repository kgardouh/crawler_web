import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://www.cnrtl.fr/lexicographie/chien')
soup = bs.BeautifulSoup(source, 'lxml')

for span in soup.find_all('span', class_='tlf_csynonime'):
   print(span.text)
