import RPi.GPIO as GPIO
import notifier
import time
import logging
import gpioConfig

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def startListeningForRing():
    GPIO.add_event_detect(gpioConfig.ringListenerPin, GPIO.BOTH, callback = ringHandler)
    print("Listening for ring signal on GPIO PIN #" + str(gpioConfig.ringListenerPin))
    
    while True:
        time.sleep(0.2) 
    print("Stopped listing for Ring")


def ringHandler(pin):
    if "openeButtonCycle" not in globals():
        global openeButtonCycle
        openeButtonCycle = True
        
    if GPIO.input(gpioConfig.ringListenerPin) == 0 and openeButtonCycle is True:
        openeButtonCycle = False

    elif openeButtonCycle is False:
        openeButtonCycle = True

        localtime = time.asctime( time.localtime(time.time()) )
        print("Doorbell rang on PIN #" + str(pin) +" at: " + localtime)

        notifier.sendNotification()