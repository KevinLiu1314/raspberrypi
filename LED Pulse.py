from gpiozero import PWMLED
from signal import pause

led = PWMLED(21)

led.pulse()

pause()
