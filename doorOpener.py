import RPi.GPIO as GPIO
from time import sleep

gpio_pin = 40
strikeDuration = 1

def openDoor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, 0)
    print("Opening door for " + str(strikeDuration) + " seconds.")
    sleep(strikeDuration)
    GPIO.output(gpio_pin, 0)

openDoor()