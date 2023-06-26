# File: CaesarCipher.py
# Student: Erik Mercado
# UT EID: emm4376
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: October 5, 2020
# Date Last Modified: October 7, 2020
# Description of Program: encrypt / decrypt given text based on the value inputted


def main():

    command = input('Enter Caesar cipher command (encrypt/decrypt): ').lower().strip()
    result = ""
    if command == 'encrypt':
        print("You've asked to encrypt.")
        shift = int(input('Please enter shift value (0 .. 25): '))
        if int(shift) > 25 or int(shift) < 0:
            print("Illegal shift value:", shift)
            exit()
        phrase = input('Please enter text to encrypt: ')
        for ch in phrase:
            if 65 <= ord(ch) <= 90:
                w = ord(ch) - ord('A')
                x = (w + shift) % 26
                y = x + ord('A')
                z = chr(y)
                result += z
            elif 97 <= ord(ch) <= 122:
                w = ord(ch) - ord('a')
                x = (w + shift) % 26
                y = x + ord('a')
                z = chr(y)
                result += z
            else:
                result += str(ch)
        print(result, end="")
    if command == 'decrypt':
        print("You've asked to decrypt")
        shift = int(input('Please enter shift value (0 .. 25): '))
        if int(shift) > 25 or int(shift) < 0:
            print("Illegal shift value:", shift)
            exit()
        phrase = input("Please enter text to decrypt: ")
        for ch in phrase:
            if 65 <= ord(ch) <= 90:
                w = ord(ch) - ord('A')
                x = (w - shift) % 26
                y = x + ord('A')
                z = chr(y)
                result += z
            elif 97 <= ord(ch) <= 122:
                w = ord(ch) - ord('a')
                x = (w - shift) % 26
                y = x + ord('a')
                z = chr(y)
                result += z
            else:
                result += str(ch)
        print(result, end="")
    if command != 'encrypt' and command != 'decrypt':
        print("Unrecognized command:", command)


main()
