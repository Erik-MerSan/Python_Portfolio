# Course Name: CS303E
# Unique Number: 50695
# Description of Program: encrypt/decrypt a text by a chosen value

def main():
    # first we display a prompt asking if the user wants to encrypt or decrypt
    command = input('Enter Caesar cipher command (encrypt/decrypt): ').lower().strip()
    result = ""
    if command == 'encrypt':
        print("You've asked to encrypt.")
        # this is where the user is going to choose the value for encryption
        shift = int(input('Please enter shift value (0 .. 25): '))
        if int(shift) > 25 or int(shift) < 0:
            # shift values should be between 0 and 25
            print("Illegal shift value:", shift)
            exit()
        # this is where the user will enter the text that they want to encrypt
        phrase = input('Please enter text to encrypt: ')
        # checking the ascii number of the individual letters in the text
        # changing algo different based on if letter is capital or not 
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
                # add the encrypted letter one by one 
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
    # error case
    if command != 'encrypt' and command != 'decrypt':
        print("Unrecognized command:", command)


main()
