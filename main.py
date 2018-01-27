#!/usr/bin/env python3

import threading
import logging
import gpioConfig
import RPi.GPIO as GPIO
import buzzer

from time import sleep
from messageListener import messageListener
from ringListener import startListeningForRing

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def runRingSignaler():
    startListeningForRing()

def runMessageListener():
    messageListener()

def gpioStartup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(gpioConfig.doorOpenerPin, GPIO.OUT)
    GPIO.output(gpioConfig.doorOpenerPin, 1)

    GPIO.setup(gpioConfig.ringListenerPin, GPIO.IN)

if __name__=='__main__':
    gpioStartup()
    buzz()
    threading.Thread(target=runRingSignaler).start()
    threading.Thread(target=runMessageListener).start()