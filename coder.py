##Nathan Hinton
from string import ascii_lowercase as alphabet
from random import randint as rint

alphabet = list(alphabet)
class adderMethod:
    def __init__(self):
        pass
    def encode():
        message = input("Message: ")
        final = ''
        for char in message:
            if char == ' ':
                final+=',.'
            elif char in alphabet:
                offset = rint(1, 5)
                position = alphabet.index(char)
                newChar = position - offset
                final += (str(alphabet[newChar])+str(offset))
            else:
                final += char
        print(final)
    def decode():
        x = 1
        message = input("Message to decode: ")
        final = ''
        for char in message:
            if char == ',':
                final+=' '
            elif char in alphabet:
                try:
                    offset = int(message[x])
                except ValueError:
                    print("ERROR!")
                    break
                position = alphabet.index(char)
                newChar = (position + offset)%26
                print(newChar)
                final += alphabet[int(newChar)]
            else:
                pass
            x += 1
        print(final)
class shifter:
    def __init__(self):
        pass
    def encode():
        message = input("Message: ")
        shiftNumber = int(input("Shift number: "))
        output = ''
        for char in message:
            if char in alphabet:
                place = alphabet.index(char)
                newPlace = place + shiftNumber
                output += alphabet[(newPlace%26)]
            else:
                output += char
        print(output)
    def decode():
        message = input("Message: ")
        shiftNumber = int(input("Shift number: "))
        output = ''
        for char in message:
            if char in alphabet:
                place = alphabet.index(char)
                newPlace = place - shiftNumber
                output += alphabet[newPlace]
            else:
                output += char
        print(output)
