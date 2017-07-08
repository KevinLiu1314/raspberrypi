import time
import RPi.GPIO as GPIO
from gpiozero import LED, Button

GPIO.setmode(GPIO.BCM)

# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1

    GPIO.output(cspin, True)
    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
            
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)
        
    adcout >>= 1       # first bit is 'null' so drop it
    return adcout


def action():
    global first, third, old_trim_pot, button_press_counter, secret_number, mode

    button_press_counter += 1
    if button_press_counter % secret_number == 0:
        mode = "110HZ"
    else:
        mode = "NORMAL"
    
    temp = first
    first = third
    third = temp

    old_trim_pot = -728


# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18     # CLK
SPIMISO = 23    # DOUT
SPIMOSI = 24    # DIN
SPICS = 25      # CS

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# 10k trim pot connected to adc #0
potentiometer_adc = 0

# set up the LED pins
first = LED(2)      # First LED
second = LED(3)     # Second LED
third = LED(4)      # Third LED
btn = Button(17)    # button
btn.when_released = action

# Button press counter & Mode
button_press_counter = 0
secret_number = 8
mode = "NORMAL"
already_110HZ = False

old_trim_pot = -728
while True:
    if mode == "110HZ" and not already_110HZ:
        first.blink(.5/110, .5/110)
        second.blink(.5/110, .5/110)
        third.blink(.5/110, .5/110)
        already_110HZ = True
    elif mode == "NORMAL":
        #reset status
        already_110HZ = False
        
        # read the analog pin
        trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        # print(trim_pot, old_trim_pot)

        if abs(trim_pot - old_trim_pot) > 5:
            if trim_pot < 1024/3:   # First LED on
                first.blink(.25, .25)
                second.off()
                third.off()
            elif trim_pot > 1024/3*2:   # Third LED on
                first.off()
                second.off()
                third.blink(.05, .05)
            else:   # Second LED on
                first.off()
                second.blink(.1, .1)
                third.off()

            old_trim_pot = trim_pot

    time.sleep(.25)                            
