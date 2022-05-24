# -*- coding: utf-8 -*-

import os,sys,time,signal

def arreterProgramme(signal,frame) :

    print("trop lent")
    sys.exit(0)

N=10
pid = os.fork()
if pid != 0 : #Processus Père

    time.sleep(5)


    os.kill(pid,signal.SIGINT)

    print("GG t'est trop rapide")
    print("relance le jeu")

    sys.exit(0)

else:

    signal.signal(signal.SIGINT, arreterProgramme)

    print("il faut entrer un entier ")

    fin=True

    while fin:

        try:
            int(input("Svp un entier  :"))
            fin=False

        except:
            print("c'est pas bon")

        

    sys.exit(0)