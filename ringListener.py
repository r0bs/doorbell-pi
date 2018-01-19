import RPi.GPIO as GPIO
from notifier import Notifier
import time

gpio_pin = 7

def startListeningForRing(tokenhandler):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio_pin, GPIO.IN)
        GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback = ringHandler, bouncetime = 800)
        print("Listening for ring on GPIO PIN #" + str(gpio_pin))
        while True:
            time.sleep(0.2)
        print("Stopped listing for Ring")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("stops listening for ring")

def ringHandler(pin):
    localtime = time.asctime( time.localtime(time.time()) )
    print("Doorbell rang at: " + localtime)
    
    signaler = Notifier(tokenhandler)
    signaler.sendNotification()
