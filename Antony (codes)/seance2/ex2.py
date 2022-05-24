import os,sys

for i in range(3):
    pid = os.fork()
    print('i vaut: ',i,' je suis le processus :',os.getpid(),'mon pere est :',os.getppid(),'retour : ',pid)

sys.exit(0)

#  cf feuille 
#  
