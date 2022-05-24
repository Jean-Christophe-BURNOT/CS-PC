# -*- coding: utf-8 -*-
import os,sys

piper1,pipew1 = os.pipe()
piper2,pipew2 = os.pipe()
fichier1=os.open("text.txt",os.O_RDWR )
fichier2=os.open("fichier.txt",os.O_RDWR )

pid=os.fork()
 
if pid==0:
    os.close(piper1)
    os.close(piper2)
    os.close(pipew2)



    os.dup2(fichier1, 0)
    os.dup2(pipew1, 1)

    os.close(pipew1)

    
    os.execlp("sort","sort")

else:
    os.close(pipew1) 

    pid=os.fork()

    if pid==0:
    
        os.dup2(piper1, 0)

        os.close(piper1)

        os.close(piper2)
        os.dup2(pipew2, 1)
        os.close(pipew2)
        
        os.execlp("grep","grep","toto")
        
    else:
        os.close(piper1)

        os.close(pipew2)
        os.dup2(piper2, 0)
        os.dup2(fichier2, 1)
        os.close(piper2)

        os.execlp("tail","tail","-n","5")
            