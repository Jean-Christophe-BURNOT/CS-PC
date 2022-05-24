
import multiprocessing as mp
import os,sys,time,signal,random


N=10
s1= mp.Semaphore(0)

s2= mp.Semaphore(0)
s3= mp.Semaphore(0)

def rdv1():
    print("je suis 1")

def rdv2():
    print("je suis 2")

def rdv3():
    print("je suis 3")

pid=os.fork()

if pid != 0 : #Processus Père
    pid2=os.fork()

    if pid2 != 0 : #Processus Père
        pid3=os.fork()

        if pid3 != 0 : #Processus Père
           os.wait()

            

        else:#Programme 1
            print("Programme 1")
            s2.release()
            s3.release()
            s1.acquire()
            s1.acquire()
            rdv1()


            sys.exit(0)

    else: #Programme 2
        print("Programme 2")
        s1.release()
        s2.acquire()
        rdv2()

    
        sys.exit(0)

else: #Programme 3
    print("Programme 1")
    s1.release()
    s3.acquire()
    rdv3()
    sys.exit(0)
sys.exit(0)