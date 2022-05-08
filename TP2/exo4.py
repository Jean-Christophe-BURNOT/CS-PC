#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:23:15 2022

@author: terramotu
"""
"""
question1: ce qui suit la ligne 2 est exécuté par le fils car le fils
voit son PID nul
question2: Le programme est deterministe parce que les outputs seront toujours
le même, en effet les processus s'attendent l'un l'autre pour s'exécuter
question3: Si on enlève le wait ce n'est plus un programme déterministe puisque
en fait on ne sait plus à quel moment est-ce que les outputs vont se faire...
"""
import os, sys

n=0

for i in range(1,5) :
    fils_pid = os.fork()
    if (fils_pid > 0): 
        os.wait()
        n = i*2
        break
    
print("n = ", n)
sys.exit(0)
