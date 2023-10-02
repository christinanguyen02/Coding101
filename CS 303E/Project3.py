# File: Project3.py
# Student: Christina Nguyen
# UT EID: ctn765    
# Course Name: CS303E
# 
# Date Created: 04/26/2021
# Date Last Modified: 05/02/2021
# Description of Program: This program takes information about Covid-19 cases and deaths
# in Texas counties and state. The program runs a loop with commands that allow for the user
# to access cases, deaths, help, and a list of counties.

import os.path

#function to read file and create dictionary and list
def readFile(file):
    countiesList = []
    d = {}
    deathSum = 0
    confirmedSum = 0

    infile = open("county-covid-data.txt", "r")

    line = infile.readline()

    while line:
        lineParse = line.split(",")
        countyName = lineParse[0]
        if ord(countyName[0]) == 35:
               line = infile.readline()
        else:
            countiesList.append(countyName)
            confirmedCases = int(lineParse[1])
            confirmedSum += confirmedCases
            probableCases = lineParse[2]
            deaths = int(lineParse[3])
            deathSum += deaths
            d[countyName] = confirmedCases, deaths
            line = infile.readline()
    d["Texas"] = confirmedSum, deathSum
    return d, countiesList
    infile.close()
    
def main():
    
#check that the input file exists
    if not os.path.isfile("county-covid-data.txt"):
        print("File county-covid-data.txt not found.")
        return
    data = readFile("county-covid-data.txt")
    d = data[0]
    countiesList = data[1]

#print messages for the welcoming
    print("\nWelcome to the Texas Covid Database Dashboard.\nThis provides\
 Covid data in Texas as of 1/26/21.\nCreating dictionary from file:\
 county-covid-data.txt")
    print("\nEnter any of the following commands:")
    print("Help - list available commands;\nQuit - exit this dashboard;\n\
Quit - exit this dashboard;\nCounties - list all Texas counties;\n\
Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\n\
Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")

#loop for commands 
    command = ''
    while command != 'quit':

        command = input("\nPlease enter a command: ").lower()
        # Parse the command into a list of words (assuming there's no punctuation).
        commWords = command.split()
        # Extract the first word in the command (which is always a one-word command):
        comm = commWords[0]
        # Extract the rest of the words and re-assemble them into a single string, 
        # separated by spaces. 
        args = commWords[1:]
        arg = " ".join(args)
        
        if comm == 'help':
            print("Help - list available commands;\nQuit - exit this dashboard;\n\
Quit - exit this dashboard;\nCounties - list all Texas counties;\n\
Cases <countyName>/Texas - confirmed Covid cases in specified county or statewide;\n\
Deaths <countyName>/Texas - Covid deaths in specified county or statewide.")

        elif comm == 'counties':
            onLine = 0
            for x in countiesList:
                print(format(x), end = ', ')
                onLine += 1
                if onLine == 10:
                    print()
                    onLine = 0
            print()
        elif comm == 'cases':
            if arg == 'texas':
                print("Texas total confirmed Covid cases:", d["Texas"][0])
            elif arg not in str(countiesList).lower():
                print("County %s is not recognized." %arg.title())
            else:
                for key in d:
                    if arg == key.lower():
                        print("%s county has %d confirmed Covid cases." %(key, d[key][0]))

        elif comm == 'deaths':
            if arg == 'texas':
                print("Texas total confirmed Covid deaths:", d["Texas"][1])
            elif arg not in str(countiesList).lower():
                print("County %s is not recognized." %arg.title())
            else:
                for key in d:
                    if arg == key.lower():
                        print("%s county has %d fatalities." %(key, d[key][1]))
           
        elif comm != 'quit':
            print("Command is not recognized.  Try again!")
    print("Thank you for using the Texas Covid Database Dashboard.  Goodbye!")

main()
