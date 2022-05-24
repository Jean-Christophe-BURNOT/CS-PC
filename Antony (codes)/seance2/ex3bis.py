import os,sys

pid = os.fork()
if pid==0:
    os.execlp('who','who')
else:
    os.wait()
    pid = os.fork()
    if pid==0:
        os.execlp('ps','ps')
    else:
        os.wait()
        os.execlp('ls','ls','-l')
