# -*- coding: utf-8 -*-
import socket

hote = ''
port = 13800

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
code=False

# AF_INET : protocole IP SOCK-STREAM : procotole TCP
connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.bind((hote, port))
connexion_serveur.listen(5)
print("############ Démarrage du serveur ###############")
print("Le serveur {} à l'adresse {} écoute à présent sur le port {}".format(hostname,ip,port))

connexion_client, infos_connexion = connexion_serveur.accept()
print("une connection en provenance de ",infos_connexion[0], "sur le port", infos_connexion[1])
bienvenue="Connection etablie avec le serveur CIA".encode()
connexion_client.send(bienvenue)

msg_recu = ""
msg_recu = connexion_client.recv(1024)
code_envoye=msg_recu.decode()
if infos_connexion[1]==int(code_envoye):
    code=True
    msg_envoye="code accepté..."
    connexion_client.send(msg_envoye.encode())
    print("le code a été accepté, en attente de message...")
else :
    msg_envoye="Erreur"
    connexion_client.send(msg_envoye.encode())

while code==True :
    msg_recu = connexion_client.recv(1024)
    print(infos_connexion[0]," : ", msg_recu.decode())
    if msg_recu==b'fin\r' :
        break
    msg_envoye = input("> ")
    connexion_client.send(msg_envoye.encode())

print("############### transmission terminée ############")
connexion_client.close()
connexion_serveur.close()
