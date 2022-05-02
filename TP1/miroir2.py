#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:30:45 2022

@author: jc.burnot
"""
import sys

#méthode un peu différente pour gérer le soucis utilisation de reversed
x=""
for i in sys.argv[1:]:
    for j in reversed(i):
        x+=j
    x+=" "
print(x)
    