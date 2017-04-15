import lirc
import time

sockid = lirc.init("irkeys", blocking = False)   #IR-code

while True:
    codeIR = lirc.nextcode()    #IR-code
    if len(codeIR)>0:
        print(codeIR)
    #time.sleep(2)
    
