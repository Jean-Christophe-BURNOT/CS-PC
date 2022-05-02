#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:44:46 2022

@author: jc.burnot
"""
import os,sys
for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("Ok !")
    print("Bonjour !")
sys.exit(0)


