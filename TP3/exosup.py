#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:22:47 2022

@author: terramotu
exercice supplémentaire sur les pipes
"""
import os, sys
import multiprocessing as mp
import numpy as np

dicoNotes = { "E1" : [10, 15, 20],
             "E2" : [12, 16, 15],
             "E3" : [18, 17, 20]
             }

dicoMoyenne = {}
for cle, valeur in dicoNotes.items():
    (dfr1, dfw1) = mp.Pipe()
    (dfr2, dfw2) = mp.Pipe()
    pid=os.fork()
    if pid == 0:
        #Envoi de la moyenne
        moyenne= sum(valeur)/len(valeur)
        dfr1.close()
        n = dfw1.send(moyenne)
        dfw1.close()
        #Envoi de l'élève (on pourrait le prendre dans le if ^^)
        dfr2.close()
        n = dfw2.send(cle)
        dfw2.close()
        sys.exit(0)
    else:
        os.wait()
        #recuperation de la moyenne
        dfw1.close()
        valeur = dfr1.recv()
        dfr1.close()
        #recuperation de l'élève
        dfw2.close()
        eleve = dfr2.recv()
        dfr2.close()
        #ajout au dictionnaire
        dicoMoyenne[eleve] = valeur
        
print(dicoMoyenne)
cle = []
valeur = []
for varcle, varvaleur in dicoMoyenne.items():
    cle.append(varcle)
    valeur.append(varvaleur)
maximum = max(valeur)
minimum = min(valeur)
posmax = np.where(np.array(valeur) == maximum)[0]
posmin = np.where(np.array(valeur) == minimum)[0]

print(maximum, minimum)
print("Bienjoué "+str(cle[int(posmax)])+" tu est le majorant avec {} de moyenne".format(maximum))


        
    

        
        