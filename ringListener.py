import RPi.GPIO as GPIO
from ringSignaler import RingSignaler
from time import sleep

gpio_pin = 7

def startListeningForRing(tokenhandler):
    try:
        signaler = RingSignaler(tokenhandler)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(gpio_pin, GPIO.IN)
        GPIO.add_event_detect(gpio_pin, GPIO.FALLING, callback = signaler.sendNotification, bouncetime = 800)
        while True:
            print("Listening for ring on GPIO PIN #" + str(gpio_pin)
            sleep(0.2)
        print("Stopped listing for Ring")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("stops listening for ring")