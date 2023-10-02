#The function should create and return a set of the names of
#all players who have scored at least 10 goals in each of the last three seasons.
def eliteGoalScorers(lst):
    names = set()
    for x in lst:
        player = x[0]
        lstScore = x[1:]
        goal1 = lstScore[0]
        goal2 = lstScore[1]
        goal3 = lstScore[2]
    
        if goal1 >= 10 and goal2 >= 10 and goal3 >= 10:
            names.add(player)
    return names

#The function should create and return a dictionary where the keys are the names
#of players and the values are the number of goals that player scored in their best season.
def bestPerformingSeason(lst):
    # Write your code here
    playerScores = {}
    
    for i in lst:
        player = i[0]
        scoreList = i[1:]
        goal1 = scoreList[0]
        goal2 = scoreList[1]
        goal3 = scoreList[2]
        playerScores[player] = max(goal1, goal2, goal3)
    return playerScores

# The function should create and return a set of the names of all players who were
#able to accomplish all three of these feats.
def topTennisPlayers(s1, s2, s3):
    s1s2Inter = s1.intersection(s2)
    s1s3Inter = s1.intersection(s3)
    if s1s2Inter == s1s3Inter:
        return s1s2Inter
    else:
        return set()

#The function should create and return a set of the names of all players
#who were able to accomplish any of these feats.
def prettyGoodTennisPlayers(s1, s2, s3):
    goodTennis = set()
    for i in s1:
        goodTennis.add(i)
    for x in s2:
        goodTennis.add(x)
    for n in s3:
        goodTennis.add(n)
    return goodTennis


#Complete the following function which accepts a set of points (i.e.
#two-element tuples, where the first element is the x-coordinate and the second
#element is the y-coordinate) and returns the rightmost lowest point.
def rightmostLowestPoint(s):
    lowest = float('inf')
    rightmost = float('-inf')
    
    for x in s:
        if x[1] <= lowest:
            lowest = x[1]
            if x[0] > rightmost:
                rightmost = x[0]
    return (rightmost, lowest)


#The function should compute and return the sum of all the values whose keys are in the given set.
def sumValuesForGivenKeys(s, d):
    sum = 0
    keys = d.keys()
    for x in s:
        if x in keys:
            sum += d[x]
    return sum

#Your function should create and return a dictionary whose keys are the pairs given
#in the list and whose values are the least common multiples of the two numbers in
#each pair. Recall that the least common multiple of two integers a and b is the
#smallest positive integer which is divisible by both a and b.
def lcmDict(lst):
    dictionary = {}
    for x in lst:
        a = x[0]
        b = x[1]
        if a > b:
            c = a
        else:
            c = b
        while (True):
            if ((c % a == 0) and (c % b == 0)):
                lcm = c
                break
            c += 1
        dictionary[x] = lcm
    return dictionary

#Your function should create and return a dictionary whose keys are the numbers in the given set.
#Each integer key in the dictionary should have as its value the second-smallest divisor of the
#number (notice that every number technically has one as its smallest divisor).
def secondSmallestDivDict(s):
    # Write your code here
    dictionary = {}
    for x in s:
        divList = []
        i = 1
        while i <= x:
            if (x % i == 0):
                divList.append(i)
            i += 1
        dictionary[x] = divList[1]
    return dictionary

# Your function should create and return a dictionary whose keys are all the letters of the alphabet
#(use the uppercase versions for the keys) and whose values are pairs of integers, where the first integer
#corresponds to the number of times the lowercase version of that letter appears in the string and the
#second integer corresponds to the number of times the uppercase version of that letter appears in the string.
def upperLowerLettersDict(str):
    d = {}
    for i in range(65, 91):
        d[chr(i)] = [0,0]
    for x in str:
        if x.isupper():
            d[x][1] += 1
        elif x.islower():
            d[x.upper()][0] += 1
    for s in d:
        d[s] = tuple(d[s])
    return d
