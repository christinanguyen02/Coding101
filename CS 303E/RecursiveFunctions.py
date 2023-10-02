# File: RecursiveFunctions.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 04/26/2021
# Date Last Modified: 04/30/2021
# Description of Program: This program are functions that can be done with class methods
# or iteratively. But, these functions are all done recursively, calling itself to solve the code.

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
    else:
        return n + addToN(n-1)

def findSumOfDigits( n ):
    """ Return the sum of the digits in a non-negative integer. """
    if n == 0:
        return 0
    else:
        return n % 10 + findSumOfDigits(n//10)
        
def decimalToBinary( n ):
    """ Given a nonnegative decimal integer n, return the 
    binary representation as a string. """
    if n <= 1:
        return str(n)
    else:
        return decimalToBinary(n // 2) + decimalToBinary(n % 2) 
        

def decimalToList( n ):
    """ Given a positive decimal integer, return a list of the 
    digits (as strings). """
    string = '0'+ str(n)
    if n < 1:
        return []
    else:
        decList = decimalToList(int(string[1:]))
        decList.append(string[-1])
        return decList
    
    
def isPalindrome( s ):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if len(s) == 0:
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:len(s)-1])
    else:
        return False

def findFirstUppercase( s ):
    """ Return the first uppercase letter in 
    string s, if any.  Return None if there
    is none. """
    if len(s) == 0:
        return
    if s.islower():
        return
    if s[0].isupper():
        return s[0]
    else:
        return findFirstUppercase(s[1:])
    

def findFirstUppercaseIndexHelper( s, index ):
    """ Helper function for findFirstUppercaseIndex. """
    if len(s) == 0:
        return -1
    if s[0].isupper():
        return index
    else:
        return findFirstUppercaseIndexHelper( s[1:], index + 1 )


# The following function is already completed for you.  But 
# make sure you understand what it's doing. 

def findFirstUppercaseIndex( s ):
    """ Return the index of the first uppercase letter in 
    string s, if any.  Return -1 if there is none.  This one 
    requires a helper function, which is the recursive 
    function. """
    return findFirstUppercaseIndexHelper( s, 0 )
