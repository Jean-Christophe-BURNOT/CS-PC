import os,sys

pid = os.fork()
if pid==0:
    os.execlp('who','who')
else:
    
    pid = os.fork()
    if pid==0:
        os.execlp('ps','ps')
    else:
        os.execlp('ls','ls','-l')