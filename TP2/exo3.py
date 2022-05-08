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

while type!=1 and type!=2:
    type=int(
        input("Entrez le type d'exécution:1 pour serie 2 pour parrallèle:\n"))

commandes = sys.argv[1:]
if type==1:
    for cmd in commandes:
        try:
            os.execlp(cmd, cmd)
        except:
            print("echec de execlp")
            
    
elif type==2:
    for cmd in commandes:
        pid=os.fork()
        if pid==0:
            try:
                os.execlp(cmd, cmd)
            except:
                print("echec de execlp")
                sys.exit(2)

"""
portion de code qui pourraiit permettre de

if len(liste)>0:
    print("Commande non exécutées=", liste)
sys.exit(0)
"""