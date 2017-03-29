from gpiozero import LED, Button
from signal import pause
from time import sleep

red_pressed = 0
yellow_pressed = 0
green_pressed = 0
message = ''

d = {(1, 0): 'a',
     (1, 1): 'b',
     (1, 2): 'c',
     (1, 3): 'd',
     (2, 0): 'e',
     (2, 1): 'f',
     (2, 2): 'g',
     (2, 3): 'h',
     (3, 0): 'i',
     (3, 1): 'j',
     (3, 2): 'k',
     (3, 3): 'l',
     (3, 4): 'm',
     (3, 5): 'n',
     (4, 0): 'o',
     (4, 1): 'p',
     (4, 2): 'q',
     (4, 3): 'r',
     (4, 4): 's',
     (4, 5): 't',
     (5, 0): 'u',
     (5, 1): 'v',
     (5, 2): 'w',
     (5, 3): 'x',
     (5, 4): 'y',
     (5, 5): 'z'
    }

# LED assignments
red = LED(2)
yellow  = LED(3)
green = LED(4)

def red_action():
    global red_pressed
    global green_pressed
    global message

    red.off()
    red_pressed += 1
    green_pressed = 0

def yellow_action():
    global yellow_pressed

    yellow.off()
    yellow_pressed += 1

def green_action():
    global red_pressed
    global yellow_pressed
    global green_pressed
    global message

    green.off()

    if red_pressed > 5:
        # End of sentence
        print()
        print(message)
        
        red_pressed = 0
        yellow_pressed = 0
        green_pressed = 0
        message = ''
    elif green_pressed == 0:        
        if (red_pressed, yellow_pressed) in d:
            letter = d[(red_pressed, yellow_pressed)]
        else:
            letter = '*'
        print(letter, end='')
        message += letter
        red_pressed = 0
        yellow_pressed = 0
        green_pressed += 1
    else:
        print('_', end='')
        message += '_'

# Button assignments
red_btn = Button(17)
red_btn.when_pressed = red.on
red_btn.when_released = red_action

yellow_btn = Button(13)
yellow_btn.when_pressed = yellow.on
yellow_btn.when_released = yellow_action

green_btn = Button(19)
green_btn.when_pressed = green.on
green_btn.when_released = green_action

pause()
