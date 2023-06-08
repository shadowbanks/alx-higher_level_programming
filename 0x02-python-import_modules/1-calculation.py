#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    add_r = add(10, 5)
    sub_r = sub(10, 5)
    div_r = div(10, 5)
    mul_r = mul(10, 5)

    print("{} + {} = {}".format(a, b, add_r))
    print("{} - {} = {}".format(a, b, sub_r))
    print("{} * {} = {}".format(a, b, mul_r))
    print("{} / {} = {}".format(a, b, div_r))
