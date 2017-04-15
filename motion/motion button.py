from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(26)
btn = Button(19)

def action():
    print("Motion detected")
    led.on()
    sleep(.2)
    led.off()

btn.when_released = action

pause()
