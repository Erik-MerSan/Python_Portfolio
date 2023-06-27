# File: ComparingLinearBinarySearch.py
# Student: Erik Mercado
# UT EID: emm437d
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: November 5, 2020
# Date Last Modified: November 6, 2020
# Description of Program: Comparing linear and binary search

import math
import random

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """

    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """

    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (count)
        else:
            low = mid + 1
    # Search failed
    return (count)

def insertionSort (lst):

    for i in range ( 1, len( lst ) ):

        # insert lst [i] into sorted sublist
        # lst [0: i] so that lst [0:i +1] is sorted
        currentElement = lst [i]
        k = i - 1
        while k >= 0 and lst [k ] > currentElement :
            lst [k + 1] = lst [k]
            k -= 1
            # Insert the current element into lst[k+1]
        lst[k + 1] = currentElement

    return lst

def ComparingLinearBinarySearch():
    lst = [random.randint(0, 999) for x in range(1000)]

    finalA1 = 0
    finalA2 = 0
    finalA3 = 0
    finalA4 = 0
    finalA5 = 0

    for i in range(0, 10):
        average1 = ((linearSearch(lst, random.randint(0, 999))) / 10) * 2
        finalA1 += average1

    for i in range(0, 100):
        average2 = ((linearSearch(lst, random.randint(0, 999))) / 100) * 2
        finalA2 += average2

    for i in range(0, 1000):
        average3 = ((linearSearch(lst, random.randint(0, 999))) / 1000) * 2
        finalA3 += average3

    for i in range(0, 10000):
        average4 = ((linearSearch(lst, random.randint(0, 999))) / 10000) * 2
        finalA4 += average4

    for i in range(0, 100000):
        average5 = ((linearSearch(lst, random.randint(0, 999))) / 100000) * 2
        finalA5 += average5

    print('Linear search:')
    print('  Tests: 10', '       ', 'Average probes:', format(finalA1, '.1f'))
    print('  Tests: 100', '      ', 'Average probes:', format(finalA2, '.2f'))
    print('  Tests: 1000', '     ', 'Average probes:', format(finalA3, '.3f'))
    print('  Tests: 10000', '    ', 'Average probes:', format(finalA4, '.4f'))
    print('  Tests: 100000', '   ', 'Average probes:', format(finalA5, '.5f'))
    bAverage = 0
    for i in range(0, 999):
        result = (binarySearch(insertionSort(lst), random.randint(0, 999))) / 1000
        bAverage += result

    print('Binary search:')
    print('  Average number of probes:', format(bAverage, '.3f'))
    print('  Differs from log(2)1000:', math.log(1000, 2) - bAverage)


ComparingLinearBinarySearch()

