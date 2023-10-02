def removeNegatives(lst):
    posList = []
    if len(lst) == 0:
        return posList
    else:
        if lst[0] > 0:
            posList.append(lst[0])
            return posList + removeNegatives(lst[1:])
        else:
            return removeNegatives(lst[1:])


