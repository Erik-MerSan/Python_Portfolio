# File: RecursiveFunctions.py
# Student: Erik Mercado
# UT EID: emm4376
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: November 17, 2020
# Date Last Modified: November 22, 2020
# Description of Program: recursions

def sumItemsInList( L ):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList( key, L ):
    """ Return the number of times key occurs in
    list L. """
    if L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList( key, L[1:] )
    else:
        return countOccurrencesInList( key, L[1:] )

def addToN ( n ):
   """ Add up the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
   if n == 0:
       return 0
   elif n == 1:
       return 1
   else:
       return n + addToN(n-1)

def findSumOfDigits( n ):
   """ Return the sum of the digits in a non-negative integer. """
   if n == 0:
       return 0
   else:
       return (n % 10) + findSumOfDigits(n//10)

def decimalToBinary( n ):
   """ Given a nonnegative decimal n, return the
   binary representation as a string. """
   if n < 2:
       return str(n)
   else:
        return str(decimalToBinary((n // 2))) + str(n % 2)

def decimalToList( n ):
   """ Given a positive decimal integer, return a list of the
   digits (as strings). """
   if n == 0:
       return []
   else:
       return (decimalToList((n // 10))) + [str(n % 10)]

def isPalindrome( s ):
   """ Return True if string s is a palindrome and False
   otherwise. Count the empty string as a palindrome. """
   if s == '':
       return True
   elif len(s) <= 1:
       return True
   elif s[0] != s[len(s) - 1]:
       return False
   else:
       return isPalindrome(s[1: len(s) - 1])

def findFirstUppercase( s ):
   """ Return the first uppercase letter in
   string s, if any.  Return None if there
   is none. """
   if s == '':
       return None
   if s[0].isupper():
       return s[0]
   else:
       return findFirstUppercase(s[1:])

def findFirstUppercaseIndexHelper( s, index ):
   """ Helper function for findFirstUppercaseIndex. """
   if len(s) == 0:
       return -1
   if index == len(s):
       return -1
   if s[index].isupper():
       return index
   else:
       return findFirstUppercaseIndexHelper(s, index + 1)

# The following function is already completed for you.  But
# make sure you understand what it's doing.

def findFirstUppercaseIndex( s ):
   """ Return the index of the first uppercase letter in
   string s, if any.  Return -1 if there is none.  This one
   requires a helper function, which is the recursive
   function. """
   return findFirstUppercaseIndexHelper( s, 0 )


#print(addToN( 10 ))
#print(addToN( 100 ))
#print(addToN( 0 ))
#print(findSumOfDigits( 0 ))
#print(findSumOfDigits( 12345 ))
#print( decimalToBinary( 25 ))
#print( decimalToBinary( 100 ))
#print(decimalToBinary( 0 ))
#print(decimalToList( 123 ))
#print(decimalToList( 348914 ))
#print(decimalToList( 0 ))
#print(isPalindrome( "abcDcba" ))
#print(isPalindrome( "abcDcbaF" ))
#print(isPalindrome( "" ))
#print(isPalindrome( "X" ))
#print(findFirstUppercase( "ab c  dEFg hi" ))
#print(findFirstUppercase( "ab c  defg hi" ))
#print(findFirstUppercaseIndex( "ab c  dEFg hi" ))
#print(findFirstUppercaseIndex( "ab c  defg hi" ))
#print(findFirstUppercaseIndex( "" ))