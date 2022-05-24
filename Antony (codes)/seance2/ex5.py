
import os,sys,time

N=int(sys.argv[1])

for i in range(1,N+1):
    pid=os.fork()
    if pid==0:
        print('Mon ID est' ,os.getpid(),"L'ID de mon pere est : ",os.getppid())
        time.sleep(2*i)
        sys.exit(i)

for i in range(1,N+1):
     pid_fils, etat = os.wait() 
     print('Mon fils : ',pid_fils, 'à fini de cette façon', etat)