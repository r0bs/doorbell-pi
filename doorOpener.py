import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def openDoor():
    GPIO.setup(gpioConfig.doorOpenerPin, GPIO.OUT)
    GPIO.output(gpioConfig.doorOpenerPin, 0)

    print("Opening door for " + str(gpioConfig.strikeDuration) + " seconds.")
    print("...")
    sleep(gpioConfig.strikeDuration)
    print("Opening door done.")

    GPIO.cleanup(gpioConfig.doorOpenerPin)
    