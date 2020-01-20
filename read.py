#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDPin = 22
buttonPin = 5

# Setup what GPIO Pin is connected to
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def isPushed():
    buttonPress = GPIO.input(buttonPin)
    if buttonPress == False:
        return True
    return False

def toggleLED(ledState):
    if ledState == False:
        GPIO.output(LEDPin, True)
    else:
        GPIO.output(LEDPin, False)
    return not ledState

def turn_LED_on():
    GPIO.output(LEDPin, True)
    return True

def turn_LED_off():
    GPIO.output(LEDPin, False)
    return False

count = 101
check_lim = 50
try:
    ledState = False
    print("Press button to turn on")

    while True:
        sleep(0.2)
        count += 1

        #check file only so often
        if count > check_lim:
            count = 0
            with open('infile.txt', 'r') as f:
                response = f.read().rstrip()
                if response == "a":
                    ledState = turn_LED_on()
                    print("LED {}, FILE value = {}".format(ledState, response))
                elif response == 'b':
                    ledState = turn_LED_off()
                    print("LED {}, FILE value = {}".format(ledState, response))
        if isPushed():
            ledState = toggleLED(ledState)
            print("LED {}".format(ledState))
except KeyboardInterrupt:
    pass

finally:
    # Reset the GPIO Pins to a safe state
    GPIO.output(LEDPin, False)
    GPIO.cleanup()
