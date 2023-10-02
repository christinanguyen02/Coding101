# File: Student.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 03/24/2021
# Date Last Modified: 03/26/2021
# Description of Program: This program defines a student class with student name and two exam grades.
# If no exam grade is given initially none is printed out, and the average can be calculated with the two exams given.
# If both exams are not entered, it will print "Some Exam grades are not available".

class Student:
#define the initializer
    def __init__(self, name, Exam1 = 'None', Exam2 = 'None'):
        self.__name = name
        self.__Exam1 = Exam1
        self.__Exam2 = Exam2

#return the string
    def __str__(self):
        return "Student: " + str(self.__name) + "\n  Exam1: " + str(self.__Exam1) + "\n  Exam2: " + str(self.__Exam2)

#getters and setters
    def getName(self):
        return self.__name

    def getExam1Grade(self):
        if self.__Exam1 == 'None':  
          pass
        else:
            return self.__Exam1
    
    def setExam1Grade(self, Exam1):
        self.__Exam1 = Exam1
    
    def getExam2Grade(self):
        return self.__Exam2 
        
    def setExam2Grade(self, Exam2):
        self.__Exam2 = Exam2

    def getAverage(self):
        if (self.__Exam1 == 'None' or self.__Exam2 == 'None'):
            print ("Some exam grades not available.")
        else:
            return ((self.__Exam1 + self.__Exam2) / 2)
        
