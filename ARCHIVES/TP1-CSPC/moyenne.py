#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:08:19 2022

@author: raphael.guzelian
"""

import sys
x=0
a=0
if len(sys.argv[1:])<=1:
    print("Aucune moyenne à calculer")
else:
    for note in sys.argv[1:]:
        if float(note)<0 or float(note)>20:
            print("Note(s) non valide(s)")
            a+=1
        else:
            x+=float(note)
            x2=x/len(sys.argv[1:])
            moy=round(x2,2)
    if a==0:
        print("Moyenne = ",moy)
                
            

