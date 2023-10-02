# Student: Christina Nguyen 
# UT EID: ctn765    
# Course Name: CS303E
# 
# Date Created: 02/20/2020
# Date Last Modified: 02/20/2020
# Description of Program: This program is used to determine the number of days in a given month and year.

# user input to ask for month and year
month = int(input("Enter a month (1-12): "))
year = int(input("Enter a year: "))

# algorithm to determine whether a year is a leap year or not
LeapYear = ( year % 4 == 0 ) and ( not ( year % 100 == 0 ) or ( year % 400 == 0 ))

MonthName = ''

# if statements to assign a month name to its respective number
if month == 1:
    MonthName = 'January'
elif month == 2:
    MonthName = 'February'
elif month == 3:
    MonthName = 'March'
elif month == 4:
    MonthName = 'April'
elif month == 5:
    MonthName = 'May'
elif month == 6:
    MonthName = 'June'
elif month == 7:
    MonthName = 'July'
elif month == 8:
    MonthName = 'August'
elif month == 9:
    MonthName = 'September'
elif month == 10:
    MonthName = 'October'
elif month == 11
    MonthName = 'November'
elif month == 12:
    MonthName = 'December'

# if statements to determine what to print
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print(MonthName, year, "has 31 days")
if month == 4 or month == 6 or month == 9 or month == 11:
    print(MonthName, year, "has 30 days")
if month == 2:
    if LeapYear:
        print(MonthName, year, "has 29 days")
    else:
        print(MonthName, year, "has 28 days")

    
