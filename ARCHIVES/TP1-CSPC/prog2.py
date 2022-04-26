#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:38:05 2022

@author: raphael.guzelian
"""

import os,sys
N=int(sys.argv[1])
for process in range(2,N):
    pid=os.fork()
    if pid==0:
        print("Je suis le processus fils :",os.getpid())
        os._exit(0)
    else:
        print("Je suis le processus pere :",os.getpid())