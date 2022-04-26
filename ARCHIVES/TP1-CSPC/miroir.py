#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:47:10 2022

@author: raphael.guzelian
"""
import sys

x=""
for i in reversed(sys.argv[1]):
    x+=i
print(x)
    
