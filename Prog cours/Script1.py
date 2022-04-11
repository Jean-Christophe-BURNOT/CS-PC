#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:14:30 2022

@author: terramotu
Ce programme est le premier programme de type partiel du cours de CS-PC
"""
import os, sys

if len(sys.argv) <2:
    print("Préciser les programmes à éxécuter en ligne de commande")
    sys.exit(1) #attribue la valeur 1 à cet exit
print(sys.argv)
liste =[]

for cmd in sys.argv[1:]:
    pid = os.fork()
    
    #Le try/except permet de tester sans bloquer en cas d'erreur
    if pid == 0:       
        try:
            os.execlp(cmd, cmd)
        except:
            print("echec de execlp")
            sys.exit(3)
            
    p,s = os.wait()
    if os.WIFEXITED(s)==True: #Si le processus s'est terminé sans erreurs
        print("Terminaison normale du processus fils:", p)
        
        if os.WEXITSTATUS(s)==3:
            liste.append(cmd)
            
if len(liste)>0:
    print("Commande non exécutées=", liste)
sys.exit(0)
