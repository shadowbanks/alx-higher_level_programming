#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while (i < x):
        try:
            num = int(my_list[i])
        except (ValueError, IndexError):
            i += 1
            pass
        else:
            count += 1
            i += 1
            print(num, end="")
    print()
    return (count)
