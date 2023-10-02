# File: MyStringFunctions.py
# Student: Christina Nguyen 
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 03/31/2021
# Date Last Modified: 04/02/2021
# Description of Program: This program contains a library of functions that implements
# different manipulations of strings and characters.

def myAppend( str, ch ):
    # Return a new string that is like str but with 
    # character ch added at the end
    return str + ch

def myCount( str, ch ):
    # Return the number of times character ch appears
    # in str.
    count = 0
    for i in str:
        if i == ch:
            count += 1
    return count
    

def myExtend( str1, str2 ):
    # Return a new string that contains the elements of
    # str1 followed by the elements of str2, in the same
    # order they appear in str2.
    return str1 + str2

def myMin( str ):
    # Return the character in str with the lowest ASCII code.
    # If str is empty, print "Empty string: no min value"
    # and return None.
    if len(str) == 0:
        print("Empty string: no min value")
        return None
    chMin = ord(str[0])
    for i in str:
        ascNum = ord(i)
        if ascNum < chMin:
            chMin = ascNum
    return(chr(chMin))
    
        
def myInsert( str, i, ch ):
    # Return a new string like str except that ch has been
    # inserted at the ith position.  I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of str and return None.
    if i > len(str):
        print("Invalid index")
    else:
        return str[:i] + ch + str[i:]

def myPop( str, i ):
    # Return two results: 
    # 1. a new string that is like str but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(str), and return str unchanged and None
    if i >= len(str):
        print("Invalid index")
        return str, None
    else:
        ithCh = str[i]
        return str[:i] + str[i+1:], ithCh

def myFind( str, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    indexCh = -1
    index = 0
    while index < len(str):
        if str[index] == ch:
            indexCh = index
            break
        index += 1
    return indexCh

def myRFind( str, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in str, if any.  Return -1 if ch does not occur in str.
    indexCh = -1
    index = len(str) - 1
    while index >= 0:
        if str[index] == ch:
            indexCh = index
            break
        index -= 1
    return indexCh

def myRemove( str, ch ):
    # Return a new string with the first occurrence of ch 
    # removed.  If there is none, return str.
    indexCh = -1
    index = 0
    while index < len(str):
        if str[index] == ch:
            indexCh = index
            break
        index += 1
    if indexCh == -1:
        return str
    return str[:indexCh] + str[indexCh+1:]

def myRemoveAll( str, ch ):
    # Return a new string with all occurrences of ch.
    # removed.  If there are none, return str.
    if ch not in str:
        return str
    index = 0
    myStr = str
    while index < len(str):
        if str[index] == ch:
            myStr = str[:index] + str[index+1:]
            str = myStr
        index += 1
    return myStr

def myReverse( str ):
    # Return a new string like str but with the characters
    # in the reverse order.
    reverse = ""
    index = len(str)
    while index > 0:
        reverse += str[index - 1]
        index = index - 1
    return reverse
        
