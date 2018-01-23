import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def openDoor():
    GPIO.output(gpioConfig.doorOpenerPin, 0)
    print("Opening door for " + str(gpioConfig.strikeDuration) + " seconds.")
    sleep(gpioConfig.strikeDuration)
    GPIO.output(gpioConfig.doorOpenerPin, 1)