# CS 303E Quiz 4D


# Problem 1: Classified Correspondence
def classifiedCorrespondence(str):
    answer = ""

    for char in str:
        if char.isupper() or char.isnumeric():
            answer += "X"
        else:
            answer += char

    return answer


# Problem 2: Adjacent Products
def adjacentProducts(lst):

    answer = []

    for i in range(len(lst) - 1):
        answer.append(lst[i] * lst[i + 1])

    return answer

