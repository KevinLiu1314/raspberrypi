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
'KEY_POWER': 'POWER',
'KEY_MENU': 'MENU',
'KEY_DISPLAYTOGGLE': 'DISPLAYTOGGLE',
'KEY_TITLE': 'TITLE',
'KEY_SETUP': 'SETUP',
'KEY_PREVIOUS': 'PREVIOUS',
'KEY_NEXT': 'NEXT',
'KEY_PLAY': 'PLAY',
'KEY_STOP': 'STOP',
'KEY_MUTE': 'MUTE',
'KEY_SUBTITLE': 'SUBTITLE',
'KEY_AUDIO': 'AUDIO',
'KEY_ZOOM': 'ZOOM',
}

prog = 'irtest'

for key in sorted(keys):
    print("begin")
    print("button = ", key)
    print("prog = ", prog)
    print("config = ", keys[key])
    print("end")
