#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    i = 1
    lenn = len(sys.argv)
    while i < lenn:
        total = total + int(sys.argv[i])
        i = i + 1
    print("{}".format(total))
