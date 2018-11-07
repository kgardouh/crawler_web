import bs4 as bs
import urllib.request

class synonymes:
    def __init__(self):
        self.syn = ""
        self.SynWord = ""
        self.source = ""
        self.soup = ""
        

    def RechercheSyn(self, mot):
       scr = urllib.request.urlopen("http://www.cnrtl.fr/definition/"+mot)
       soup = bs.BeautifulSoup(scr, 'lxml')

       syn = soup.find('span',{'class':'tlf_cdefinition'})
       #print(syn.text)
       return syn.text 
