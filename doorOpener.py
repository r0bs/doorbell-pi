import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def openDoor():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(gpioConfig.doorOpenerPin, GPIO.OUT)
    GPIO.output(gpioConfig.doorOpenerPin, 1)
    
    GPIO.output(gpioConfig.doorOpenerPin, 0)
    print("Opening door for " + str(gpioConfig.strikeDuration) + " seconds.")
    print("...")
    sleep(gpioConfig.strikeDuration)
    GPIO.output(gpioConfig.doorOpenerPin, 1)
    print("Opening door done.")