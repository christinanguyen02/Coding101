# CS 303E Exam 1C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1 - Octagonal Order
def octagonalOrder():
    # replace pass with your solution to problem 1 here
    k = int(input())
    for i in range(1, k + 1):
        octagonal = 3 * i * i - 2 * i
        print(octagonal, end = " ") 

# Problem 2 - Stylish Sum
def stylishSum():
    # replace pass with your solution to problem 2 here
    k = int(input())
    sum = 0
    import math
    for i in range(1, k+1):
        sum += math.sqrt(i) / ((i+7) ** 2)
    print(format(sum, "0.2f"))

# Problem 3 - Affable Average
def affableAverage():
    # replace pass with your solution to problem 3 here
    d = int(input())
    sum = 0
    count = 0
    for i in range(1, 51):
        if i % d == 0:
            sum += i
            count += 1
            average = sum / count
        else:
            average = 0.0
        i += 1
    print(average)

    
# Problem 4 - The Wienni Walkabout
def theWienniWalkabout():
    # replace pass with your solution to problem 4 here
    l = int(input())
    a = int(input())
    if a > l:
        for i in range(0, 5):
            sequence = a
            a = (3 * a + 3)
            print(sequence, end = ' ')
    elif a < l:
        for i in range(0, 5):
            sequence = a
            a = (8 * a - 3)
            print(sequence, end = ' ')
    elif a == l:
        for i in range(0, 5):
            sequence = a
            a = (a - 2) ** 2
            print(sequence, end = ' ')


# Problem 5 - Coin Conundrum
def coinConundrum():
    # replace pass with your solution to problem 5 here
    amount = int(input())
    coinOne = amount // 60
    leftOne = amount % 60
    coinTwo = leftOne // 12
    leftTwo = leftOne % 12
    coinThree = leftTwo // 3
    leftThree = leftTwo % 3
    coinFour = leftThree // 1
    total = (coinOne + coinTwo + coinThree + coinFour)
    print(total)
    
# Problem 6 - Versatile Vowel
def versatileVowel():
    # replace pass with your solution to problem 6 here
    letter = input()
    asciiLetter = ord(letter)
    if asciiLetter >= 65 and asciiLetter <= 68:
        vowel = chr(69)
        print(vowel)
    elif asciiLetter > 68 and asciiLetter <= 72:
        vowel = chr(69)
        print(vowel)
    elif asciiLetter > 72 and asciiLetter <= 78:
        vowel = chr(73)
        print(vowel)
    elif asciiLetter > 78 and asciiLetter <= 84:
        vowel = chr(79)
        print(vowel)
    elif asciiLetter > 84 and asciiLetter <= 90:
        vowel = chr(85)
        print(vowel)
    
# Problem 7 - Tiered Taxation
def tieredTaxation():
    # replace pass with your solution to problem 7 here
    income = int(input())
    if income > 0 and income < 10000:
        tax = 10000 * 0.00
        print(format(tax, ".0f"))
    elif income > 10000 and income < 20000:
        left = income - 10000
        tax = (10000 * 0.00) + (left * 0.10)
        print(format(tax, ".0f"))
    elif income > 20000 and income < 1000000:
        left = income - 20000
        tax = (10000 * 0.00) + (10000 * 0.10) + (left * 0.20)
        print(format(tax, ".0f"))


# Problem 8 - Opportunistic Operation
def opportunisticOperation():
    # replace pass with your solution to problem 8 here
    x = int(input())
    y = int(input())
    if (x - y) > 100:
        quotient = x / y
        print(format(quotient, "0.2f"))
    else:
        difference = x - y
        print(format(difference, "0.2f"))

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    #octagonalOrder()
    #stylishSum()
    #affableAverage()
    #theWienniWalkabout()
    #coinConundrum()
    #versatileVowel()
    #tieredTaxation()
    #opportunisticOperation()  
    pass
