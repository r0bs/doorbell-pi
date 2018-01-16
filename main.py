import threading
from time import sleep
from tokenHandler import TokenHandler
from commandListener import CommandServer
from ringListener import startListeningForRing

tokenhandler = TokenHandler()

def runRingSignaler():
    startListeningForRing(tokenhandler)

def runCommandServer():
    CommandServer(tokenhandler)

if __name__=='__main__':
    threading.Thread(target=runRingSignaler).start()
    threading.Thread(target=runCommandServer).start()
