#!/usr/bin/python3

def fizzbuzz():
    """Print number from 1 to 100,
    for all multiples of 3 print Fizz
    for all multiples of 5 print Buzz
    for all multiples of 3&5 print FizzBuzz
    """

    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (i % 3 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
