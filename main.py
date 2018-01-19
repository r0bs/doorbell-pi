import threading
import logging
from time import sleep
#from tokenHandler import TokenHandler
from messageListener import messageListener
# from commandListener import CommandServer
from ringListener import startListeningForRing

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#tokenhandler = TokenHandler()

def runRingSignaler():
    startListeningForRing()

# def runCommandServer():
#     CommandServer(tokenhandler)

def runMessageListener():
    messageListener()

if __name__=='__main__':
    threading.Thread(target=runRingSignaler).start()
    threading.Thread(target=runMessageListener).start()
    # threading.Thread(target=runCommandServer).start()
