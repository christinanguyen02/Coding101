# CS 303E Quiz 1D
# Author: Finn Frankis
from math import sqrt

# Problem 1: Isosceles Triangle Area
def isoscelesTriangleArea():
    # convert incoming values to floats immediately
    a = float(input()) 
    b = float(input())

    area = 1/4 * b * sqrt(4 * (a ** 2) - (b ** 2)) # calculate area from a and b
    area_rounded = round(area, 2) # round area to two decimal places

    print("{:.2f}".format(area_rounded)) # print area to two decimal places
    

# Problem 2: Volume Unit Conversion
def volumeUnitConversion():
    tablespoons = int(input()) # convert input tablespoons to integer

    pints = tablespoons // 32 # determine the integer number of pints in the given number of tablespoons
    tablespoons_remaining = tablespoons % 32 # determine how many tablespoons are left after the rest have been converted to pints

    gallons = pints // 8 # determine the integer number of gallons in the remaining number of pints
    pints_remaining = pints % 8 # determine how many pints are left after the rest have been converted to gallons

    print(gallons, pints_remaining, tablespoons_remaining)

