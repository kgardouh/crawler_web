# -*- coding: utf-8 -*-

import re,sys,urllib2,requests
import os
from bs4 import BeautifulSoup
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
french_stopwords = set(stopwords.words('french'))
english_stopwords = set(stopwords.words('english'))


if not (len(sys.argv) == 2):
    print "Usage: "+sys.argv[0]+" nb_documents_par_terme"
    exit(-1)

def research(keywords,langue):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #for start in range(0,10):
    url = "https://www.bing.com/search?&lr=lang_"+langue+"&num="+str(int(sys.argv[1]*4))+"&q="+keywords
    print("\n"+url+"\n")
    #print url
    page = opener.open(url)
    soup = BeautifulSoup(page,'lxml')
    res = list()
    for cite in soup.findAll('cite'):
        res.append(cite.text.encode('utf-8'))
    return res
    

def term_corpus_creator(term,file_propre,file_propre_mot,langue,file_statistique):
    link = research(term,langue)
    counter = 0
    file_propre.write("\n<terme>"+term+"</terme>\n".encode('utf-8'))
    file_propre_mot.write("\n<terme>"+term+"</terme>\n".encode('utf-8'))
    file_statistique.write("\n<terme>"+term+"</terme>\n".encode('utf-8'))
    for url in link:
        if(not (url.find("youtube") == -1)) or (not (url.find("amazon") == -1)):
            continue
        try: #test de l'url de la recherche google
            page = urllib2.urlopen(url)  #ouverture du lien dans page
        except:
            try:
                page = urllib2.urlopen('https://'+url)    
            except:
                try:
                    page = urllib2.urlopen('http://'+url)
                except :
                    print url+' ne peut être traité sous http/https'
                    continue
        
        occurence_term = 0
        nmb_mots = 0
        strpage=page.read() #lecture de la page html
        page.close()
        filename = "./corpus/documents_"+term+str(counter)+".txt"
        soup = BeautifulSoup(strpage,"lxml") #declaration de beautiful soup avec les données de la page html
        for script in soup(["script","style","comments","head","title","ol","il"]):  #extraction du bruit dans script
            script.extract()
        text_data = soup.get_text() #récupération de toutes les données texte
        if not(text_data.find("FTpanel") == -1):
            continue
        lines = (line.strip() for line in text_data.splitlines()) #retirer les retour chariot supplémentaire
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_data = '\n'.join(chunk for chunk in chunks if chunk)

       
        #********construction d'une liste qui contient tous les mots du site***********
        if re.search(term,text_data)==None :
        	continue
        text_propre=list()
        text_propre_2=list()
        liste_mots=list()
        text_propre.append("<p>")
        i=0;
        chaine_temp=""
        while i<len(text_data):
             if text_data[i]!="\n":
                 chaine_temp=chaine_temp+text_data[i]
                 i+=1
             else:
                text_propre.append(chaine_temp)
                if text_data[i]=="\n":
                    chaine_temp="</p>"
                    text_propre.append(chaine_temp)
                    chaine_temp="<p>"
                    text_propre.append(chaine_temp)
                chaine_temp=""
                i+=1

        tokenizer = TreebankWordTokenizer()
        tokens = tokenizer.tokenize(text_data)
        if langue=="fr":
        	tokens = [token for token in tokens if token.lower() not in french_stopwords]
        else:
        	tokens = [token for token in tokens if token.lower() not in english_stopwords]
     
        i=0
        liste_mots.append("<w>")
        while i<len(tokens):
             if (tokens[i]!="\n" and tokens[i]!=" " and tokens[i]!="," and tokens[i]!=";" and tokens[i]!="." and tokens[i]!="\"" and tokens[i]!= '?' and tokens[i]!="!" and tokens[i]!=":" and tokens[i]!="(" and tokens[i]!=")" and tokens[i]!="[" and tokens[i]!="]"):
                 liste_mots.append(tokens[i])
                 liste_mots.append("</w>\n")
                 liste_mots.append("<w>")
                 nmb_mots +=1
                 if tokens[i].find(term)!=-1:
                	occurence_term += 1
             i+=1
        liste_mots[len(liste_mots)-1]=""

        file_propre_mot.write("\n<url>"+url+"</url>\n".encode('utf-8'))
        file_propre_mot.write("\n<occurence_term>"+str(occurence_term)+"/"+str(nmb_mots)+"<occurence_term>\n\n".encode('utf-8'))
        for mot in liste_mots:
        	file_propre_mot.write(mot.encode('utf-8'))
        
        file_statistique.write("<url>"+url+"</url>\n".encode('utf-8'))
        file_statistique.write("<occurence_term>"+str(occurence_term)+"/"+str(nmb_mots)+"<occurence_term>\n".encode('utf-8'))

        #*******fin de la construction de la liste********** 

        #*******nettoyage du texte**************************
        i=0
        j=0
        debut_paragraphe=0 
        fin_paragraphe=0
        arret=0
        booleen=0
        while arret<len(text_propre):
        	while i<len(text_propre):
        		if text_propre[i]=="<p>":
        			debut_paragraphe=i
        			break
        		else:
        			i+=1
        	i=debut_paragraphe+1
        	while j<len(text_propre):
        		if text_propre[j]=="</p>":
        			fin_paragraphe=j
        			arret=fin_paragraphe
        			break
        		else:
        			j+=1
        	
        	j=fin_paragraphe+1
        	for mot in range(debut_paragraphe,fin_paragraphe):
        		if re.search(term,text_propre[mot]) :
        			booleen=1;
        			break
        	if booleen==1:
        		for mot in range(debut_paragraphe,fin_paragraphe+1):
        			text_propre_2.append(text_propre[mot])
        		if text_propre_2[len(text_propre_2)-1]!="\n":
        			text_propre_2.append("\n")
        	booleen=0
        	arret+=1
        #*******Fin du nettoyage du texte**************************
        file_propre.write("\n<url>"+url+"</url>\n".encode('utf-8'))
        file_propre.write("\n<occurence_term>"+str(occurence_term)+"/"+str(nmb_mots)+"<occurence_term>\n\n".encode('utf-8'))
        for mot in text_propre_2:
        	file_propre.write(mot.encode('utf-8')) #écrire le résultat dans un fichier

        

        file = open(filename,"w")
        file.write(text_data.encode('utf-8')) #écrire le résultat dans un fichier
        file.close()
        counter +=1
        print filename +" traite le lien "+url
        if(counter >= int(sys.argv[1])):
            print '\n\n'
            return

