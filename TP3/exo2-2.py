#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:59:53 2022

@author: terramotu (Jean-Christophe)
Exercice 2 partie 1 du poly sur les Pipes
"""
"""
commande à exécuter:
sort < fichier | grep chaine | tail –n 5 > sortie
0: entrée
1: sortie
le pipe est bloquant pas besoin de wait() et exit()
"""


import os, sys

(dfr1, dfw1) = os.pipe()
(dfr2,dfw2) = os.pipe()
#text est un descripteur de fichier
textinput = os.open("exotext.txt", os.O_RDWR)
#ouvre le fichier avec les droits de création, lecture et écriture du fichier ("|"=> et logique)
textoutput = os.open("exotextsortie.txt", os.O_RDWR|os.O_CREAT)

pid = os.fork()

if pid==0:
    #redirection des entrées et des sorties
    os.dup2(textinput, 0)
    os.dup2(dfw1, 1)
    #fermeture des descripteurs
    os.close(dfr1)
    os.close(dfw1)
    os.close(dfr2)
    os.close(dfw2)
    #exécution du code voulu
    os.execlp("sort", "sort")
    
else:
    pid2 = os.fork()
    if pid2==0:
        os.dup2(dfr1, 0)
        os.dup2(dfw2, 1)
        os.close(dfr1)
        os.close(dfw1)
        os.close(dfr2)
        os.close(dfw2)
        os.execlp("grep", "grep", "in")
    
    else:
        os.dup2(dfr2, 0)
        os.dup2(textoutput, 1)
        os.close(dfr1)
        os.close(dfw1)
        os.close(dfr2)
        os.close(dfw2)
        os.execlp("tail", "tail", "-n 5")

os.close(textinput)
os.close(textoutput)
sys.exit(0)