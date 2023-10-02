# File: MinMax.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 03/04/2021
# Date Last Modified: 03/04/2021
# Description of Program: This program is a loop that takes numbers entered and
# prints out the maximum and minimum integers when "stop" is entered.

import math
value = ''
stoppedInstantly = False
count = 1

while (value != 'stop'):
    value = input("Enter an integer or 'stop' to end: ")

    if (value == 'stop'):
        if (count == 1):
            stoppedInstantly = True
        break
        
    valueInt = int(value)

    if (count == 1):
        maxi = valueInt
        mini = valueInt
    else:
        maxi = max(valueInt, maxi)
        mini = min(valueInt, mini)
    count += 1

if (stoppedInstantly == True):
    print("You didn't enter any numbers")
else:
    print("The maximum is", maxi)
    print("The minimum is", mini)
