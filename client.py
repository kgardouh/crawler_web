import socket
import json


def openManifest():
	manifest="{}"
	with open("manifest.json", "r+") as f:
		manifest = json.load(f)
	return manifest;

class Client:

	def __init__(self,tcp= "0.0.0.0",port= 0000,buffer_size = 2048):
		self.tcp= tcp
		self.port= port
		self.buffer_size= buffer_size
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connectToServer(self):
		self.s.connect((self.tcp, self.port))
		data = self.s.recv(self.buffer_size)
		manifest = openManifest()
	#	print (data)
		self.s.send(json.dumps(manifest).encode('utf-8'))
		data = self.s.recv(self.buffer_size)
	#	print (data)
		return data

		
	




#TCP_IP = "37.59.57.203"

#TCP_PORT = 55555

#BUFFER_SIZE = 2048

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.connect((TCP_IP, TCP_PORT))

#data = s.recv(BUFFER_SIZE)

#print (data)

#manfiest="{}"

#with open("manifest.json", "r+") as f:
#    manfiest = json.load(f)
#s.send(json.dumps(manfiest).encode('utf-8'))

#data = s.recv(BUFFER_SIZE)

#print (data)

#s.close()



