# File: Project2.py
# Student: Erik Mercado
# UT EID: emm4376
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: November 1, 2020
# Date Last Modified: November 2, 2020
# Description of Program: factoring and priming


def isPrime(command, num):

        if command == 'isprime':
            if num < 1:
                print('Illegal input: ', num, ';', ' input must be an integer > 1.', sep='')

            if num > 1:
                if num < 2:
                    print('The number', num, "is not prime")
                    print()
                    return
                elif num == 2:
                    print('The number 2 is prime')
                    print()
                    return
                else:
                    divisor = 2
                    while divisor < num:
                        if num % divisor == 0:
                            print('The number', num, "is not prime")
                            print()
                            return
                        else:
                            divisor += 1
                    print('The number', num, "is prime")
                    print()
                    return
        print()
        return


def primeFactorization(command, num):

    onum = num

    if command == 'factor':
        if num < 1:
            print('Illegal input: ', num, ';', ' input must be an integer > 1.', sep='')
            return
        if num > 1:
            factors = []
            d = 2
            while num > 1:
                if num % d == 0:
                    factors.append(d)
                    num //= d
                else:
                    d += 1
            print('The prime factorization of', onum, 'is:', factors)
            return


def main():

    print('Welcome to the Prime factory!')
    print()
    while True:

        command = input('Enter a command (factor, isprime, end): ').lower().strip()

        if command == 'end':
            print('Thanks for using our service! Goodbye.')
            break
        elif command != 'factor' and command != 'isprime' and command != 'end':
                print('Command', command, 'not recognized. Try again!')
                print()

        elif command == 'isprime' or command == 'factor':
            num = int(input('Enter an integer > 1: '))
            primeFactorization(command, num)
            isPrime(command, num)


main()

