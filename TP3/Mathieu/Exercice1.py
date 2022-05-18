import os,sys
import multiprocessing as mp


print("création d'un pipe anonyme")
(dfr,dfw) = mp.Pipe()

if os.fork() == 0:

    dfr.close()

    msg = 'monMessage'
    n = dfw.send(msg)
    print("LE processus %d a transmis le message %s\n" %(os.getpid(),msg))
    exit(0)

dfw.close()

msgReception = dfr.recv()
print("Le processus %d a reçu le message %s\n"%(os.getpid(),msgReception))

dfr.close()

sys.exit(0)

# toto
# toto
# chaine
# chaine
#z chaine
