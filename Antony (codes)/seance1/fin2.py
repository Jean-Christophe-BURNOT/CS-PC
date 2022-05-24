import os,sys
N=10
i=1
while i<=N :
    pid = os.fork()
    if pid==0:
        break
    i+=1
    if pid!=0:
        os.wait()

print('Je suis ' ,os.getpid(), 'et mon pere est', os.getppid() )