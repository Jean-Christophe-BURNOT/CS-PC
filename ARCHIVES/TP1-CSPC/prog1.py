#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:14:04 2022

@author: raphael.guzelian
"""

import os,sys
N=int(sys.argv[1])
for process in range(2,N):
    pid=os.fork()
    if pid==0:
        print("Je suis le processus fils :",os.getpid())
    else:
        print("Je suis le processus pere :",os.getpid())
        os._exit(0)