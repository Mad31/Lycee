# -*- coding: utf-8 -*-
# LFT Tananarive 2019
import socket
# Entrez ici l'adresse IP de votre chef de réseau
hote = "127.0.0.1"
port = 13800
msg_recu=""

connexion_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_serveur.connect((hote, port))
print("############# démarrage du client ############")
print("Connexion établie avec le serveur {} sur le port {}".format(hote,port))
# le code de connexion c'est le port de connexion utilisé par le client
bienvenue=connexion_serveur.recv(1024)
print(bienvenue.decode())
print("############# envoi du code de connexion #########")

msg_envoyer = ""
while 1 :
    msg_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux ou accentués
    msg_envoyer = msg_envoyer.encode()
    # On envoie le message
    connexion_serveur.send(msg_envoyer)
    if msg_envoyer==b'fin\r' :
        break
    msg_recu = connexion_serveur.recv(1024)
    print(hote," : ", msg_recu.decode()) # Là encore, peut planter s'il y a des accents
    if msg_recu==b'Erreur' :
        break

print("######## Transmission terminée ###########" )
connexion_serveur.close()
