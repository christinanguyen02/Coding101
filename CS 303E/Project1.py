# File: Project1.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 03/21/2021
# Date Last Modified: 03/24/2021
# Description of Program: The program is suppose to compute a student's semester grade with the 3 homeworks,
# 2 exams, and 2 projects.

#input student name
print("")
name = input("Enter the student's name: ")

#homeworks
print("")
print("HOMEWORKS:")
hwCount = 1
hwTotal = 0
while (hwCount <= 3):
    hwScore = int(input("  Enter HW%i grade: " % hwCount))
    while hwScore > 10 or hwScore < 0:
        print("  Grade must be in range [0..10]. Try again.")
        hwScore = int(input("  Enter HW%i grade: " % hwCount))
    hwCount += 1
    hwTotal += hwScore

#projects
print("")
print("PROJECTS:")
proCount = 1
proTotal = 0
while (proCount <= 2):
    proScore = int(input("  Enter Project%i grade: " % proCount))
    while proScore > 100 or proScore < 0:
        print("  Grade must be in range [0..100]. Try again.")
        proScore = int(input("  Enter Project%i grade: " % proCount))
    proCount += 1
    proTotal += proScore

#exams
print("")
print("EXAMS:")
examCount = 1
examTotal = 0
while (examCount <= 2):
    examScore = int(input("  Enter Exam%i grade: " % examCount))
    while examScore > 100 or examScore < 0:
        print("  Grade must be in range [0..100]. Try again.")
        examScore = int(input("  Enter Exam%i grade: " % examCount))
    examCount += 1
    examTotal += examScore

#averages
hwAverage = (hwTotal / 3) * 10
proAverage = proTotal / 2
examAverage = examTotal / 2
courseAverage = (hwAverage * 0.3) + (proAverage * 0.3) + (examAverage * 0.4)

#letter grade
if courseAverage >= 90:
    letter = 'A'
elif courseAverage >= 80:
    letter = 'B'
elif courseAverage >= 70:
    letter = 'C'
elif courseAverage >= 60:
    letter = 'D'
else:
    letter = 'F'

#formatting
hwFormat = (format(hwAverage, "0.2f"))
proFormat = (format(proAverage, "0.2f"))
examFormat = (format(examAverage, "0.2f"))
courseFormat = (format(courseAverage, "0.2f"))

#print statements
print("")
print("Grade report for:", name)
print("  Homework average (30% of grade):", hwFormat)
print("  Project average (30% of grade):", proFormat)
print("  Exam average (40% of grade):", examFormat)
print("  Student course average:", courseFormat)
print("  Course grade (CS303E: Spring, 2021):", letter)
print("")
