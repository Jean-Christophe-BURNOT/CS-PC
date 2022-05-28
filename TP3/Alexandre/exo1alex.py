import os, sys

dr,dw = os.pipe()

if os.fork() == 0:
    os.close(dr)
    n1 = input("Entrer un nombre: ")
    n2 = input("Entrer un deuxieme nombre: ")
    encoded_r = bytes(n1 + ":" + n2, "UTF-8")
    #Envoit l'information dans le pipe
    os.write(dw, encoded_r)
    sys.exit(0)

os.wait()

#50 correspond au nombre de bits que l'ont reçoit (valeur arbitraire)
r_byte = os.read(dr,50)
r_decoded = r_byte.decode("UTF-8")

listeNbr = r_decoded.split(":")

print("La somme de", listeNbr[0], "et", listeNbr[1], "est", float(listeNbr[0]) + float(listeNbr[1]))


