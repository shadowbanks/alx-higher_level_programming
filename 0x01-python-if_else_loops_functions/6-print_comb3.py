#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if (i >= j):
            continue
        print("{}{}".format(i, j), end="")
        if (i == 8 and j == 9):
            break
        print(end=", ")
print()
