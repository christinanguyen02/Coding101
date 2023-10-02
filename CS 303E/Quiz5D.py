# CS 303E Quiz 5D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Verbose Vocabulary
def verboseVocabulary(A, B, C):
    # replace pass with your solution for Problem 1
    AandB = A.intersection(B)
    AandC = A.intersection(C)
    BandC = B.intersection(C)
    if (len(AandB) > len(AandC)) and (len(AandB) > len(BandC)):
        return AandB
    if (len(AandC) > len(AandB)) and (len(AandC) > len(BandC)):
        return AandC
    if (len(BandC) > len(AandC)) and (len(BandC) > len(AandB)):
        return BandC

# Problem 2: Get Grades
def getGrades(lst):
    # replace pass with your solution for Problem 2
    import math
    d = {}
    for x in lst:
        name = x[0]
        midtermOne = x[1]
        midtermTwo = x[2]
        midtermThree = x[3]
        final = x[4]
        averageMidterm = ((midtermOne + midtermTwo + midtermThree) / 3)
        if averageMidterm > final:
            final = averageMidterm
        test1 = (midtermOne * .20)
        test2 = (midtermTwo * .20)
        test3 = (midtermThree * .20)
        test4 = (final * .40)
        classAverage = math.floor(test1 + test2 + test3 + test4)
        d[name] = classAverage
    return d

if __name__ == "__main__":
    # uncomment the following lines to run the given test cases

    print(
         verboseVocabulary(
             {"apple", "orange", "lemon", "grape"},
             {"apple", "kiwi", "strawberry"},
             {"strawberry", "lemon", "orange", "pineapple", "kiwi", "grape"},
         )
     )
    print(verboseVocabulary({"a", "b"}, {"c", "e"}, {"a", "b", "c", "d"}))
    print(verboseVocabulary({"x", "y", "z"}, {"x"}, {"y", "x"}))

    print(
         getGrades(
             [
                 ("Spongebob", 84, 87, 92, 82),
                 ("Patrick", 25, 30, 20, 25),
                 ("Sandy", 96, 95, 100, 99),
             ]
         )
     )
    print(getGrades([]))
    print(getGrades([("Squidward", 80, 90, 65, 0), ("Plankton", 20, 20, 100, 100)]))
    pass

