#!/usr/bin/python3

import sys
argv = sys.argv

if __name__ == "__main__":
    count = 1
    num = len(argv) - 1

    print("{} arguments".format(num), end="")
    if (num == 0):
        print(".")
    else:
        print(":")

    while (count <= num):
        print("{}: {}".format(count, argv[count]))
        count += 1
