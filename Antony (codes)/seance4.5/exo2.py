import multiprocessing as mp
import os,sys,time,signal

s= mp.Semaphore(0)

pid=os.fork()
if pid != 0 : #Processus Père

    pid2=os.fork()
    if pid2 != 0 : #Processus Père
        os.wait()
    else: #Processus 1
        print("Processus 1")
        print("je fait la tache 1")
        s.release()
        sys.exit(0)

else: #Processus 2 paire
    print("Processus 2")
    s.acquire()
    print("je fait la tache 2")
    s.release()
    sys.exit(0)

sys.exit(0)