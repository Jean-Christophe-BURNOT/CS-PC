#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:27:34 2022

@author: raphael.guzelian
"""

import os,sys

pid=os.fork()
if pid==0:
    print("Je suis le fils")
    os.execlp("python3","python3","test.py")
else:
    print("Je suis le père")