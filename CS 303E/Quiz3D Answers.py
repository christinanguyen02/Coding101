# CS 303E Quiz 3D
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

import math

# Problem 1: Fancy Functions
def followsRule(num):
    
    sqrt = math.sqrt(num)

    # sqrt is in the form X.YZ
    # so we're checking that
    # X.YZ == X.00
    return sqrt == int(sqrt)

def rangeOfNums(lower, upper):
    
    count = 0

    for i in range(lower, upper + 1):
        if followsRule(i):
            count += 1

    return count


# Problem 2: Phone Class
class Phone:
    def __init__(self, brand, volume=5):
        
        self._brand = brand
        self._volume = volume
        self._muted = False # starts unmuted

    def toggleMute(self):
        
        self._muted = not self._muted

    def increaseVolume(self):
        
        self._volume = min(10, self._volume + 1)

    def decreaseVolume(self):
        
        self._volume = max(0, self._volume - 1)

    def __str__(self):

        volume_status = "muted"
        
        if not self._muted:
            volume_status = "at " + str(self._volume) + " volume"

        return "This " + self._brand + " phone is currently " + volume_status + "."

