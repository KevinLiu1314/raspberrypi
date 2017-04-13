import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
pwm = GPIO.PWM(11, 50)
pwm.start(1)
while True:
    try:
        for i in range(1, 101):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
        for i in range(100, 0, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(.02)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
