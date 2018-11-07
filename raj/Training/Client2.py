import socket

hote = "37.59.57.203"
port = 55555
msg=b'Projet Crawler'

to_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
to_serveur.connect((hote, port))

to_serveur.send(msg)
msg_recu = to_serveur.recv(1024)
print(msg_recu) # Là encore, peut planter s'il y a des accents

manifest ={}
to_serveur.send(manifest)

to_serveur.close()
