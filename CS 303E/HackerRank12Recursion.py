def cleanString(string):
    if len(string) <= 1:
        return string
    else:
        if string[0] == string[1]:
            return cleanString(string[1:])
        else:
            return string[0] + cleanString(string[1:])

def stringWithStars(string):
    if len(string) <= 1:
        return string
    else:
        return stringWithStars(string[0]) + '*' + stringWithStars(string[1:])

def removeNegatives(lst):
    posList = []
    if len(lst) == 0:
        return posList
    else:
        if lst[0] >= 0:
            posList.append(lst[0])
            return posList + removeNegatives(lst[1:])
        else:
            return removeNegatives(lst[1:])

def collatzLength(num):
    count = 1
    if num <= 1:
        return count
    if num % 2 == 0:
        count = 1
        return count + collatzLength(num // 2)
    else: 
        count = 1
        return count + collatzLength(3 * num + 1)

def maxInList(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        if lst[0] < lst[1]:
            return maxInList(lst[1:])
        else:
            lst.remove(lst[1])
            return maxInList(lst)

def stringCharacterSet(string):
    stringSet = set()
    if len(string) == 0:
        return stringSet
    else:
        stringSet = stringCharacterSet(string[1:])
        stringSet.add(string[0])
        return stringSet

def occurrenceCounts(lst):
    dictionary = {}
    if len(lst) == 0:
        return dictionary
    else: 
        dictionary = occurrenceCounts(lst[1:])
        if lst[0] in dictionary:
            dictionary[lst[0]] = dictionary[lst[0]] + 1
        elif lst[0] not in dictionary:
            dictionary[lst[0]] = 1
        return dictionary

def countUpperLower(string):
    if len(string) == 0:
        return 0, 0 
    if string[0].islower():
        lower = 1
    else:
        lower = 0
    if string[0].isupper():
        upper = 1
    else:
        upper = 0
    
    rec1, rec2 = countUpperLower(string[1:])
    return (rec1 + upper, rec2 + lower)

def bumpUpToEven(lst):
    newLst = []
    if len(lst) == 0:
        return lst
    else: 
        if lst[0] % 2 != 0:
            newLst.append(lst[0] + 1)
            return newLst + bumpUpToEven(lst[1:])
        else:
            newLst.append(lst[0])
            return newLst + bumpUpToEven(lst[1:])

def recursiveSumSeries(n):
    sum = 0
    if n == 0:
        return sum
    else:
        sum += n/(n+1)
        return sum + recursiveSumSeries(n -1)