reload(sys)
sys.setdefaultencoding('utf-8')


if not os.path.isdir("./corpus"):
    os.makedirs("./corpus")

if not os.path.isdir("./corpus_propre_fr"):
    os.makedirs("./corpus_propre_fr")
term_fr="./corpus_propre_fr"

if not os.path.isdir("./corpus_propre_en"):
    os.makedirs("./corpus_propre_en")
term_en="./corpus_propre_en"

file_statistique = open("statistique.xml","w")
file_statistique.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode('utf-8'))
file_statistique.write("<langue>Français</langue>\n".encode('utf-8'))


langue="fr"
file_propre = open(term_fr+"/documents_phrases.xml","w")
file_propre_mot = open(term_fr+"/documents_mots.xml","w")
file_propre.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode('utf-8'))
file_propre_mot.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode('utf-8'))
for term in open("lexique.txt","r").read().split("\n"):
    if(len(term) <= 2 ):
        break
    print 'traitement du terme : '+term
    term_corpus_creator(term,file_propre,file_propre_mot,langue,file_statistique)
file_propre.close()
file_propre_mot.close()

file_statistique.write("\n<langue>Anglais</langue>\n".encode('utf-8'))
langue="en"
file_propre = open(term_en+"/documents_phrases.xml","w")
file_propre_mot = open(term_en+"/documents_mots.xml","w")
file_propre.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode('utf-8'))
file_propre_mot.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n".encode('utf-8'))
for term in open("lexique_en.txt","r").read().split("\n"):
    if(len(term) <= 2 ):
        break
    print 'traitement du terme : '+term
    term_corpus_creator(term,file_propre,file_propre_mot,langue,file_statistique)
file_propre.close()
file_propre_mot.close()
file_statistique.close()

print 'fin'
