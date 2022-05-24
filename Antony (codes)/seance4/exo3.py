import signal,time, sys

global fin
fin=False

def arreterProgramme(signal,frame) :
    global fin 
    fin=True

signal.signal(signal.SIGINT, arreterProgramme)



def boucle():
    global fin 

    while not(fin) :
        time.sleep(2)
        print("je boucle")

boucle()
sys.exit(0)