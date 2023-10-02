# File: ComparingLinearBinarySearch.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 04/14/2021
# Date Last Modified: 04/16/2021
# Description of Program: This program compares the performance of the linear and binary search.
# For linear search a test is run from 0 to 999 and for binary search it tests 1000 times. For linear search
# the averafe is expexted to be half the length of the list and for binary it is the log (base 2) of 1000.

import random
import math

def main():
    lst = [x for x in range (1000)]
    shuffledList = lst
    random.shuffle(shuffledList)
    print ("Linear search:")
    for i in range(1, 6):
        n = 10 ** i
        linearTest(n, shuffledList)
        
    print ("Binary search:")
    binaryTest(lst)
    
def getRandomKey():
    return random.randint(0,999)

def linearTest(n, lst):
    sum = 0
    for i in range (n):
        key = getRandomKey()
        probes = linearSearch(lst, key) + 1
        sum += probes
    average = sum / n
    testForm = format(n, "<8d")
    print("  Tests:",testForm, "Average probes:", average)
        
def binaryTest(lst):
    sum = 0
    for i in range (1000):
        key = getRandomKey()
        probes = binarySearch(lst, key)[1]
        sum += probes
    average = sum / 1000
    print ("  Average number of probes:" , average)
    print ("  Differs from log2(1000) by:", abs(math.log(1000, 2) - average))

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
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)
main()
