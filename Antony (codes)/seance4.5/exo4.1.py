import multiprocessing as mp
import os,sys,time,signal
def rdv1():
    print("je suis 1") 

def rdv2():
    print("je suis 2") 

s1= mp.Semaphore(0)

s2= mp.Semaphore(0)



pid=os.fork()
if pid != 0 : #Processus Père

    pid2=os.fork()
    if pid2 != 0 : #Processus Père
        os.wait()

    else: #Processus 1
        print("Processus 1")

        s2.release()
        s1.acquire()

        rdv1()
        sys.exit(0)

else: #Processus 2 paire
    print("Processus 2")
    time.sleep(2)

    s1.release()
    s2.acquire()

    rdv2()
    sys.exit(0)

sys.exit(0)
