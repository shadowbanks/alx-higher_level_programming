#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
reminder = abs(number) % 10
if (number < 0):
    reminder = reminder * -1
print(f"Last digit of {number} is {reminder}", end=" ")
if ((reminder) == 0):
    print("and is 0")
elif ((reminder) < 6):
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
