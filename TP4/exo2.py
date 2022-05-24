#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:27:49 2022

@author: terramotu
"""
import sys, signal, time

#Fonction executée lors de la reception du signal
def fonc(s, frame):
    print("\n le programme a recu un signal !")
    sys.exit(0)

#gère le comportement du signal
signal.signal(signal.SIGINT , signal.SIG_IGN)

#boucle infinie
while True:
    print("Ceci est une boucle infinie interruptible")
    time.sleep(1)
    

