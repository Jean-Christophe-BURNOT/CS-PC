# -*- coding: utf-8 -*-

import os,sys,random

piper1,pipew1 = os.pipe()
piper2,pipew2 = os.pipe()
piper3,pipew3 = os.pipe()
piper4,pipew4 = os.pipe()

N=4

pid=os.fork()
 
if pid==0:
    #generator
    
    os.close(piper1)
    os.close(piper2)
    os.close(pipew3)
    os.close(pipew4)

    for i in range(N):
        random.seed()
        var = random.randint(0,1000)


        lb = var.to_bytes(4,byteorder="little",signed = True)

        if var%2==0:
            os.write(pipew1,lb)
   
        else:
            os.write(pipew2,lb)

  
    var = -1

    lb = var.to_bytes(4,byteorder="little",signed = True)

    os.write(pipew1,lb)
   

    os.write(pipew2,lb)
  

    os.close(pipew1)
    os.close(pipew2)

    lb = os.read(piper3,4)
    somme1 = int.from_bytes(lb,byteorder="little",signed=True)
   

    os.close(piper3)

    lb = os.read(piper4,4)
    somme2 = int.from_bytes(lb,byteorder="little",signed=True)

     
    os.close(piper4)

    somme=somme1 +somme2

    print("La somme ",somme)


    sys.exit(0)
else:
    somme=0
    pid=os.fork()
    if pid==0:
        #paire
        os.close(pipew1)
        os.close(piper2)
        os.close(pipew2)
        os.close(piper3)
        os.close(piper4)
        os.close(pipew4)
        var=0
        while var != -1:
            somme+=var
            lb = os.read(piper1,4)
            var  = int.from_bytes(lb,byteorder="little",signed=True)
            
        os.close(piper1)
        print("La somme des paires",somme)
       
        lb = somme.to_bytes(4,byteorder="little",signed = True)

        os.write(pipew3,lb)
        os.close(pipew3)
        sys.exit(0)
        

    else:
        #impaire
        os.close(piper1)
        os.close(pipew1)
        os.close(pipew2)
        os.close(piper3)
        os.close(pipew3)
        os.close(piper4)
        
        var=0
        while var != -1:
            somme+=var
            lb = os.read(piper2,4)
            var = int.from_bytes(lb,byteorder="little",signed=True)

        os.close(piper2)

        print("La somme des impaires",somme)

    
        lb = somme.to_bytes(4,byteorder="little",signed = True)

        os.write(pipew4,lb)


        os.close(pipew4)
        sys.exit(0)
        