# -*- coding: utf-8 -*-
import os,sys,time,signal

def arreterProgramme(signal,frame) :

    print("C'est l'heure d’arrêt !")
    sys.exit(0)



N=10
print(os.getpid())
pid = os.fork()
if pid != 0 : #Processus Père
    signal.signal(signal.SIGINT,  signal.SIG_IGN)
    for i in range(N):

        time.sleep(1)
        print("wolooooooooolloooolololooooooooooooololoooolololooooooooooo")
        if i==3:
            print("3")
    sys.exit(0)
else:
    signal.signal(signal.SIGINT, arreterProgramme)
    while True:
        time.sleep(0.25)
        print("wolooooooloooooooloooo")