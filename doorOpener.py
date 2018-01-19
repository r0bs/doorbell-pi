import RPi.GPIO as GPIO

gpio_pin = 40
strikeDuration = 1

def openDoor():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(port_or_pin, 1)
    print("Opening door for " + strikeDuration + " seconds.")
    sleep(strikeDuration)
    GPIO.output(port_or_pin, 0)