#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 16:26:39 2022

@author: jc.burnot
"""
a = ["ps -aux", "ls -la"]
for i, cmd in enumerate(a):
    if " " in cmd:
        truc = a[i].split(" ")
    print(truc)