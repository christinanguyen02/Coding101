# CS 303E Quiz 2D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Is Punctuation
def isPunctuation():
    # write your solution to problem 1 here
    char = input()
    if char == '!' or char == '?' or char == '.' or char == ',' or char == ':' or char == ';':
        print("That is a punctuation.")
    else:
        print("That is not a punctuation.")


# Problem 2: Calculate Restaurant Bill
def calculateRestaurantBill():
    # write your solution to problem 2 here
    meal = input()
    dessert = input()
    total = 0
    if meal == 'Spaghetti':
        total += 15
    elif meal == 'Cheeseburger':
        total += 5
    elif meal == 'Hotdog':
        total += 2
    elif meal == 'Sandwich':
        total += 7
    elif meal == 'Pizza':
        total += 20

    if dessert == 'Cheesecake':
        total += 6
    elif dessert == 'Tiramisu':
        total += 12

    print(total)
