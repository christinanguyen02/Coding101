#Quadratic Solutions
a = float(input())
b = float(input())
c = float(input())
import math
discriminant = math.sqrt((b ** 2) - (4*a*c))
rootOne = ((- b + discriminant) / (2 * a))
rootTwo = ((- b - discriminant) / (2 * a))
if a == 0:
    print("The equation has no real roots")
if discriminant >= 0:
    print("The roots are", format(rootOne, "0.3f"), "and", format(rootTwo, "0.3f"))
else:
    print("The equation has no real roots")

#Cramers Rule
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

check = (a * d) - (b * c)

if check == 0:
    print ("The equation has no solution")
else:
    x = ((e * d) - (b * f))/((a * d) - (b * c))
    y = ((a * f) - (e * c))/((a * d) - (b * c))
    print ("x is", format(x, "0.1f"), "and y is", format(y, "0.1f"))

#Compare Costs
weightPackOne = float(input())
pricePackOne = float(input())
weightPackTwo = float(input())
pricePackTwo = float(input())

costOne = weightPackOne / pricePackOne
costTwo = weightPackTwo / pricePackTwo

if costOne > costTwo:
    print("1")
else:
    print("2")
