import signal,time, sys

def arreterProgramme(signal,frame) :

    print("C'est l'heure d’arrêt !")
    sys.exit(0)

signal.signal(signal.SIGINT, arreterProgramme)

signal.signal(signal.SIGINT , signal.SIG_IGN)


def boucle():

    while True :
        time.sleep(2)
        print("je boucle")

boucle()
sys.exit(0)