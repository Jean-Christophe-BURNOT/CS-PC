#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:23:16 2022

@author: terramotu
ce code est l'exercice 5 du TP2 de CS-PC
"""
import os, sys, time

#Nombre de processus à créer:
N = int(sys.argv[1])

#structure qui génère les processus:
for i in range(N):
    pid=os.fork()
    if pid!=0:
        #La première var retourne le process fils qui s'est terminé
        #La deuxième ligne donne le signal qui a mis fin au processus
        pid_fils, etat = os.wait()
        print(pid_fils, etat)

    if pid==0:
        myPID = os.getpid()
        myFatherPID = os.getppid()
        time.sleep(2*i)
        sys.exit(i)
    
        
