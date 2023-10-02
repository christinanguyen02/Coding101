# CS 303E Quiz 3D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: Fancy Functions
def followsRule(num):
    import math
    num = int(num)
    root = round(math.sqrt(num))
    if (root * root == num):
    #if (math.sqrt(num) ** 2 == num):
        return True
    else:
        return False

def rangeOfNums(lower, upper):
    import math
    count = 0
    for i in range(lower, upper + 1):
        if followsRule(i) == True:
            count += 1
    return count
    


# Problem 2: Phone Class
class Phone:
    def __init__(self, brand, volume=5):
        self.__brand = brand
        self.__volume = volume
        
    def toggleMute(self):
        mute = False
        if mute == True:
            mute = False
        if mute == False:
            mute = True
    
    def increaseVolume(self):
        if self.__volume < 10:
            self.__volume += 1

    def decreaseVolume(self):
        if self.__volume > 0:
            self.__volume -= 1

    def __str__(self):
        if toggleMute == False:
            return "This" + str(self.__brand) + "phone is currently at" + str(self.__volume) + "volume."
        else:
            return "This" + str(self.__brand) + "phone is currently muted."
