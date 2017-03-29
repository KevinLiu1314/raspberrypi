from gpiozero import LED, Button
from time import sleep
from signal import pause
import os
import random

button = Button(19)

farts = ['ben-fart.wav', 'ca-fart.wav', 'marc-fart.wav']

while True:
    button.wait_for_press()
    fart = random.choice(farts)
    os.system("aplay {0}".format(fart))
    sleep(1)
