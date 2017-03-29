import RPi.GPIO as GPIO
import random
import time
 
# Use pin numbers
GPIO.setmode(GPIO.BOARD)

# Use GPIO numbers not pin numbers
# GPIO.setmode(GPIO.BCM)
 
# set up the GPIO channels - one input and one output
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
 
# input from GPIO7
# input_value = GPIO.input(7)
 
# output to GPIO8
#GPIO.output(8, True)

while True:
	GPIO.output(3, random.choice([GPIO.HIGH, GPIO.LOW]))
	GPIO.output(5, random.choice([GPIO.HIGH, GPIO.LOW]))
	GPIO.output(7, random.choice([GPIO.HIGH, GPIO.LOW]))
	time.sleep(random.choice([.05, .1, .15, .2]))
