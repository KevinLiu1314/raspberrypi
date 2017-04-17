import os
import lirc
import time
from sys import stdout

sockid = lirc.init("irkeys", blocking = False)   #IR-code

current_volume = 65
set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = current_volume)
os.system(set_vol_cmd)  # set volume

stdout.write("\r\r\r%3d" % current_volume)
stdout.flush()

while True:
    codeIR = lirc.nextcode()    #IR-code
    if len(codeIR)>0 and codeIR[0] in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'POWER']:
        if codeIR[0] == 'POWER':
            current_volume = 65
        elif codeIR[0] == 'UP':
            current_volume += 1
        elif codeIR[0] == 'DOWN':
            current_volume -= 1
        elif codeIR[0] == 'LEFT':
            current_volume -= 5
        elif codeIR[0] == 'RIGHT':
            current_volume += 5

        if current_volume > 100:
            current_volume = 100
        if current_volume < 0:
            current_volume = 0
            
        set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' .format(volume = current_volume)
        os.system(set_vol_cmd)  # set volume

        stdout.write("\r\r\r%3d" % current_volume)
        stdout.flush()

    time.sleep(.5)
