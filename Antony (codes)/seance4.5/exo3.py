import multiprocessing as mp
import os,sys,time,signal,random
N=10
s1= mp.Semaphore(1)

s2= mp.Semaphore(1)

queue1 = mp.Queue()
queue2 = mp.Queue()

pid=os.fork()
if pid != 0 : #Processus Père
    pid2=os.fork()

    if pid2 != 0 : #Processus Père
        pid3=os.fork()

        if pid3 != 0 : #Processus Père
            pid4=os.fork()

            if pid4 != 0 : #Processus Père
                os.wait()

            else:#Consomateur 1
                print("Consomateur 1")
                for i in range(N):
                    s1.acquire()
                    queue1.get()
                    s1.release()
                
                sys.exit(0)

        else:#Consomateur 2
            print("Consomateur 2")
            for i in range(N):
                s2.acquire()
                queue2.get()
                s1.release()

            sys.exit(0)

    else: #Producteur 1
        print("Producteur 1")
        for i in range(N):
            queue2.put(random.randint(0,1000))

    
        sys.exit(0)

else: #Producteur 2
    print("Producteur 2")
    for i in range(N):
        queue2.put(random.randint(0,1000))

    sys.exit(0)

sys.exit(0)