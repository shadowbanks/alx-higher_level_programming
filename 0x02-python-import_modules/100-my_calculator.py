#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv

    inputs = len(argv) - 1

    if (inputs != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    oper = argv[2]
    b = int(argv[3])

    opers = {"+": add(a, b), "-": sub(a, b), "*": mul(a, b), "/": div(a, b)}

    if not (oper in opers):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, oper, b, opers[oper]))
