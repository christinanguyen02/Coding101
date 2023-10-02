# File: Benford.py
# Student: Christina Nguyen 
# UT EID: ctn765
# Course Name: CS303E
# 
# Date Created: 04/22/2021
# Date Last Modified: 04/23/2021
# Description of Program: This program verifies Benford's law from U.S Census data from 2009.
# The program opens and reads the Census data, writing a new file that provides the count for
# the first digit, the percentage, the total population, the unique population, and prints out
# a table in a text file.

import os.path

def main():
    file = input("Enter the name of a file of census data: ")
    if not os.path.isfile(file):
        print("File does not exist")
        return
    populationSet = set()
    digitCount = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, \
                  '6' : 0, '7' : 0, '8' : 0, '9' : 0}
    
    lineCount = runCensus(file, populationSet, digitCount)
    writeFile(digitCount, populationSet, lineCount)
    print("Output written to benford.txt")

def runCensus(file, populationSet, digitCount):
    infile = open(file, "r")
    
    #header line, don't need this
    headerLine = infile.readline()
    line = infile.readline()

    populationList = []
    while line:
        lineList = line.split()
        population = lineList[len(lineList) - 1]
        populationSet.add(population)
        populationList.append(population)
        line = infile.readline()


    for i in populationList:
        numberString = str(i)
        firstDigit = numberString[0]
        digitCount[firstDigit] = digitCount.get(firstDigit) + 1
        
    infile.close()
    return len(populationList)
        
def writeFile(dictionary, populationSet, lineCount):
    outfile = open("benford.txt", "w")
    outfile.write("Total number of cities: %d\n" %lineCount)
    outfile.write("Unique population counts: %d\n" %len(populationSet))
    outfile.write("First digit frequency distributions:\n")
    outfile.write("Digit\tCount\tPercentage\n")
    for key in dictionary:
        percentage = ((dictionary[key] / lineCount) * 100)
        outfile.write("%s\t%d\t%.1f\n" %(key, dictionary[key], percentage))
    outfile.close()

main()
