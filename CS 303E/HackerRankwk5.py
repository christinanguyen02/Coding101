#Display Next Character
#n = input()
#asciiCode = ord(n)
#for i in range(asciiCode + 1, asciiCode + 11):
    #letter = chr(i)
    #print(letter, end = ' ',)
#Count Positive and Negative Numbers
#value = int(input())
#posValue = 0
#negValue = 0
#while value != 0:
    #if value > 0:
        #posValue += 1
        #value = int(input())
    #else:
        #negValue += 1
        #value = int(input())
#print(posValue, negValue)
#Odd Fractions Series
#n = int(input())
#sum = 0
#for i in range (1, n+1):
    #sum += (2*i - 1) / (2*i + 1)
#print(format(sum, "0.2f"))
#Arbitrary Time Compound Value
#saving = float(input())
#months = int(input())
#total = 0
#for i in range(1, months + 1):
    #total = ((saving + total) * (1.02))
#print("$",format(total, ".2f"), sep = '')
#Sum Divisors
#n = int(input())
#i = 1
#sum = 0
#while i <= n:
    #if n % i == 0:
        #sum += i
    #i = i + 1
#print(sum)
#Reciporocal Root Sum Series
n = int(input())
sum = 0
import math
for i in range(1, n+1):
    sum += 1 /(math.sqrt(i) + math.sqrt(i+1))
print(format(sum, "0.2f"))
#Maximum Change
value = int(input())
maxCount = 1
import math
while value != 0:
    maxi = value
    value = int(input()
    if (value > maxi):
        maxi = max(maxi, value)
    maxCount += 1
print(maxCount)
   
