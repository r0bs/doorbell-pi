import RPi.GPIO as GPIO
from ringSignaler import RingSignaler
from time import sleep

gpio_pin = 26

def startListeningForRing(tokenhandler):
    try:
        signaler = RingSignaler(tokenhandler)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio_pin, GPIO.IN)
        GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback = signaler.sendNotification, bouncetime = 200)
        while True:
            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("stops listening for ring")