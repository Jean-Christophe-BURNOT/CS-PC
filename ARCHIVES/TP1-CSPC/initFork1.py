#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:44:41 2022

@author: raphael.guzelian
"""

import os,sys
N = 10
i=1
while os.fork()==0 and i<=N :
    i += 1
print(i)
sys.exit(0)

#Ce programme crée des fils tant que i est inférieur ou égal à N qui vaut 10,
#quand i vaut 11, on ne crée plus de fils