
# -*- coding: utf-8 -*-

import os,sys,time,signal
def envoi(signal,frame):
            print("wolooooooloooooooloooo")


def arreterProgramme(signal,frame) :

    print("ok")
    sys.exit(0)


N=10
pid = os.fork()

if pid != 0 : #Processus Père
    for i in range(N):

        time.sleep(1)
        print("wolooooooooolloooolololooooooooooooololoooolololooooooooooo")
        if i==3:
            os.kill(pid , signal.SIGUSR1)
        if i==5:
            os.kill(pid , signal.SIGUSR1)

    os.kill(pid , signal.SIGUSR2)
    sys.exit(0)

else:
    while True:
      
        signal.signal(signal.SIGUSR1,envoi )
        signal.signal(signal.SIGUSR2,arreterProgramme)
    