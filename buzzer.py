import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def buzz():
    print("Making sound")
    for beep in range(0, 10):
        GPIO.output(gpioConfig.buzzerPin, 1)
        sleep(0.1)
        GPIO.output(gpioConfig.buzzerPin, 0)
    print("Sound stopped.")
    
    