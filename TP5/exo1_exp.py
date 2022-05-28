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
Somme = mp.value("i",0)
pid1 = os.fork()

#Processus P1
if pid1==0:
    i = 1
    SommeImpairs = 0
    while i <= N:
        SommeImpairs += liste[i]
        i = i+2
    Somme.value += SommeImpairs
    pid2 = os.fork()
    if pid2!=0:
        os.wait()
    if pid2==0:
        #Processus P2
        i = 0
        SommePairs = 0
        while i <= N:
            SommePairs += liste[i]
            i = i+2
        Somme.value += SommePairs
#faire attendre le père    
else:
    os.wait()
    
    