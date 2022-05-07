#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:25:09 2022

@author: terramotu
"""
import os,sys

for i in range(3):
    os.fork()
    print("i :",i,"je suis le processus :",os.getpid(),"mon pere est :",os.getppid())
sys.exit(0)

#le fils crée à la boucle 0 crée les fils à la boucle 1 et 2.
#donc les fils héritent de la boucle du père sans que les fils n'est de boucle dans leur code