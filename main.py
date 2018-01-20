#!/usr/bin/env python3

import threading
import logging
from time import sleep
from messageListener import messageListener
from ringListener import startListeningForRing

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def runRingSignaler():
    startListeningForRing()

def runMessageListener():
    messageListener()

if __name__=='__main__':
    threading.Thread(target=runRingSignaler).start()
    threading.Thread(target=runMessageListener).start()