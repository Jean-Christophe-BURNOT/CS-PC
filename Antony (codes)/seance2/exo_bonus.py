# -*- coding: utf-8 -*-

import os,sys

piper,pipew = os.pipe()
dicoNotes = { "E1" : [10, 15, 20], "E2" : [12, 16, 15], "E3" : [11, 13, 20],"E4" : [11, 13, 20],"E5" : [11, 13, 20] }
N=len(dicoNotes)



for i in range(1,N+1):
    var="E"+str(i)
    pid=os.fork()
    moyenne=0
    notes=dicoNotes[var]
    l=len(notes)

    if pid==0:
        os.close(piper)
        for note in notes:
            moyenne+=note

        var=moyenne/l
        var_b = var.hex().encode()
        length = len(var_b)
        lb = length.to_bytes(4,byteorder="little",signed = True)

        os.write(pipew,lb)

        os.write(pipew,var_b)


        os.close(pipew)

        sys.exit(0)


os.close(pipew)
max=0
min=20
pire=0
meilleur=0
for i in range(1,N+1):
    lb = os.read(piper,4)
    length = int.from_bytes(lb,byteorder="little",signed=True)
    var_b = os.read(piper,length)
    var = float.fromhex(var_b.decode())
    print("La moyenne de E"+str(i)+" est de ",var)

    if var<min:
        min=var
        pire=i
    if var>max:
        max=var
        meilleur=i

os.close(piper)

print("Le pire eleve est E"+str(pire)+" avec une moyenne de "+str(min)+" Le pire eleve est E"+str(meilleur)+" avec une moyenne de "+str(max))

sys.exit(0)





