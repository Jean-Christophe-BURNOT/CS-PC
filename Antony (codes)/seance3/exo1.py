
# -*- coding: utf-8 -*-

import os,sys

var=13.33
piper,pipew = os.pipe()

pid = os.fork()
if pid != 0 : #Processus Père
    os.close(piper)
    var=var+12
    var_b = var.hex().encode()
    length = len(var_b)
    lb = length.to_bytes(4,byteorder="little",signed = True)
    os.write(pipew,lb)

    os.write(pipew,var_b)
  
    print ("lol")
    os.close(pipew)
else : #Processus fils

    os.close(pipew)

    lb = os.read(piper,4)
    length = int.from_bytes(lb,byteorder="little",signed=True)
    var_b = os.read(piper,length)
    var = float.fromhex(var_b.decode())
    print("new var",var)

    print ("mdr")
    os.close(piper)
sys.exit(0)