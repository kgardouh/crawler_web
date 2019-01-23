import bs4 as bs
import urllib.request
import requests
from bs4 import BeautifulSoup
from database import Base_donnee



class synonymes:
    def __init__(self):
        self.syn = ""
        self.SynWord = ""
        self.source = ""
        self.soup = ""
        self.db = Base_donnee()

        

    def test(self, mot):
       scr = urllib.request.urlopen("http://www.cnrtl.fr/definition/"+mot)
       soup = bs.BeautifulSoup(scr, 'lxml')

       syn = soup.find('span',{'class':'tlf_cdefinition'})
       return syn

    def RechercheSyn(self,mot):
      url = "http://www.cnrtl.fr/definition/"+mot
      code = requests.get(url)
      plain = code.text
      s = BeautifulSoup(plain, "html.parser")
      syn = s.find('span', {'class':'tlf_cdefinition'})
      if syn is None:
        self.db.insertion(mot,"synonyme:"+mot,url)
        return "null"
      else:
        self.db.insertion(mot,syn.text,url)
        return syn.text

    #  print(syn.text)
      