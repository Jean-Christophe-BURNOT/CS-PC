import multiprocessing as mp
import os,sys,time,signal


pid=os.fork()
if pid != 0 : #Processus Père

    pid2=os.fork()
    if pid2 != 0 : #Processus Père
        os.wait()
    else: #Processus 1
        print("Processus 1")
        sys.exit(0)

else: #Processus 2 paire
    print("Processus 2")
    sys.exit(0)

sys.exit(0)