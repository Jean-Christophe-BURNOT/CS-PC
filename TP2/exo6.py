#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:20:07 2022

@author: terramotu
"""

import os, time, random, sys
for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(0,4)
time.sleep(delai)
print("Mon nom est " + chr(ord('A')+i) +" j ai dormi "+
str(delai) + " secondes")
sys.exit(0)
