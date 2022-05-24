import os,sys
N=10
i=1
while os.fork()==0 and i<=N :
    print('Je suis ' ,os.getpid(), 'et mon pere est', os.getppid() )
    i+=1
if i<=N:
    os.wait()