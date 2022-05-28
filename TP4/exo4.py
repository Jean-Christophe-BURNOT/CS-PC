#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 20:12:22 2022

@author: terramotu
exercice 4 du TP sur les signaux
"""
import os, time, sys
from signal import SIGKILL

N = 5
pid = os.fork()

#Boucle du processus fils
if pid==0:
    while True:
        time.sleep(1)
        print("Je suis le fils qui est en train de boucler")
    #Le sys exit est inutile la sortie se fait par un signal mais je trouve ça plus propre...
    sys.exit(0)
        
#Boucle du processus père
else:
    for i in range(N):
        time.sleep(1)
        print("Et moi je suis le père qui boucle N fois")
    #Envoit le signal "sigkill" au PID
    os.kill(pid, SIGKILL)

