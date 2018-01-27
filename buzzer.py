import RPi.GPIO as GPIO
import gpioConfig
from time import sleep

def buzz():
    print("Making sound")
    for beep in range(0, 3):
        GPIO.output(gpioConfig.buzzerPin, 1)
        sleep(0.2)
        GPIO.output(gpioConfig.buzzerPin, 0)
        sleep(0.3)
    print("Sound stopped.")
    
    