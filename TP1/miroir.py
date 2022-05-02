#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:45:31 2022

@author: jc.burnot
2em exercice du TP de CS-PC
"""
import sys
motmiroir = ""

#j'ai décidé de faire une boucle for inversée...
for i in range(len(sys.argv[1])-1,0-1,-1):
    motmiroir += sys.argv[1][i]
print(motmiroir)
    

