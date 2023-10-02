hwCount = 1
hwTotal = 0
while (hwCount <= 3):
    hwScore = int(input("  Enter HW1 grade: "))
    if hwScore > 10 or hwScore < 0:
        print("  Grade must be in range [0..10]. Try again.")
        hwScore = int(input("  Enter HW1 grade: " ))
    hwCount += 1
    hwTotal += hwScore
