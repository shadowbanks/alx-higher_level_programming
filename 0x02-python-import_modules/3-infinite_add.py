#!/usr/bin/python3

import sys
argv = sys.argv

if __name__ == "__main__":
    count = 1
    num = len(argv) - 1
    total = 0

    while (count <= num):
        total += int(argv[count])
        count += 1
    print("{}".format(total))
