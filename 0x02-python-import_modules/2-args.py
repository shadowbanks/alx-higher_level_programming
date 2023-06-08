#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 1
    arg = len(sys.argv) - 1
    if arg == 0:
        print("{} arguments.".format(arg))
    else:
        if arg == 1:
            print("{} argument:".format(arg))
        else:
            print("{} arguments:".format(arg))
        while i <= arg:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
