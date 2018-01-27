import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def buzz():
    GPIO.output(gpioConfig.buzzerPin, 1)
    print("Making sound for " + str(gpioConfig.strikeDuration) + " seconds.")
    print("...")
    sleep(gpioConfig.strikeDuration)
    print("Sound stopped.")
    GPIO.output(gpioConfig.buzzerPin, 0)
    