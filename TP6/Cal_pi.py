#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 13:44:09 2022

@author: Maximilien Remillieux et Jean-christophe Burnot
(code couresc Hippique voir chez Jean-christophe)
"""

import random, time, sys
import multiprocessing as mp
# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)

def frequence_de_hits_pour_n_essais(s,nb_iteration,nb_hits):
    count = 0
    for i in range(nb_iteration):
        x = random.random() 
        y = random.random()
# si le point est dans l’unit circle
        if x * x + y * y <= 1: 
            count += 1
    s.acquire()
    nb_hits.value += count
    s.release()
    return 


if __name__ == "__main__":
    # Nombre d’essai pour l’estimation
    nb_total_iteration = 10000000
    # #nimbre de processeur
    nb_hits = mp.Value('f', 0.0)
    #nombre pros
    nb_pros = 8
    debut = time.time()
    sem = mp.Semaphore(1)
    list_pros = []
    for i in range(nb_pros):
        pros = mp.Process(target = frequence_de_hits_pour_n_essais, args = (sem, nb_total_iteration // nb_pros, nb_hits,))
        list_pros.append(pros)
        pros.start()
    for p in list_pros:
        p.join()
    fin = time.time()
  
#calcule de pi avec 8bpross
    print("Valeur estimée Pi par la méthode Mono−Processus 8 pros : ", 4 * nb_hits.value / nb_total_iteration, "temps 1:", fin - debut)

#calcule de pi avec 1 pross
    debut = time.time()
    frequence_de_hits_pour_n_essais(sem, nb_total_iteration, nb_hits)
    fin = time.time()
    print( "temps 2:", fin - debut)
    sys.exit()

