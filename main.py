from Client import Client
from crawler import Crawler
from database import Base_donnee


TCP_IP = "node.nicopr.fr"
TCP_PORT = 55555
BUFFER_SIZE = 2048



#client = Client(TCP_IP,TCP_PORT,BUFFER_SIZE)
#data = client.connectToServer()




Crawler().web(1,"https://fr.wiktionary.org/wiki/","arbre")
#print(data)

