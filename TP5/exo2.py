#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:31:42 2022

@author: terramotu
Ceci est l'exercice 2 sur les sémaphores
"""
import os, sys, time
import multiprocessing as mp

somme = mp.Value("i",0)
sem = mp.Semaphore(0)
pid = os.fork()
n1 = 0
n2 = 0

#processus fils
if pid==0:
    for i in range(4):
        n1 += i
        print("Je somme les indices")
        time.sleep(1)
    somme.value+=n1
    print("Le fils a terminé")
    sem.release()
    sys.exit(0)

else:
    for i in range(4):
        n1 += i
        print("Je somme mais je suis le second")
        time.sleep(1)
    sem.acquire()
    somme.value+=n1
    print("Le père a terminé")
    sem.release()
    
print(somme.value)

"""
On est plus optimisé qu'un os.wait car les deux process font le calcul
simultanément et c'est l'incrémentation du compteur qui est sécurisé par le
sémaphore
"""