#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:38:18 2022

@author: terramotu
Ceci est le code de l'exercice 3 du TP de CS-PC
"""
import os, sys


if len(sys.argv) <2:
    print("Préciser les programmes à éxécuter en ligne de commande")
    sys.exit(1)
typ=0
while typ!=1 and typ!=2:
    typ=int(input("Entrez le type d'exécution:1 pour serie 2 pour parrallèle:\n"))
commandes = sys.argv[1:]



#path=[]



"""
Ce processus permet de connaitre la localisation des programmes
"""
"""
#Permet de trouver les localisations des commandes
for cmd in commandes:
    pid = os.fork()
    if pid == 0:   
        try:
            os.execlp("/usr/bin/which", "which", cmd)
        except:
            print("echec de la recherche de la commande")
            sys.exit(2)
        os.wait()
        
    p,s = os.wait()


p,s = os.wait()
if os.WIFEXITED(s)==True: #Si le processus s'est terminé sans erreurs
    print("Le chemin de la commande à été trouvé:", p)
    
    if os.WEXITSTATUS(s)==3:
        path.append(cmd)

"""

#Permet de gérer les éventuels paramètres
for i,cmd in enumerate(commandes):
    if " " in cmd:
        commandes[i] = cmd.split(" ")
print(commandes)
        

#serie
if typ==1:
        pid = os.fork()     
        if pid == 0:   
            try:
                #Quand la première partie sera fonctionnelle changer le premier argument
                print("<",cmd[0], cmd[0], cmd[1:],">")
                input("?")
                os.execv(cmd[0], cmd[0], cmd[1:])
            except:
                print("echec de execlp", cmd)
                sys.exit(2)
        os.wait()
        sys.exit(2)
                
#parrallèle
elif typ==2:
    for cmd in commandes:
        pid=os.fork()
        if pid==0:
            try:
                #Meme commentaire ici
                os.execv(cmd[0], cmd[0], cmd[1:])
            except:
                print("echec de execlp")
                #sys.exit(3)

"""
portion de code qui pourraiit permettre de

if len(liste)>0:
    print("Commande non exécutées=", liste)
sys.exit(0)
"""