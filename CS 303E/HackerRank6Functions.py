def sumTwoIntegers():
    integerOne = int(input())
    integerTwo = int(input())
    sum = integerOne + integerTwo
    print(sum)
def sumTwoIntegers():
    integerOne = int(input())
    integerTwo = int(input())
    total = integerOne + integerTwo
    return total
def sumTwoIntegers(num1, num2):
    total = num1 + num2
    print (total)
def sumTwoIntegers(num1, num2):
    return num1 + num2
def displayPattern(n):
    for i in range (1, n + 1):
        for j in range (1, i+1):
            print(j, end = ' ')
        print('')
def sumDigits(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    
    return sum

def daysInYear(year):
    
    IsLeapYear = ( year % 4 == 0 ) and ( not ( year % 100 == 0 ) or ( year % 400 == 0 ) )
    
    if IsLeapYear:
        return 366
    else:
        return 365
        
def daysInDecade(startYear):
    totalDays = 0
    for i in range (0, 10):
        days = daysInYear(startYear + i)
        totalDays += days
    return totalDays
