#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:48:29 2022

@author: terramotu
exercice 3 du TP sur les signaux
"""
import signal,time, sys

global fin
fin=False

def arreterProgramme(signal,frame) :
    global fin 
    fin=True

signal.signal(signal.SIGINT, arreterProgramme)



def boucle():
    global fin 

    while not(fin) :
        time.sleep(2)
        print("je boucle")

boucle()
sys.exit(0)
    

