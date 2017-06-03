message = "What a smart Puffle!"

coded_message = []
for c in message:
    b = "{0:08b}".format(ord(c))
    coded_message.append(b)
    print(b, end=' ')

print()

for code in coded_message:
    print(chr(int(code, 2)), end='')

print()

for code in coded_message:
    print(code[::-1], end='  ')
