#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:48:29 2022

@author: terramotu
exercice 3 du TP sur les signaux
"""
import signal, time

#Fonction executée lors de la reception du signal
def fonc(s, frame):
    print("\n le programme a recu un signal !")
    fin = True
    return fin

#gère le comportement du signal
signal.signal(2, fonc)

#boucle infinie
global fin
fin = False
while not fin:
    print("Ceci est une boucle infinie")
    time.sleep(1)
    if fin:
        print("salut mon pote !")
        break
    

