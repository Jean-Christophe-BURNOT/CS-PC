#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:07:36 2022

@author: terramotu
exo1 su TP sur les sémaphores
"""
import os
import multiprocessing as mp

liste = [1,2,3,4,5,69,180]
N=len(liste)
Somme = mp.Value("i",0)
sem=mp.Semaphore(1) #Création du sémaphore
pid1 = os.fork()


#Processus P1
if pid1==0:
    i = 1
    SommeImpairs = 0
    while i <= N-1:
        SommeImpairs += liste[i]
        i = i+2
    #calcul risqué
    sem.acquire()
    Somme.value += SommeImpairs
    sem.release()
    print("la somme impaire est:", SommeImpairs)
    
else:
    #Processus P2
    i = 0
    SommePairs = 0
    while i <= N:
        SommePairs += liste[i]
        i = i+2
    #calcul risqué   
    sem.acquire()
    Somme.value += SommePairs
    sem.release()
    print("la somme paire est:", SommePairs)
    

print("Valeur de la somme finale est:", Somme.value)