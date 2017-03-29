from gpiozero import LED, Button
from time import sleep
from signal import pause

d = {'a': (1, 0),
     'b': (1, 1),
     'c': (1, 2),
     'd': (1, 3),
     'e': (2, 0),
     'f': (2, 1),
     'g': (2, 2),
     'h': (2, 3),
     'i': (3, 0),
     'j': (3, 1),
     'k': (3, 2),
     'l': (3, 3),
     'm': (3, 4),
     'n': (3, 5),
     'o': (4, 0),
     'p': (4, 1),
     'q': (4, 2),
     'r': (4, 3),
     's': (4, 4),
     't': (4, 5),
     'u': (5, 0),
     'v': (5, 1),
     'w': (5, 2),
     'x': (5, 3),
     'y': (5, 4),
     'z': (5, 5)
    }

red = LED(2)
yellow  = LED(3)
green = LED(4)
on_time = .5
off_time = .5

def flash(r, y):
    for i in range(r):
        red.on()
        sleep(on_time)
        red.off()
        sleep(off_time)
    for i in range(y):
        yellow.on()
        sleep(on_time)
        yellow.off()
        sleep(off_time)
    green.on()
    sleep(on_time)
    green.off()

word = input('Enter word to send: ')
for letter in word.lower():
    flash(*d[letter])
    green.on()
    sleep(off_time)
    green.off()
