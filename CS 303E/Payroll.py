# File: Payroll.py
# Student: Christina Nguyen
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 02/12/2020
# Date Last Modified: 02/12/2020
# Description of Program: This program prints the payroll sheet when hourly wage, hours worked, the federal tax rate, and state tax rate is entered.
# The program calculates the gross pay, deductions with the tax rates, total deduction, and the net pay.

y = input("Enter employee's name: ")
x = float(input("Enter number of hours worked in a week: "))
a = float(input("Enter hourly pay rate: "))
b = float(input("Enter federal tax withholding rate: "))
c = float(input("Enter state tax witholding rate: "))
grossPay = float(a*x)
federalWithholding = grossPay*b
stateWithholding = grossPay*c
bPercent = format(b*100, ".1f")
cPercent = format(c*100, ".1f")
total = federalWithholding+stateWithholding
net = grossPay-total
print("")
print("Employee Name:",y)
print("Hours Worked:",x)
print("Pay Rate: $",format(a,".2f"), sep="")
print("Gross Pay: S",format(grossPay,".2f"), sep="")
print("Deductions:")
print("  Federal Withholding("+bPercent, "%): $", format(federalWithholding,".2f"), sep="")
print("  State Withholding("+cPercent, "%): $", format(stateWithholding,".2f"), sep="")
print("  Total Deduction: $", format(total,".2f"), sep="")
print("Net Pay: $", format(net,".2f"), sep="")
