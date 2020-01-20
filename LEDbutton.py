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
        newState = "ON"
        GPIO.output(LEDPin, True)
    else:
        newState = "OFF"
        GPIO.output(LEDPin, False)

    print("LED {}".format(newState))
    sleep(0.5)

    return not ledState

try:
    ledState = False
    print("Come on Man, Press the button")

    while True:

        if isPushed():
            ledState = toggleLED(ledState)
        else:
            sleep(0.1)
finally:
    # Reset the GPIO Pins to a safe state
    GPIO.output(LEDPin, False)
    GPIO.cleanup()



