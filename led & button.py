from gpiozero import LED, Button
from signal import pause
from time import sleep

# LED assignments
red = LED(2)
yellow  = LED(3)
green = LED(4)

# Button assignments
red_btn = Button(17)
red_btn.when_pressed = red.toggle
#red_btn.when_released = red.toggle

yellow_btn = Button(13)
yellow_btn.when_pressed = yellow.on
yellow_btn.when_released = yellow.off

green_btn = Button(19)
green_btn.when_pressed = green.on
green_btn.when_released = green.off

pause()
