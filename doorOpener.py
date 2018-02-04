import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def openDoor():
    GPIO.output(gpioConfig.doorOpenerPin, 1)
    print("Opening door for " + str(gpioConfig.strikeDuration) + " seconds.")
    print("...")
    sleep(gpioConfig.strikeDuration)
    print("Opening door done.")
    GPIO.output(gpioConfig.doorOpenerPin, 0)
    