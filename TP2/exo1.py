# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Ce programme est l'exercice 1 du TP2'
"""
import os, sys

pid=os.fork()

if pid==0:
    print("Je suis le fils")
    os.execlp("python3","python3","test.py")
    
else:
    print("je suis le père")

