# CS 303E Quiz 2D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Is Punctuation
def isPunctuation():
    # write your solution to problem 1 here
    punc = input()
    if (punc == '!' or punc == '?' or punc == '.' or punc ==',' or punc == ';' or punc == ':'):
        print("That is a punctuation.")
    else:
        print("That is not a punctuation.")

# Problem 2: Calculate Restaurant Bill
def calculateRestaurantBill():
    # write your solution to problem 2 here
    meal = input()
    dessert = input()
    #meal pricing
    if (meal == 'Spaghetti'):
        price = 15
    elif (meal == 'Cheeseburger'):
        price = 5
    elif (meal == 'Hotdog'):
        price = 2
    elif (meal == 'Sandwich'):
        price = 7
    elif (meal == 'Pizza'):
        price = 20
    #dessert pricing
    if (dessert == 'Cheesecake'):
        priceTwo = 6
    else:
        priceTwo = 12

    print(price + priceTwo)
    
    
