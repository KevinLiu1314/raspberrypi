import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BOARD)

relay_pin = 35
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    try:
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

    
