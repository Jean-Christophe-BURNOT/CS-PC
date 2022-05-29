#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 15:55:08 2022

@author: terramotu
Ceci est l'exercice 3 du TP sur les sémaphores
"""
import multiprocessing as mp
import os,random, signal, sys

#Fonction qu s'éxécute lors de l'arrêt
def fin(s, frame):
    print("Fin des messages !")
    sys.exit(0)

#Pour le fun même si dans la réalité c'est inutile ici
if __name__ == "__main__":
    #Création d'un sémaphore
    sem = mp.Semaphore()
    #création d'une liste commune de valeur maximum 10
    listeDeMessages = mp.Array("i", 10)
    #Creation de la redirection du signal de fin pour arrêter
    signal.signal(signal.SIGINT, fin)
    #Creation de 4 processus
    pid1 = os.fork()
    pid2 = os.fork()
   
    
    #processus P1
    if pid1==0:
        while True:
            message=random.randint(0,9)
        os.wait()
        
    #Processus P2
    if pid2==0:
        while True:
            message=random.randint(0.9)
        os.wait()
        
    #Processus C1
    if pid1==0 and pid2==0:
        os.wait()
        
    #Processus C2
    else:
        os.wait()