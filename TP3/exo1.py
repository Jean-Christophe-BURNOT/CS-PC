#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:32:58 2022

@author: terramotu
"""
import os, sys
import multiprocessing as mp

#%% Portion éxécuté par le père et le fils
x=41
(dfr, dfw) = mp.Pipe()
n = dfw.send(x)
#%% Portion éxécutée par le fils
if (os.fork()==0):
    x = dfr.recv()
    dfr.close()
    x+=1
    n = dfw.send(x)
    dfw.close()
    sys.exit(0)
os.wait()
dfw.close()
x = dfr.recv()
dfr.close()
print("La valeur de x est de {}".format(x))
sys.exit(0)