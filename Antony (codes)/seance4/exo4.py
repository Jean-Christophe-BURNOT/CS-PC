
# -*- coding: utf-8 -*-

import os,sys,time
from signal import SIGKILL

N=10
pid = os.fork()
if pid != 0 : #Processus Père
    for i in range(N):
        time.sleep(1)
        print("wolooooooooolloooolololooooooooooooololoooolololooooooooooo")
        if i==3:
            os.kill(pid , SIGKILL)
    sys.exit(0)
    
else:
    while True:
        time.sleep(0.25)
        print("wolooooooloooooooloooo")
