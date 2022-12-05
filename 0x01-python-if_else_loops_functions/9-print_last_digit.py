#!/usr/bin/python3
def print_last_digit(number):
    try:
        for i in str(number):
            pass
        print(i, end="")
        return int(i)
    except ValueError:
        pass
