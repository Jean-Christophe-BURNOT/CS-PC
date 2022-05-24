#coding:utf-8
import sys

if len(sys.argv)<=1:
    print('Aucune moyenne à calculer')
else: 
    valeur=0 
    bool1=1

    for arg in sys.argv[1:]:
        try :
            float(arg)
            if 0 <= float(arg) <= 20:
                valeur+=float(arg)

            else:
                bool1=3
                break

        except:
            bool1=2
          
            
    if bool1==1:
        valeur=valeur/(len(sys.argv)-1)
        
        print('La moyenne est ' + str(round(valeur,2)))    

    elif bool1==2:
        print("les arguments n'ont pas le bon type")
    else :
        print('Note(s) non valide(s)')

