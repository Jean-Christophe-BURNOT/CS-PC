import os,sys

pid = os.fork()
if pid==0:
    print('traitement1')
else:
    os.wait()
    print('traitement2')
    
    os.execlp('python3','python3','test.py')
sys.exit(0)