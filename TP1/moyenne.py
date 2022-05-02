#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:20:47 2022

@author: jc.burnot
"""
import sys

x=0
listeNonValide = []
if len(sys.argv[1:])<=1:
    print("Aucune moyenne à calculer")
    
else:
    for note in sys.argv[1:]:
        if float(note)<0 or float(note)>20:
            listeNonValide.append(float(note))
            print("Note(s) non valide(s)", listeNonValide)
            
        else:
            x+=float(note)
            
    x=x/len(sys.argv[1:])
    moy=round(x,2)
    print("Moyenne = ",moy)