import RPi.GPIO as GPIO
from ringSignaler import RingSignaler
from time import sleep

def startListeningForRing(tokenhandler):
    try:
        signaler = RingSignaler(tokenhandler)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(17, GPIO.IN)
        GPIO.add_event_detect(17, GPIO.FALLING, callback = signaler.sendNotification, bouncetime = 200)
        while True:
            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("stops listening for ring")