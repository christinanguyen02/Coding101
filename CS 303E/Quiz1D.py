# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Isosceles Triangle Area
def isoscelesTriangleArea():
    # write your solution to problem 1 here
    import math
    a = float(input())
    b = float(input())
    area = (b/4)*math.sqrt((4*a**2)-(b**2))
    if a and b > 0:
        print(format(area, ".2f"))




# Problem 2: Volume Unit Conversion
def volumeUnitConversion():
    # write your solution to problem 2 here
    import math
    volume = int(input())
    gallon = round((volume/(32*8)))
    galRem = volume%(32*8)
    pt = math.floor((galRem/32))
    tbsp = round(((volume%(32*8))%32))
    if volume >= 0:
        print(gallon, pt, tbsp)
    else:
        print("Invalid Input")




