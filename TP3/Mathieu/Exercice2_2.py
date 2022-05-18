import os,sys
import multiprocessing as mp

# "wc Fichier.format" donne 3 paramètre (le nombre de ligne, le nombre de mot, le nombre de caractere d'un fichier)
# "sort Fichier.format" trie les lignes d'un fichier en fonction de la premiere lettre de chaque ligne
# "tail arg -n" affiche les dernières ligne d'un fichier, peux prendre des argument (Ex: -1 pour n'avoir que la dernière ligne)
# "sort < fichier.py > fichier_trie" crée un fichier (fichier_trie) correspondant au sort de fichier0py
# "sort fichier | grep toto | wc –l"

n = input("fichier : ")

(dfr,dfw) = os.pipe()
(dfr2,dfw2) = os.pipe()

pid = os.fork()

if pid == 0:

    print("[Le processus %d] : sort \n"%os.getpid())
    os.close(dfr)
    os.close(dfw2)
    os.close(dfr2)

    os.dup2(dfw,1)

    os.close(dfw)
    os.execlp("sort","sort",n,"sortie") 

else :
    pid = os.fork()
    if pid == 0:
        print("[Le processus %d] : grep \n" %os.getpid())
        os.close(dfw)
        os.close(dfr2)
        os.dup2(dfr , 0)
        os.dup2(dfw2 , 1)
        os.close(dfw2)
        os.close(dfr)
        os.execlp("grep" , "grep","chaine")
    else :

        print ("[Le processus %d] : tail \n" %os.getpid() )
        os.close(dfw) ; os.close(dfr)
        os.close(dfw2)
        os.dup2(dfr2 ,0 ) 
        os.close(dfr2)
        os.execlp("tail" ,"tail" , "-n" ,"5")