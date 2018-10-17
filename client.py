import socket
import json


TCP_IP = "37.59.57.203"

TCP_PORT = 55555

BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE)

print (data)

manfiest="{}"

with open("manifest.json", "r+") as f:
    manfiest = json.load(f)
s.send(json.dumps(manfiest).encode('utf-8'))

data = s.recv(BUFFER_SIZE)

print (data)

s.close()



