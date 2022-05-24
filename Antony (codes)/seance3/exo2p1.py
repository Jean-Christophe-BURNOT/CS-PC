
# -*- coding: utf-8 -*-

import os,sys

piper,pipew = os.pipe()

pid=os.fork()
if pid==0:
    os.close(piper)
    os.dup2(pipew, 1)
    os.close(pipew)
    
    os.execlp("cat","cat","text.txt")
    
else:
    os.close(pipew)

    os.dup2(piper, 0)

    os.close(piper)

    os.execlp("wc","wc","text.txt")
