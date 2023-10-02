l = int(input())
a = int(input())
for i in range(0, 5):
    if a > l:
        sequence = a
        a = (3 * a + 3)
    elif a < l:
        sequence = a
        a = (8 * a - 3)
    else:
        sequence = a
        a = (a - 2) ** 2

print(sequence, end = ' ')
