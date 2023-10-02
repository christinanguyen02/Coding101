# CS 303E Mock Exam (homework 6)
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Sphere Surface Area
def sphereSurfaceArea():
    # write your solution to problem 1 here
    r = float(input())
    if r >= 0:
        import math
        surfaceArea = 4 * math.pi * (r ** 2)
        print(format(surfaceArea, ".2f"))
    else:
        print("Negative radius entered")

# Problem 2: Make Uppercase
def makeUppercase():
    # write your solution to problem 2 here
    char = input()
    charNumber = ord(char)
    if charNumber in range (97, 123):
        difference = (ord('a') - ord('A'))
        upperCase = chr(ord(char) - difference)
        print(upperCase)
    else:
        print(char)



# Problem 3: Sum Series
def sumSeries():
    # write your solution to problem 3 here
    n = int(input())
    sum = 0
    i = 1
    if n > 1:
        while i < n:
            sum = sum + ((n - 1) * n)
            n -= 1
        print(sum)



# Problem 4: Sort Three Integers
def sortThreeIntegers():
    # write your solution to problem 4 here
    numA = int(input())
    numB = int(input())
    numC = int(input())

    # we're just brute forcing this by checking
    # for every possible order for the inputted integers

    if numA <= numB and numA <= numC: # check that numA is the min
        small = numA
        if numB <= numC: # check that numC is the max
            mid = numB
            big = numC
        else: # numB must be the max
            mid = numC
            big = numB
    elif numB <= numA and numB <= numC: # check that numB is the min
        small = numB
        if numA <= numC: # check that numC is the max
            mid = numA
            big = numC
        else: # numA must be the max
            mid = numC
            big = numA
    else: # numC must be the min
        small = numC
        if numA <= numB: # check that numB is the max
            mid = numA
            big = numB
        else: # numA must be the max
            mid = numB
            big = numA
       print(small, mid, big)
    

# Problem 5: Sum Positive Floats
def sumPositiveFloats():
    # write your solution to problem 5 here
    unit = float(input())
    sum = 0
    while unit != 0:
        if unit > 0:
            sum += unit
        unit = float(input())

    print(format(sum, ".3f"))
        


# Problem 6: Print Squared Table
def printSquaredTable():
    # write your solution to problem 6 here
    number = int(input())
    print ("  n      n**2")
    print ("-------------")
    count = 1
    while count <= number:
        square = count ** 2
        formatNum = format(count, "3d")
        formatSquare = format(square, "10d")
        print(formatNum, formatSquare)
        count +=1



# Problem 7: Largest Square
def largestSquare():
    # write your solution to problem 7 here
    n = int(input())
    import math
    root = math.sqrt(n)
    k = math.floor(root)
    print(k)


# Problem 8: Collatz Conjecture
def collatzConjecture():
    # write your solution to problem 8 here
    n = int(input())
    count = 1
    while n != 1:
        if (n % 2 == 0):
            n = n/2
        else:
            n = (3*n) + 1
        count +=1
    print(count)
            


