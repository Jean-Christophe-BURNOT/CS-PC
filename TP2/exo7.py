#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:56:38 2022

@author: terramotu
ceci est l'exercice 7
"""
import sys, os

N = 3
for i in range(N) :
#__________début des ajouts_________
    pid1 = os.fork()
    if pid1!=0:
        os.wait()
        
  
        
    
# __________fin des ajouts__________
    print("Bonjour")
    sys.exit(0)
