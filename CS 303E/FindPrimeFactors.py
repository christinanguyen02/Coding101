# File: FindPrimeFactors.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 04/08/2021
# Date Last Modified: 04/09/2021
# Description of Program: This program takes in a positive integer and prints out the prime factorization of the number.
# If the number is negative, it will not work. If zero is entered, the loop will end. 

import math

def main():
    num = -1
    print("Find Prime Factors:")
    while (num != 0):
        num = int(input("Enter a positive integer (or 0 to stop): "))
        if num == 0:
            print("Goodbye!")
            break
        
        if (num == 1):
            print("  1 has no prime factorization.\n")

        if (num < 0):
            print("  Negative integer entered.  Try again.\n")

        elif (num > 1):
            unchangedNum = num
            if isPrime(num) == True:
                factors = [num]
            else:
                factors = []
                divisor = 2
                while num > 1:
                    while (num % divisor == 0):
                        factors.append(divisor)
                        num = num / divisor
                    divisor = findNextPrime(divisor)
            print("  The prime factorization of %d is: " %unchangedNum + str(factors) + "\n")
    

def isPrime(num):
    if (num < 2 or num % 2 == 0):
        return (num == 2)
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findNextPrime (num):
    if (num < 2):
        return 2
    if (num % 2 == 0):
        num -= 1
    guess = num + 2

    while (not isPrime(guess)):
        guess += 2
    return guess

main()
