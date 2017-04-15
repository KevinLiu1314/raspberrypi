keys = {'KEY_0': '0',
'KEY_1': '1',
'KEY_2': '2',
'KEY_3': '3',
'KEY_4': '4',
'KEY_5': '5',
'KEY_6': '6',
'KEY_7': '7',
'KEY_8': '8',
'KEY_9': '9',
'KEY_LEFT': 'LEFT',
'KEY_RIGHT': 'RIGHT',
'KEY_DOWN': 'DOWN',
'KEY_UP': 'UP',
'KEY_OK': 'OK',
}

prog = 'irtest'

for key in sorted(keys):
    print("begin")
    print("button = ", key)
    print("prog = ", prog)
    print("config = ", keys[key])
    print("end")
