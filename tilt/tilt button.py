from gpiozero import PWMLED, Button
from time import sleep
from signal import pause

btn = Button(20, hold_time=.25)
led = PWMLED(21)

def pressed_action():
    print("contact")
    led.off()
    
def released_action():
    print("no contact")
    led.off()
    
def held_action():
    print("tilted")
    #led.pulse()
    led.blink(.1, .1)

btn.when_pressed = pressed_action
btn.when_released = released_action
btn.when_held = held_action

pause()

