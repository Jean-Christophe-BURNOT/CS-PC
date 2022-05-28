#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:52:06 2022

@author: terramotu
ceci est le code de l'exercice 5 du TP sur les signaux
"""
import os, time, sys, signal

def stop(signal,frame):
    print("c'est fini")
    sys.exit(0)
    
N = 5
pid = os.fork()
#Boucle du processus fils
if pid==0:
    while True:
        time.sleep(1)
        print("Je suis le fils qui est en train de boucler")
        #permet de dérouter le fils
        signal.signal(signal.SIGINT, stop)
    #Le sys exit est inutile la sortie se fait par un signal mais je trouve ça plus propre...
    sys.exit(0)
        
#Boucle du processus père
else:
    for i in range(N):
        time.sleep(1)
        print("Et moi je suis le père qui boucle N fois")
    os.kill(pid, signal.SIGINT)
    