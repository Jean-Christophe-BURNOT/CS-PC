import multiprocessing as mp
import os,sys,time,signal

L=[0,1,2,3,4,5,6,7,8,9,10]
N=len(L)

Somme=mp.Value('i',0)

pid=os.fork()
if pid != 0 : #Processus Père

    pid2=os.fork()
    if pid2 != 0 : #Processus Père
        os.wait()
    else: #Processus 1 impaire
        i=1
        SommeImpairs = 0

        while i <= (N-1):
            print("i =" ,i)
            SommeImpairs = SommeImpairs + L[i]
            i = i + 2
        
        Somme.value =  Somme.value + SommeImpairs
        print("sommeimpaire =",Somme.value)
        sys.exit(0)

else: #Processus 2 paire
    i=0
    Sommepairs = 0

    while i <= (N-1):
        print("i =" ,i)

        Sommepairs = Sommepairs + L[i]
        i = i + 2
    
    Somme.value =  Somme.value+Sommepairs

    print( "sommepaire =",Somme.value)
    sys.exit(0)


print("sommetotal =",Somme.value)
sys.exit(0)