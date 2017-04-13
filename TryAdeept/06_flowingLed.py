#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = [3, 5, 7, 11, 31, 33, 35, 37]

step = .01
def setup():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode is output
        GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V) to off led

def loop():
    while True:
        for delay in range(1, 31):
            for pin in pins:
                GPIO.output(pin, GPIO.LOW)  
                time.sleep(delay*step)
                GPIO.output(pin, GPIO.HIGH)

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)    # turn off all leds
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
