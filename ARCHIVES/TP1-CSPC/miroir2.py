#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:51:43 2022

@author: raphael.guzelian
"""

import sys

x=""
for i in sys.argv[1:]:
    for j in reversed(i):
        x+=j
    x+=" "
print(x)