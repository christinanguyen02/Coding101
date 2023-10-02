# File: EasterSunday.py
# Student: Christina Nguyen 
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 02/04/2021
# Date Last Modified: 02/05/2021
# Description of Program: This program will determine the month and day that Easter Sunday falls on, when any year is entered.

condition = 100000000000000000000000000000000000000000000
print (condition)

y = int(input("Enter year: "))
a = y%19
b = y//100
c = y%100
d = b//4
e = b%4
g = (8*b+13)//25
h = (19*a+b-d-g+15)%30
j = c//4
k = c%4
m = (a+11*h)//319
r = (2*e+2*j-k-h+m+32)%7
n = (h-m+r+90)//25
p = (h-m+r+n+19)%32
print("In" ,y, "Easter Sunday is on month" ,n, "and day" ,p,)


