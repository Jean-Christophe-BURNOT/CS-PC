#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:40:13 2022

@author: terramotu
1er exercice du TP de CS-PC
"""
import sys
print("Nom du programme : ", sys.argv[0])
print("Nombre d’arguments : ", len(sys.argv)-1)
print("Les arguments sont : ")
for arg in sys.argv[1:] :
    print(arg)
