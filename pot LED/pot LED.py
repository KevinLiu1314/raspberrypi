import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

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

# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 12     # CLK
SPIMISO = 16    # DOUT
SPIMOSI = 18    # DIN
SPICS = 22      # CS

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# 10k trim pot connected to adc #0
potentiometer_adc = 0

# set up the LED pins
GPIO.setup(3, GPIO.OUT)     # First LED
GPIO.setup(5, GPIO.OUT)     # Second LED
GPIO.setup(7, GPIO.OUT)     # Third LED

while True:
        # read the analog pin
        trim_pot = readadc(potentiometer_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)
        
        if trim_pot < 1024/3:   # First LED on
            GPIO.output(3, GPIO.HIGH)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
        elif trim_pot > 1024/3*2:   # Third LED on
            GPIO.output(3, GPIO.LOW)
            GPIO.output(5, GPIO.LOW)
            GPIO.output(7, GPIO.HIGH)
        else:   # Second LED on
            GPIO.output(3, GPIO.LOW)
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(7, GPIO.LOW)

        time.sleep(0.1)                            
