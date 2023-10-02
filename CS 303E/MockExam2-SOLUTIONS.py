# CS 303E Mock Exam 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

import math

# Problem 1 - Student Class
# DO NOT CHANGE ANYTHING IN THE COURSE CLASS
class Course:
    """A course with a name, professor, and number of credit hours"""
    def __init__(self, name, professor, hours):
        """Create a new course with the given name (a string), professor (a string), and hours (an integer)"""
        self.__name = name
        self.__professor = professor
        self.__hours = hours
    
    def getName(self):
        """Returns the name of this course"""
        return self.__name
    
    def getProfessor(self):
        """Returns the professor for this course"""
        return self.__professor
    
    def getHours(self):
        """Returns the number of credit hours this course counts for"""
        return self.__hours
    
    def __str__(self):
        """Returns the string representation of this course"""
        return "{} with {}".format(self.__name, self.__professor)

# Complete the Student class below
class Student:
    def __init__(self, name, year, major, courses):

        # .__ or ._ necessary to make private

        self._name = name
        self._year = year
        self._major = major
        self._courses = courses

    def numCourses(self):
        return len(self._courses)

    def isUpperClassman(self):
        return self._year >= 3

    def totalHours(self):
        
        hours = 0
        for course in self._courses:

            hours += course.getHours()
        
        return hours

    def __str__(self):  

        if self._year == 1:
            year = "freshman"
        elif self._year == 2:
            year = "sophomore"
        elif self._year == 3:
            year = "junior"
        else:
            year = "senior"

        return f"{self._name} is a {year} {self._major} major."


# Problem 2 - ASCII List to String
def asciiListToString(lst):

    res = ""
    for code in lst:
        res += chr(code)
    return res

# Problem 3 - Essay Character Count
def essayCharacterCount(sentence, words):

    # convert each word in words to be lowercase

    lowercase_words = set()
    for word in words:
        lowercase_words.add(word.lower())

    # then you can either do it more compactly:

    sentence_words = set(sentence.lower().split())

    valid_words = sentence_words.difference(lowercase_words)

    count = 0
    for word in valid_words:
        count += len(word)

    return count

    # or you could do it something like:
    #
    # count = 0
    # sentence = sentence.lower().split()

    # for word in sentence:
    #     if word not in lowercase_words:
    #         count += len(word)
    # return count

# Problem 4 - List of Perfect Squares
def isPerfectSquare(num):

    sqrt = math.sqrt(num)

    # True if is perfect square, False otherwise
    return sqrt == int(sqrt)

def listOfPerfectSquares(lst):

    is_perfect_list = []
    for item in lst:

        is_perfect_list.append(isPerfectSquare(item))

    return is_perfect_list

# Problem 5 - Character Index Dictionary
def characterIndexDictionary(string):

    dictionary = {}    
    for i in range(len(string)):

        ch = string[i]

        # only create entry if ch hasn't been seen yet
        if ch not in dictionary:
            dictionary[ch] = i

    return dictionary

# Problem 6 - Set of Common Factors
def setOfCommonFactors(tup):

    # no number greater than the min
    # can be a factor of the min

    min_val = min(tup)
    factors = set() 

    # min_val can be a factor
    # % 0 will cause an error, so skip it
    for i in range(1, min_val + 1):   

        factor_for_all = True

        # check until we find a number in tup
        # that does not have a factor of i
        for num in tup:
            if num % i != 0:
                factor_for_all = False
                break
        
        if factor_for_all:
            factors.add(i)

        # another way of doing it could be
        #
        # num_factors = 0
        #
        # for num in tup:
        #     if num % i == 0:
        #         num_factors += 1
        #
        # if num_factors == len(tup):
        #     factors.add(i)

    return factors
            
# Problem 7 - Recursive Count Digits
def countDigits(string):
    
    # base case
    if len(string) == 0:
        return 0

    # general cases
    if string[0].isdigit():
        count = 1
    else:
        count = 0
    return count + countDigits(string[1:])

# Problem 8 - Recursive Divisible by 3 and 5
def divBy3And5(lst):

    if len(lst) == 0:
        return 0, 0

    # general cases

    # check the current number lst[0]
    # for divisibility by 3 or 5
    if lst[0] % 3 == 0:
        this_3 = 1
    else:
        this_3 = 0

    if lst[0] % 5 == 0:
        this_5 = 1
    else:
        this_5 = 0

    # get the divisibility data for the rest of lst
    by_3, by_5 = divBy3And5(lst[1:])

    # create a new tuple that aggregates the previous values
    return (by_3 + this_3, by_5 + this_5)

if __name__ == '__main__':
    # uncomment the following lines to run the given test cases

    # s = Student('Candice', 1, 'Chemistry', [Course('CH 301', 'Laude', 3), \
    #     Course('CS 303E', 'Young', 3), Course('UGS 303', 'Murry', 3), \
    #     Course('M 408C', 'Davis', 4), Course('GOV 310L', 'Moser', 3)])
    # print(s.isUpperClassman())
    # print(s.numCourses())
    # print(s.totalHours())
    # print(str(s))

    # print(asciiListToString([72, 101, 108, 108, 111]))
    # print(asciiListToString([]))
    # print(asciiListToString([123, 116, 114, 51, 51, 32, 37, 33, 125]))

    # print(essayCharacterCount('In conclusion the United States of America is a country', \
    #     {'the', 'a', 'an', 'at', 'but', 'by', 'in', 'for', 'of', 'on', 'to'}))
    # print(essayCharacterCount('Ultimately we shall see that history is not my strongest subject', \
    #     {'this', 'that', 'these', 'those', 'I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', \
    #     'him', 'her', 'us', 'them', 'my', 'his', 'hers'}))
    # print(essayCharacterCount('nOne Of thiS actually cOuntS', {'words', 'actually', 'are', \
    #     'none', 'of', 'your', 'business', 'this', 'counts', 'as', 'poetry'}))

    # print(isPerfectSquare(16))
    # print(isPerfectSquare(29))
    # print(listOfPerfectSquares([8, 55, 49, 1, 121, 77, 14, 65, 64, 21, 25, 49]))

    # print(characterIndexDictionary('Hello World!'))
    # print(characterIndexDictionary(''))
    # print(characterIndexDictionary('CS303E is fun CS303E is fun CS303E is fun'))

    # print(setOfCommonFactors((50, 100)))
    # print(setOfCommonFactors((18,)))
    # print(setOfCommonFactors((210, 770, 2730, 1015)))

    # print(countDigits('Ab1cD234EfG56H7'))
    # print(countDigits(''))
    # print(countDigits('CS303E is fun :D'))

    # print(divBy3And5([15, 9, 7, 5, 3]))
    # print(divBy3And5([]))
    # print(divBy3And5([32, 47, -200, 5, 20]))


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT