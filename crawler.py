import requests
from bs4 import BeautifulSoup
from synonymes import *


class Crawler:


	def web(self,page,WebUrl,mot):
	    if(page>0):
	        url = WebUrl
	        print("Mot: "+mot)
	        code = requests.get("http://www.dictionnaire-synonymes.com/synonyme.php?mot="+mot+"&OK=OK")
	        plain = code.text
	        s = BeautifulSoup(plain, "html.parser")
	        syn = synonymes()
	        definition = syn.RechercheSyn(mot)
	        print("\nLa définition trouvé est: " + definition)
	        for link in s.findAll('a', {'class':'lien3'}):
	            #mot = link.find('a', {'class':'lien3'})
	            mot = str(link.text)
	            if mot!="[informal]" and mot:
	            	print("Synonymes: "+ str(link.text))
	           







