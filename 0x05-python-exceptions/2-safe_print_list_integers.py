#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while (i < x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
            i += 1
    except (ValueError, TypeError):
        i += 1
        pass
    print()
    return (count)
