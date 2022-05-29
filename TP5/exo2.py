#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:31:42 2022

@author: terramotu
Ceci est l'exercice 2 sur les sémaphores
"""
import os , sys, time, signal
import multiprocessing as mp

Somme = mp.Value('i', 0)
listeNumber = [4, 6, 2, 1, 9, 7]
N = len(listeNumber)
S1 = mp.Semaphore(0)
S2 = mp.Semaphore(0)
S = mp.Semaphore(1)

def SommeImp(listeNumber, N):
    SommeImpairs = 0
    i = 1
    
    while i<= N :
        S1.release()
        S2.acquire()
        SommeImpairs = SommeImpairs + listeNumber[i]
        i += 2
        print('Compteur Impaire =', i)
    S.acquire()    
    Somme.value += SommeImpairs
    S.release()
    print(Somme.value)
    S.acquire()
    
    
    
def SommePai(listeNumber, N):
    SommePairs = 0
    i = 0
    
    while i< N :
        S1.acquire()
        SommePairs = SommePairs + listeNumber[i]
        i += 2
        print('Compteur Paire =', i)
        S2.release()
    S.acquire()
    Somme.value += SommePairs
    print(Somme.value)
    S.release()
    
    
p1 = mp.Process(target = SommeImp , args = (listeNumber, N, ))
p2 = mp.Process(target = SommePai , args = (listeNumber, N, ))

p1.start()
p2.start()
p1.join()
p2.join()
print(Somme.value)
sys.exit(0)